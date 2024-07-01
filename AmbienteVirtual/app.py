from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return "Hello world"

@app.route('/login',methods=["POST"])
def login():
    data = request.get_json()
    mail = data.get("email")
    pwd = data.get("password")
    if mail == "email" and pwd == "password":
        return jsonify({"Exito": "Exito"}) 
    else: 
        return jsonify({"Chafa": "Chafa"})
        

if __name__ == "__main__":
    app.run(debug = True)