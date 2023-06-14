from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome ():
    html = """
    <b> welcome </b>
    """
    return html

@app.route('/welcome/home')
def home ():
    html = """
    <b> welcome home </b>
    """
    return html

@app.route('/welcome/back')
def back ():
    html = """
    <b> welcome back </b>
    """
    return html

if __name__ == '__main__':
    app.run()