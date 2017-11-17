### Sample customer lookup api
Built using AWS Lambda+Dynamodb+Serverless

Steps to build:
1. Create the API
```
sls deploy
```
This creates the API and the Dynamodb tables. <br>

2. Load data onto dynamoddb
```
python loadCustomerData.py
```

3. Check the API using curl
To list all the customers
```
curl https://6pqdcqcdyb.execute-api.us-east-1.amazonaws.com/dev/customer/
```
Sample output:
```
[{"info": {"due_date": "09/15/17", "available_credit": 6655, "available_notes_value": "20", "name": ["Sarah Conor"], "rewards_points": 6, "current_balance": 800, "pbpd_available": 2, "statement_balance": 1542, "lastest_date": "08/21/17", "available_notes": ["8255-4455-2233-1111; Access Code 456", "8255-4455-2233-1333; Access Code 567"]}, "dob": "06/06", "phonenumber": 30325259328, "zipcode": 30302}, {"info": {"due_date": "07/15/17", "available_credit": 548, "available_notes_value": "30", "name": ["Rudolf Roland"], "rewards_points": 7, "current_balance": 452, "pbpd_available": 3, "statement_balance": 452, "lastest_date": "06/15/17", "available_notes": ["8255-4455-4433-2233; Access Code 678", "8255-4455-4433-2444; Access Code 789"]}, "dob": "07/07", "phonenumber": 30325259327, "zipcode": 30303}, {"info": {"due_date": "06/15/17", "available_credit": 5548, "available_notes_value": "40", "name": ["Brad Doebelin"], "rewards_points": 8, "current_balance": 1452, "pbpd_available": 1, "statement_balance": 2452, "lastest_date": "05/18/17", "available_notes": ["8255-4455-3344-2233; Access Code 123", "8255-4455-3344-2444; Access Code 234"]}, "dob": "05/05", "phonenumber": 30325259329, "zipcode": 30301}]
```

To get one single customer with their phone number
```
curl https://6pqdcqcdyb.execute-api.us-east-1.amazonaws.com/dev/customer/30325259328
```
Sample output:
```
{"info": {"M": {"due_date": {"S": "09/15/17"}, "available_credit": {"N": "6655"}, "available_notes_value": {"S": "20"}, "name": {"L": [{"S": "Sarah Conor"}]}, "rewards_points": {"N": "6.4"}, "current_balance": {"N": "800"}, "pbpd_available": {"N": "2"}, "statement_balance": {"N": "1542"}, "lastest_date": {"S": "08/21/17"}, "available_notes": {"L": [{"S": "8255-4455-2233-1111; Access Code 456"}, {"S": "8255-4455-2233-1333; Access Code 567"}]}}}, "dob": {"S": "06/06"}, "phonenumber": {"N": "30325259328"}, "zipcode": {"N": "30302"}}
```
