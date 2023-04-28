from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

connect_string = 'mongodb+srv://niksonsihombing18:nikson@cluster0.zhoewhm.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connect_string)
db = client.dbsparta


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    # sample_receive = request.args.get('sample_give')
    # print(sample_receive)

    articles = list(db.diary.find({}, {'_id': False}))
    return jsonify({'articles': articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    # sample_receive = request.form.get('sample_give')
    # print(sample_receive)
    title_receive = request.form.get('title_give')
    content_receive = request.form.get('content_give')

    doc = {
        'title':title_receive,
        'content':content_receive
    }
    db.diary.insert_one(doc)

    return jsonify({'msg':'Upload complete!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)