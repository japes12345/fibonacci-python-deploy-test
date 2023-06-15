from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/fibonacci/<int:n>')
def get_fibonacci(n):
    fib_seq = fibonacci(n)
    return jsonify(fib_seq)

if __name__ == '__main__':
    app.run()