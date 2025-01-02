from flask import jsonify

from DBService import insertdata

import logging
from flask import Flask, jsonify
from flask_cors import CORS
from oracledb import connect


def register_appointment(request):
    data = request.json
    firstname = data.get('firstName')
    lastname = data.get('lastName')
    email = data.get('email')
    phoneno = data.get('phoneNo')
    address = data.get('address')
    doctor = data.get('doctor')
    date = data.get('date')
    time = data.get('time')

    if firstname == '':
        return jsonify({'error': 'first name cannot be empty'}), 400
    if lastname == '':
        return jsonify({'error': 'last name cannot be empty'}), 400

    if email == '':
        return jsonify({'error': 'email cannot be empty'}), 400
    if phoneno == '':
        return jsonify({'error': 'phoneno cannot be empty'}), 400

    if address == '':
        return jsonify({'error': 'address cannot be empty'}), 400

    if doctor == '':
        return jsonify({'error': 'doctor cannot be empty'}), 400

    if date == '':
        return jsonify({'error': 'date cannot be empty'}), 400

    if time == '':
        return jsonify({'error': 'time cannot be empty'}), 400
    print('before function')
    if firstname and lastname and email and phoneno and address:
        insertdata(firstname, lastname, email, phoneno, address, doctor, date, time)
        print('after function')
        return jsonify({'success': 'user data  recived'}), 200
    else:
        return jsonify({'error': 'user data not recived'}), 400

def get_appointments():
    try:
        # Connect to the Oracle database
        connection = connect(user='system', password='1234', dsn="localhost:1521/orcl")
        cursor = connection.cursor()

        # Query to fetch all appointments
        cursor.execute("SELECT * FROM AHOSPITAL")

        # Prepare data as a list of dictionaries
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        connection.close()
        return jsonify(data), 200

    except Exception as e:
        logging.error(f"Error retrieving appointments: {e}")
        return jsonify({'error': 'Error retrieving appointments'}), 500