
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from firebase_admin import db
from flask_socketio import SocketIO,send
import datetime
from flask_cors import CORS
import time
import json
cred = credentials.Certificate("key.json")


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://map-backend-66850-default-rtdb.firebaseio.com/'
})
ref=db.reference("/")

app = Flask(__name__)
CORS(app)


@app.route("/delete", methods=['DELETE'])
def delete():
    
    try:
        idm=request.args.get('current_id')
        data=ref.get()
        for key, value in data.items():
            tmp_idm=json.loads(idm)
            print(tmp_idm['date'])
            print(value['date'])
            print("-----------")
            if(str(value["date"]) == str(tmp_idm['date'])):
                print("hey")
                ref.child(key).set({})
        return "correct"
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route("/getall", methods=['GET'])
def greeting():

    try:
        data=ref.get()
        print(data)
        if data==None:
            return {}
        
        return data
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/add', methods=['POST'])
def create():
    lat=request.args.get('lat')
    lng=request.args.get('lng')
    ts = time.time()
    new_ts=str(ts)
    print(new_ts)
    print(isinstance(new_ts,str))
    output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        ref.push({ 
            
                  
                            
                            "lat":lat,
                            "lng":lng,
                            "date":output_date
            
           
        })

        

    # Enable Access-Control-Allow-Origin
        return "200"
    except Exception as e:
        return f"An Error Occured: {e}"