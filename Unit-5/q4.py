from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        day = request.form.get('day')
        session = request.form.get('session')
        with open('schedule.csv', 'r') as f:
            reader = csv.reader(f)
            headers = next(reader) # skip headers
            data = [row for row in reader if row[0] == day and row[1] == session]
        return render_template('schedule.html', data=data)
    else:
        return render_template('schedule-form.html')

if __name__ == '__main__':
    app.run(debug=True)
