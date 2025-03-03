from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/members")
def members():
    return {"members": ["Gianna", "Ethan", "Adrianna"]}

if __name__ == "__main__":
    app.run(debug=True)
