from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os
import threading
from generate_process import text_to_audio, create_reel

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static/reels', exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []

        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        for key, value in request.files.items():
            print(key, value)
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder_path, filename))
                input_files.append(filename)

        with open(os.path.join(folder_path, "desc.txt"), "w") as f:
            f.write(desc)

        for f in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"), "a") as inp:
                inp.write(f"file '{f}'\nduration 1\n")

        # run reel creation in background thread
        def process():
            text_to_audio(rec_id)
            create_reel(rec_id)
            with open("done.txt", "a") as f:
                f.write(rec_id + "\n")

        thread = threading.Thread(target=process)
        thread.start()

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)