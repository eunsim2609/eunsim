from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def write_order():
    user_name = request.form['name_give']
    number = request.form['number_give']
    addr = request.form['address_give']
    phone = request.form['phone_give']

    doc = {
        'name': user_name,
        'number': number,
        'addr': addr,
        'phone': phone
    }
    db.order.insert_one(doc)
    return jsonify({'result':'success','msg': '주문이 완료되었습니다.'})

@app.route('/order',methods=['GET'])
def read_order():
    order_list=list(db.order.find({},{'_id':0}))
    return jsonify({'result':'success','order':order_list})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)