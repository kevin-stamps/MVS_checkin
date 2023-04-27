from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    address = request.form['address']
    zipcode = request.form['zipcode']
    phone = request.form['phone']
    email = request.form['email']
    branch = request.form['branch']
    relationship = request.form['relationship']
    reason = request.form['reason']

    # Modified code to add a dropdown box for the reason for visit question
    reason_options = ['Employment', 'Emergency Support – Community One Source', 'Transition Support', 'Fitness Center', 'Computer Lab', 'Gaming Center', 'Laundry Facilities', 'Meeting with VA', 'Meeting with other Resources', 'Programs', 'Class Offering']
    if reason not in reason_options:
        return '<h1>Please select a valid reason for visit.</h1>'
    if reason == 'Other':
        return render_template('other_reason.html', name=name, address=address, zipcode=zipcode, phone=phone, email=email, branch=branch, relationship=relationship)

    with open('visitors.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'address', 'zipcode', 'phone', 'email', 'branch', 'relationship', 'reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'name': name, 'address': address, 'zipcode': zipcode, 'phone': phone, 'email': email, 'branch': branch, 'relationship': relationship, 'reason': reason})

    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

