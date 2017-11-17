import os

import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

EMPLOYEES_TABLE = os.environ['EMPLOYEES_TABLE']
client = boto3.client('dynamodb')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/employees/<string:employee_id>")
def get_employee(employee_id):
    resp = client.get_item(
        TableName=EMPLOYEES_TABLE,
        Key={
            'employeeId': { 'N': employee_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'Employee does not exist'}), 404

    return jsonify({
        'employeeId': item.get('employeeId').get('N'),
        'name': item.get('name').get('S')
    })


@app.route("/employees", methods=["POST"])
def create_employee():
    employee_id = request.json.get('employeeId')
    name = request.json.get('name')
    if not employee_id or not name:
        return jsonify({'error': 'Please provider employeeId and name'}), 400

    resp = client.put_item(
        TableName=EMPLOYEES_TABLE,
        Item={
            'employeeId': {'N': employee_id },
            'name': {'S': name }
        }
    )

    return jsonify({
        'employeeId': employee_id,
        'name': name
    })
