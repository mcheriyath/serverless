from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('customers-table-dev')

with open("customerdata.json") as json_file:
    customers = json.load(json_file, parse_float = decimal.Decimal)
    for customer in customers:
        phonenumber = int(customer['phonenumber'])
        zipcode = int(customer['zipcode'])
        dob = customer['dob']
        info = customer['info']

        print("Adding customer info:", phonenumber, zipcode, dob, info)

        table.put_item(
           Item={
               'phonenumber': phonenumber,
               'zipcode': zipcode,
               'dob': dob,
               'info': info,
            }
        )
