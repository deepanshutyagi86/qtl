from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect("https://www.youtube.com/watch?v=jo6iAkSoraY")

if __name__ == '__main__':
   app.run(host='192.168.29.39', port=5000, debug=True)
 