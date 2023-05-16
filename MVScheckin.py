from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['date']
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    address = request.form['address']
    zipcode = request.form['zipcode']
    phone = request.form['phone']
    email = request.form['email']
    which_applies_to_you = request.form['which_applies_to_you']

    reason = request.form['reason']

    # Modified code to add a dropdown box for the reason for visit question
    reason_options = ['Employment', 'Emergency Support – Community One Source', 'Transition Support', 'Fitness Center', 'Computer Lab', 'Gaming Center', 'Laundry Facilities', 'Meeting with VA', 'Meeting with other Resources', 'Programs', 'Class Offering']
    if reason not in reason_options:
        return '<h1>Please select a valid reason for visit.</h1>'
    if reason == 'Other':
        return render_template('other_reason.html', first_name=first_name, last_name=last_name, address=address, zipcode=zipcode, phone=phone, email=email, which_applies_to_you=which_applies_to_you)

    if not first_name or not last_name:
        return '<h1>Please enter a first and last name.</h1>'

    with open('visitors.csv', 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'zipcode', 'phone', 'email', 'which_applies_to_you', 'reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'first_name': first_name, 'last_name': last_name, 'address': address, 'zipcode': zipcode, 'phone': phone, 'email': email, 'which_applies_to_you': which_applies_to_you, 'reason': reason})

    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)
