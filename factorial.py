from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n < 0:
        return None
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/<int(signed=True):n>', methods=['GET'])
def get_factorial(n):
    n_factorial = factorial(n)
    if n_factorial is None:
        return jsonify(error="Error: El número no puede ser negativo"),
    else:
        return jsonify(number=n, factorial=n_factorial)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
