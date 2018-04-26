from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def whatsMyName():
  return render_template('index.html')  

@app.route('/process', methods=['POST']) 
def process():
    name = str(request.form['name'])
    submitName = str(request.form['submit-name'])
    print name
    return redirect('/')

app.run(debug=True) 