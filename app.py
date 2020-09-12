from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
import datetime as dt

import NewYorkTaxiFarePrediction as tm

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        passenger_count = request.form.get('passenger')
        total_distance = request.form.get('distance')
        doj = request.form.get('doj')
        time = request.form.get('time')

        month = int(doj.split('-')[1])
        day = int(doj.split('-')[2])
        hour = int(time.split(':')[0])
        minute = int(time.split(':')[1])

        datetimeobj = dt.datetime.strptime(doj, '%Y-%m-%d')

        if datetimeobj.weekday() < 5:
            weekday = 0
        else:
            weekday = 1

        if hour < 12:
            meridiem = 0
        else:
            meridiem = 1


        prediction = round(float(tm.predict_fare(passenger_count, month, day, hour, minute, meridiem, weekday, total_distance)), 2)
        print(prediction)
        return render_template("index.html", prediction_text="The estimated taxi fare is $" + str(prediction))

    return render_template("index.html")


if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug=True)