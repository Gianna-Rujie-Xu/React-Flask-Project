from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Rujie Xu's Home Page</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { color: #333; }
            p { color: #555; }
            .section { margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <h1>Welcome to Rujie(Gianna) Xu's Home Page!</h1>
        <div class="section">
            <p><strong>University:</strong> University College London (UCL)</p>
            <p><strong>Major:</strong> BSc Information Management for Business</p>
            <p><strong>Acquired Programming Languages:</strong> Python, SQL, Cypher, HTML</p>
        </div>
        <div class="section">
            <p>This is a Flask-React project built by Rujie, who self-learned Flask, React, and Heroku deployment through YouTube tutorial videos.</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)

