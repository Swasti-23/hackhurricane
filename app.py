# app.py (Flask app)
from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import time
import json
app = Flask(__name__)
cred=credentials.Certificate({
  "type": "service_account",
  "project_id": "tryhackathon",
  "private_key_id": "6b5100d7909676ddb2d16033abe01d0d7e7d6077",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCila3K9vRBRkEe\nVdGD8Z7fEM6K5ADWyLg4R40QuKGTgKS5ETyZOz1CfyaC/djz0t9e5HxihOm7Ve0y\nFRWMNxmPC/e6xsF9FYX1y/3DA9BleOJp0htCTo1iDurds4iCPBxD3P6BDnh78zuK\n7PEdvlkDKn9nlLyj/UKniUIrP8fU7ZtdinmXrLqhXL0M/zAiRyEcZKsPPrIsourG\nca/t41oY/Bk60yTaNZHVBzvK0dy6xYfmEtq5+GslXzpS/CAD/+aXFPkC8rXLiTJY\nUQtUNvWFL1LnJsuHkQNJVpo86qVkqpQk4a2wbFdnqXKKXqmTectlklqlwsVeYMl5\npt34qcotAgMBAAECgf8iPePxxeaA2OBeGIpH1QY2H2lgrHnWF/AJ6l02EwH0pDi3\nwX7scXg1c7y+BI3szDy/KjVdinYE6SlLovp8IslUl0YAJbFv5q3lVqaGAVz4AhMC\ntn2HOYQNYuw+79DlnO4BskmSZLnQtn7pLiiaBbzkLc8nbEFOnchWq1HZn1U27X4a\nhCn0MbPRkAPhkbN6haB48U5IYy+MwVzroKzo0rmOsWSkL9/enI8fMUe1CMyw0t/+\nn9CbvGV5Soi+Iq6h9XLvHFE2CFrrKXhcdnKaJppxt+LRWH/AHVCLnNYIap/Sz1W7\nktHrtJ8BWiArXTq1WxbZeQmMuQk4UfHS9I+vtakCgYEAzjjFIsNxXFbnwuu94puy\nob1Z+5ZPjatQXlR3tSJQbMpiwt5NCRNJG2OVTJV/QzGV6eHnB70AtK25U0KAVaTz\neKgPqCFb7d2+ZoRBnXB9mosAPkuI3XIyR9mDBZXFJx3bHp4+RRZ5zD3Ls4avef7e\nG6jpLcWFgRwwJnD+1RzoXEUCgYEAydRoRfT0l5pPyCWaVZuttzAFzakUfD8hG6Kw\nUz/oi79cPjiIaETQUCRIECE7nmb36UPgwnPS5I5/fBJypqy482N2E5t5+mkpGUUl\nTrgg1l8i1FZ2C7K0SLlfBk+w0J/A282AvB2VwfPJVz8VWsJ/XguAKspt7EuT9dYW\n+MEleMkCgYAaFSIR6IhQ9ojvpWNp4ulv/YQBBxzevTk4BRTy6vkjGWHuZbF2oWLQ\nvQKoIgxrkjz0zOasmuIY+BQFjNawfmFw9EiuqjF3X2Fyk+28nPq17jjEqEcSQxxK\n7B7fOPcroGITeE5F7LbQ90vpU/KjynGLLAz6Bg6BqvAIHKiOic51xQKBgQDIsxHl\nzwqS3v5LFyl7y81ZBsYelu4qB1TS+FrCziBfJzGBJhJvLU7BAvMuJv30LIyGR9tv\nQmIKqbEYHfgoykU4skUuhkMrwfr+iAXrW6o7wmsOH9RPGauxTbSyv/gh3VqYuKg1\naG4NanFi8vY3RIYHbQRMiPP6L8W4huZdAyRSEQKBgE54frmtb+X+CqV6xZF7yd6E\n8BfCMAOjPKzyP41jWXO6ewVOfrny9jc9mDBZVJhnitT2KUrSMgWxLlLGmihXszwy\nMLv4Agu2eVO10UUb4sagcim+QFYrvJ4U+SWnMgf7DA4EcqAk+QmGTtNOFBBDjlIK\nf9WvY2Lm+hODod0N+8+5\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-38536@tryhackathon.iam.gserviceaccount.com",
  "client_id": "118092460552172352710",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-38536%40tryhackathon.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred, {'databaseURL': 'https://tryhackathon-default-rtdb.firebaseio.com/'})
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    json_content = data.get('jsonContent', '')
    db_url = data.get('dbUrl', '')
    
    cred = credentials.Certificate(json.loads(json_content))
    print("first phase done!!")
    time.sleep(1)
    firebase_admin.initialize_app(cred, {'databaseURL': db_url})
    print("second phase done!!")
    time.sleep(1)
    print("connection done")
    
    
    # Process the JSON content and database URL as needed
    print('Received JSON content:', type(json_content))
    print('Received Database URL:', type(db_url))

    return jsonify({'message': 'Data received successfully'})
def live(cred):
    a = cred.split("-")
    url = ""
    username = a[0]
    password = a[1]
    data_ref = db.reference('/')

    for i in data_ref.get():
        if i == username:
            url = "/" + username
            pass_data_ref = db.reference(url)
            
            for j in pass_data_ref.get():
                if pass_data_ref.get()[j] == password:
                    # Return a JSON response on success
                    return jsonify({'message': 'Success', 'template': 'database.html'})
                else:
                    response_data = {'message': 'Incorrect password'}
        else:
            response_data = {'message': 'No user exists'}

    # Return a JSON response on failure
    return jsonify(response_data)





if __name__ == '__main__':
    app.run(debug=True)
