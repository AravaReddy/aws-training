from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve inputs from the form
        operation = request.form['operation']
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float, default=None)

        # Perform calculations based on the selected operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))
        elif operation == 'log':
            result = math.log10(num1) if num1 > 0 else 'Error: Logarithm undefined for non-positive values'
        elif operation == 'sqrt':
            result = math.sqrt(num1) if num1 >= 0 else 'Error: Square root of negative number'
        else:
            result = 'Invalid operation'

        return render_template('calculator.html', result=result)
    except Exception as e:
        return render_template('calculator.html', result=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
