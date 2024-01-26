from flask import Flask, render_template

app = Flask(__name__)

# app.static_folder = "static"
# app.static_url_path = "/static"

@app.route("/")
def index():
    return render_template("first-main.html")

@app.route("/slide")
def slide():
    return render_template("slide-16-9-2.html")

@app.route("/main-character")
def main_character():
    return render_template("main-character.html")

@app.route("/main-character-in")
def main_character_in():
    return render_template("main-character-introduction.html")

@app.route("/sup-character")
def sup_character():
    return render_template("sup-character.html")

@app.route("/sup-character-in")
def sup_character_in():
    return render_template("sup-character-introduction.html")

@app.route("/prop")
def prop():
    return render_template("prop.html")

@app.route("/prop-character-in")
def prop_character_in():
    return render_template("prop-character-introduction.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/save-story")
def save_story():
    return render_template("save-story.html")

@app.route("/save-success")
def save_success():
    return render_template("story-EmS.html")

@app.route("/user-information")
def user_information():
    return render_template("user-information.html")

@app.route("/user-information-2")
def user_information_2():
    return render_template("user-information-2.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
