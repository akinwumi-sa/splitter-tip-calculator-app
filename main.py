from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        total_bill = int(request.form['bill'])
        tip_percent = float(request.form['options'])
        num_persons = int(request.form['persons'])
        tip_amount = total_bill * tip_percent

        if tip_amount != 0.0:
            tip_amount_per_person = round(tip_amount / num_persons, 2)
            tip_amount_per_person_fmt = "{:.2f}".format(tip_amount_per_person)
        else:
            tip_amount_per_person = 0
            tip_amount_per_person_fmt = "{:.2f}".format(0)
        if num_persons != 0:
            total_bill_per_person = round(total_bill / num_persons, 2)
            total_bill_per_person_fmt = "{:.2f}".format(total_bill_per_person)
        else:
            total_bill_per_person = 0
            total_bill_per_person_fmt = "{:.2f}".format(0)
        return render_template('index.html', tip=tip_amount_per_person_fmt, bill=total_bill_per_person_fmt,
                               tot_bill=total_bill, num_pers=num_persons, perce=tip_percent)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
