from flask import Flask,render_template
import subprocess
from subprocess import PIPE
import re

app = Flask(__name__)

@app.route('/')
def index():
    lines_inner = []
    proc = subprocess.run("algia tl -n 100", shell=True, stdout=PIPE, stderr=PIPE, text=True, encoding="utf-8")
    cmd_out = proc.stdout
    cmdout_lines = cmd_out.split("\n")
    for line in cmdout_lines:
        if re.match(r'.+:\s[0-9a-z]+$', line) != None:
            lines_inner.append([True,line])
        else:
            lines_inner.append([False,line])
        
    return render_template('index.html', lines=lines_inner)

app.run(host='0.0.0.0', port=8080, debug=False)

    
