from flask import Flask, request

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
            a { text-decoration: none; color: blue; }
            img { max-width: 100%; height: auto; margin-top: 20px; }
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
        <div class="section">
            <!-- Display the image here -->
            <img src="/static/images.jpg" alt="Hi cat">
        </div>
        <div class="section">
            <p><a href="/feedback">Leave Feedback</a></p>
        </div>
    </body>
    </html>
    """
    return html_content


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback_text = request.form.get("feedback")
        print("Feedback received:", feedback_text)
        return """
        <h2>Thank you for your feedback!</h2>
        <p><a href="/">Return Home</a></p>
        """
    return """
    <h2>Leave Your Feedback</h2>
    <form method="post" action="/feedback">
        <textarea name="feedback" rows="4" placeholder="Enter your feedback here..."></textarea><br>
        <input type="submit" value="Submit Feedback">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
