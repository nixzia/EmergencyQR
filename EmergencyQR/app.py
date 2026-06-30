from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/qr/<room>")
def qr_redirect(room):

    with open("classroom_links.json","r") as file:
        links = json.load(file)

    if room in links:
        return redirect(links[room])

    return "Classroom not found.",404

if __name__ == "__main__":
    app.run(debug=True)