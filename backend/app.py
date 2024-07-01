from flask import Flask

app = Flask(__name__)
# Initialize SQLAlchemy with Flask app


@app.route('/')
def index():
    return "YOU ARE HOSTED WITH DOCKER"
if __name__ == '__main__':
    app.run(debug=True)