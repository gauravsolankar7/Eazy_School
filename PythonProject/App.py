from flask import Flask,request, jsonify
from flask_cors import CORS

from AppointmentService import register_appointment, get_appointments
from DBService import insertdata
from EmailService import send_email


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/post_data', methods=['GET', 'POST'])
def add_appointment():
    return register_appointment(request)

@app.route('/get_data', methods=['GET'])
def appointments():
    return get_appointments()

@app.route('/send_emails', methods=['GET', 'POST'])
def send_emails():
    return send_email(request)

if __name__ == '__main__':
    app.run(debug=True)