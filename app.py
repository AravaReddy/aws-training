from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle the form submission
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
