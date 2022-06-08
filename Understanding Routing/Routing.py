



from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def Dojo():
    return  "Dojo!"




@app.route('/Hi/<name>/<num>')
def hi (name,num):
    print(name)
    return  render_template('index.html',_name = name,_num = int(num))













if __name__=="__main__":
    app.run(debug=True)