from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

r = requests.get("https://api.github.com/users/radk0n9/repos")
github_json = r.json()
for p in github_json:
    print(p["created_at"].split("T")[0])
# first_one = github_json[0]
# print(first_one["name"])


@app.route("/")
@app.route("/index.html")
def home():
    how_many_items_portfolio = github_json
    return render_template("index.html", work_contents=how_many_items_portfolio)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)


if __name__ == "__main__":
    app.run(debug=True)
