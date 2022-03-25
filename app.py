from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yt2mp3")
def yt2mp3():
    return render_template("yt2mp3.html")

@app.route("/yt2mp4")
def yt2mp4():
    return render_template("yt2mp4.html")

@app.route("/download-mp3", methods=['POST'])
def download_mp3():
    from main import download
    link = request.form.get("link")
    name = download.download_mp3(link)
    return send_file(name, as_attachment=True)

@app.route("/download-mp4", methods=["POST"])
def download_mp4():
    link = request.form.get('link')
    resolution = request.form.get("quality")
    from main import download
    name = download.download_mp4(link=link, resulution=resolution)
    return send_file(name, as_attachment=True)

if __name__ == "__main__":
    app.debug = True
    app.run(port=9876)