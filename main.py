from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['portfolio']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contactus', methods=['POST'])
def contactus():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    doc = {
        'name' : name,
        'email' : email,
        'message' : message
    }
    
    db.contactus.insert_one(doc)
    return "Thank you for contacting us!"

if __name__ == '__main__':
    app.run(debug=True,port=80)