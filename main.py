from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    name = data['name']
    email = data['email']
    message = data['message']
    with open('database.txt', mode='a') as db:
        db.write(f'\n{name}, {email}, {message}')


def write_to_csv(data):
    name = data['name']
    email = data['email']
    message = data['message']
    with open('database.csv', newline='', mode='a') as db2:
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again.'


@app.route('/<string:pagename>')
def test(pagename):
    return render_template(pagename)
