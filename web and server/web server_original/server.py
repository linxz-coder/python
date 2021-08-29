from flask import Flask, render_template, url_for

app = Flask(__name__)

# 127.0.0.1:5000/Lin/5
@app.route("/<username>/<int:post_id>")
def hello_world(username = None, post_id=None):
    # return "<h1>Cheer, Man!</h1>"
    # return "Cheer, Man!"
    return render_template('index.html', name = username, post_id = post_id)

@app.route("/about")
def blog():
    return render_template('about.html')

@app.route("/blog/2020")
def blog2():
    return "<p>This is good</p>"