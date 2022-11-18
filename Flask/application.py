from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"] = "asdfghjrox@gmail.com"
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail=Mail(app)



SPORTS   = [
    "cricket",
    "football",
    "snooker",
    "chess",
    "volleyball"
]


@app.route("/")
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():
    email= request.form.get("email")
    sport=request.form.get("sports") 
    if sport not in SPORTS:
        return render_template('errors.html', message="invalid sports")
    if not email:
         return render_template('errors.html', message="missing email")
    if not sport:
         return render_template('errors.html', message="missing sports")
 
    
    message = Message("You are registered", recipients=[email])
    mail.send(message)

    return render_template("success.html")
   


if __name__=="__main__":
    app.run(debug=True)

