from flask import Flask, request
from flask import render_template 
app = Flask(__name__)
src = None
dest = None

@app.route("/")
def vivek():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    src = request.form['source']
    dest = request.form['destination']  
    return 'submitted'

if __name__ == '__main__':
    app.run()