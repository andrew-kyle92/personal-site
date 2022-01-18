import datetime

from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from forms import ContactForm
from dotenv import dotenv_values

from email_class import SendEmail
import os
from datetime import date
from dateutil.relativedelta import relativedelta

config = dotenv_values(".env")
app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE'] = 'full'
Bootstrap(app)
app.config["SECRET_KEY"] = config.get("SECRET_KEY")
send_mail = SendEmail()


@app.route("/", methods=["POST", "GET"])
def index():
    dob = datetime.datetime(1992, 1, 29)
    preset_date = datetime.datetime.today()
    it_start = datetime.datetime(2016, 5, 12)
    time_diff_music = relativedelta(preset_date, dob)
    time_diff_it = relativedelta(preset_date, it_start)
    age = time_diff_music.years
    it_exp = time_diff_it.years
    guitar_exp = age - 12
    year = datetime.datetime.now().strftime("%Y")
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            msg_info = {
                "name": form.name.data,
                "email": form.email.data,
                "phone": form.phone.data,
                "message": form.message.data
            }
            send_mail.send_email_message(msg_info)
            flash(message="Your message was sent, successfully!", category="Email Sent Success")
            return redirect(url_for("index"))

    return render_template("index.html", form=form, year=year, guitar_years=guitar_exp, work_exp=it_exp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)