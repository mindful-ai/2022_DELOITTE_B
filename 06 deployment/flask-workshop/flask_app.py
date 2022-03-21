from flask import Flask
app = Flask(__name__)

# 127.0.0.1:5000/
@app.route('/')
def index():
    return ('''
            <h1 style="color:#F05647">Welcome to Flask Experiments!</h1>
            <button>Click Me!</button>
            ''')


if __name__ == "__main__":
    app.run()