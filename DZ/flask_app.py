from flask import Flask
import generator

app = Flask('fibonacci sequences')

@app.route('/')
def index():
    return 'My cool fibonacci sequence flask app!'

@app.route('/<int:n>')
def get_sequence(n):
    return list(generator.fib(n))

@app.errorhandler(404)
def page_not_found(e):
    return 'Oops! Try to enter a number!'

if __name__ == '__main__':
    app.run(debug=True)