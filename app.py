pip install flask
python
Copy code
from flask import Flask, render_template
# Create the Flask app
app = Flask(__name__)
# Define the home route
@app.route("/")
def home():
    return "<h1>Welcome to My Website!</h1><p>This is the home page.</p>"
# Define another route
@app.route("/about")
def about():
    return "<h1>About</h1><p>This is a simple website created using Flask.</p>"
# Run the application
if __name__ == "__main__":
    app.run(debug=True)
