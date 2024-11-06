from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n < 0:
        return "Error: Tu numero no puede ser negativo"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/factorial/<int(signed=True):n>', methods=['GET'])
def get_factorial(n):
    factorial = factorial(n)
    return jsonify(factorial)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
