from flask import Flask, request
import subprocess
import os
app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def api():
	if request.form.get('command'):
		proc = subprocess.Popen(request.form.get('command'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
		proc.wait()
		str_stdout = proc.stdout.read().decode()
		str_stderr = proc.stderr.read().decode()
		return {"std":str_stdout, "err":str_stderr}
	else:
		return ''
		
@app.route("/", methods=["GET"])
def index():
	with open("index.html","r") as f:
		html = f.read()
	return html

@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ
    
if __name__ == "__main__":
	app.run("0.0.0.0", 1235, debug=True)
