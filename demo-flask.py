from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
   return render_template('index.html')


@app.route('/', methods=['POST'])
def signUp():
    print("name is")
    # read the posted values from the UI
    _name = request.form['inputName']

    print(_name)



if __name__ == '__main__':
    app.run()
