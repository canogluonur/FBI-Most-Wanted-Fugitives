from flask import Flask, jsonify, render_template
import requests
import json
from flask_cors import CORS


app=Flask(__name__)
CORS(app)


@app.route('/home',methods=['GET'])
def index():
    response = requests.get('https://api.fbi.gov/wanted/v1/list')
    data = json.loads(response.content)
    return  data
    

        
@app.route("/book")
def hadi():
    response = requests.get('https://api.fbi.gov/wanted/v1/list',)
    data = json.loads(response.content)
    books=[
                 
        {
          "id":data['items'][10]['files'][0]['url'],
           "title":data['items'][10]['title'],
           "images":data['items'][10]['images'][1]["original"]}
        ,{
    
        "id":data['items'][9]['files'][0]['url'],
        "title":data['items'][1]['title'],
        "images":data['items'][9]['images'][1]["original"]},
        {
        
        "id":data['items'][3]['files'][0]['url'],
        "title":data['items'][3]['title'],
        "images":data['items'][3]['images'][1]["original"]   
        },
        {
        "id":data['items'][13]['files'][0]['url'],
        "title":data['items'][13]['title'],
        "images":data['items'][13]['images'][1]["original"]
        },
        {
        "id":data['items'][17]['files'][0]['url'],
        "title":data['items'][17]['title'],
        "images":data['items'][17]['images'][1]["original"] 
        },
        {
        "id":data['items'][18]['files'][0]['url'],
        "title":data['items'][18]['title'],
        "images":data['items'][18]['images'][1]["original"] 
        },
        {
        "id":data['items'][14]['files'][0]['url'],
        "title":data['items'][14]['title'],
        "images":data['items'][14]['images'][1]["original"] 
        },
        {
        "id":data['items'][1]['files'][0]['url'],
        "title":data['items'][1]['title'],
        "images":data['items'][1]['images'][1]["original"] 
        },
        {
        "id":data['items'][19]['files'][0]['url'],
        "title":data['items'][19]['title'],
        "images":data['items'][19]['images'][1]["original"]
        },
        {
        "id":data['items'][2]['files'][0]['url'],
        "title":data['items'][2]['title'],
        "images":data['items'][2]['images'][1]["original"]
        }
        ]
    
    return jsonify(books)

@app.route("/")
def newhome():
    return render_template('index.html')
 


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)