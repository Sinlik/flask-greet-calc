from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/<oper>")
@app.route("/math/<oper>")
def do_math(oper):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[oper](a, b)
    return str(result)

if __name__ == '__main__':
    app.run()