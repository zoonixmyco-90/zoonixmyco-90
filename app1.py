from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def home_user():
    return render_template ("home.html")

@app.route("/home1")
def home1_user():
    return render_template ("home1.html")


@app.route("/fullcode")
def fullcode_user():
    return render_template ("full code.html")

if __name__ == '__main__':
    app.run(debug=True)
