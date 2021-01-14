from flask import Flask 

app = Flask(__name__) # name in this case is going to act as main
 
@app.route('/')
def index():
    return "Hello world"
@app.route('/lakshmi')
def lakshmi():
    return "Hello Lakshmi"
if __name__ == '__main__':
    app.run(debug=True)