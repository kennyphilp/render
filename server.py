from flask import Flask, render_template
import random
import datetime as dt


app = Flask(__name__)


@app.route('/')
def home():

    currentDate=dt.datetime.today()

    formattedDate= currentDate.strftime("%x")
    formattedTime = dt.datetime.now().strftime("%H:%M:%S")
    print("The date is " + formattedDate)
    return render_template("index.html", displayDate = formattedDate, displayTime=formattedTime)

if __name__=="__main__":
    app.run(debug=True)