from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
token = "ajkjd77sdlkjf&&8f"

@app.route('/login', methods=['POST'])
def index():
    user = request.form['user']
    pwd = request.form['password']
    print(user)
    if(user == "admin" & pwd == "admin" ):
        user: {
            "name": "David Ramirez",
            "company": "Motion Miners",
            "token": token
        }
        response = jsonify(user)
        response.status_code = 200
    else:
        response.status_code = 401
    return response


