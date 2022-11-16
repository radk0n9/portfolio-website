from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import requests
import os
import smtplib

app = Flask(__name__)
Bootstrap(app)

load_dotenv()
EMAIL_PYTHON = os.getenv("EMAIL")
PASSWORD_PYTHON = os.getenv("PASSWORD")

r = requests.get("https://api.github.com/users/radk0n9/repos")
github_json = r.json()


# for p in github_json:
#     print(p["created_at"].split("T")[0])
# first_one = github_json[0]
# print(first_one["name"])

def send_email(name, email, subject, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=str(EMAIL_PYTHON), password=str(PASSWORD_PYTHON))
        connection.sendmail(from_addr=EMAIL_PYTHON,
                            to_addrs=EMAIL_PYTHON,
                            msg=f'Subject: New Message from Portfolio Website\n\n'
                                f'Name: {name}\n'
                                f'Email: {email}\n'
                                f'Subject: {subject}\n'
                                f'Message: {message.encode("utf8")}')


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def home():
    how_many_items_portfolio = github_json
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(message)
        send_email(name, email, subject, message)
    return render_template("index.html", work_contents=how_many_items_portfolio)


if __name__ == "__main__":
    app.run(debug=True)
