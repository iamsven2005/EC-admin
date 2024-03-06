from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__)
uri = "mongodb+srv://iamsven2005:BIbQ7Lgmq6ZbdU14@cluster0.1amm90a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client['EC']
collection = db['rewards']
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    cursor = collection.find({})
    about_data = [doc for doc in cursor]
    return render_template('about.html', about_data=about_data)


    

