from flask import Flask, render_template, request
import subprocess
from subprocess import Popen, PIPE
app = Flask(__name__)


@app.route('/')
def add():
    return render_template('add.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      data = request.form
      inputlist = data.values()
      inputdata = ''.join(inputlist)
      print inputdata
      cmd = ['java', 'Addition', inputdata]
      print cmd
      process = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE)
      stdout, stderr = process.communicate()
      result = stdout 
      return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)