import os
from flask import Flask, render_template, request, redirect, session, url_for
from src import inpaint



tmp_dir = os.path.abspath("./tmp/")
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = tmp_dir

@app.route("/", methods=["GET"])
def main():
    # return the main page (u should make it first tho)
    status = request.args.get("status")
    out_url = request.args.get("out_url")
    return render_template("index.html", status=status, out_url=out_url)

@app.route("/api", methods=["POST"])
def api():
    f = request.files["face"]
    p = request.files["pic"]
    out_url = ""
    if f and p:
        # save image to tmp (if image exists)
        face_path = os.path.join(tmp_dir, "face.jpg")
        pic_path = os.path.join(tmp_dir, "pic.jpg")
        f.save(face_path)
        p.save(pic_path)
        # call the api stuff TODO
        inpaint.chugjug_with_you(face_path, pic_path)
        out_url = "out.jpg"
        # redirect to root with good status
        status = "ok"
    else:
        # u effed up and image does not exist; redirect to root with error status
        status = "error"
    return redirect(url_for("main", status=status, out_url=out_url))

# -------------------- STINKY OAUTH, DO NOT TOUCH -----------------------------
# We don't have time to do this stuff lol
# We just get the tokens via the frontend and call it a day