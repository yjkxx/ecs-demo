from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Cloud! - Rev. 5:continuous delivery'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

