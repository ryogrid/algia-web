from flask import Flask, render_template, request, Markup
import subprocess
from subprocess import PIPE
import re
from shlex import quote
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
        lines_inner = []
        proc = subprocess.run("algia tl -n 100", shell=True, stdout=PIPE, stderr=PIPE, text=True, encoding="utf-8")
        cmd_out = proc.stdout
        cmdout_lines = cmd_out.split("\n")
        for line in cmdout_lines:
            if re.match(r'.+:\s[0-9a-z]+$', line) != None:
                lines_inner.append([1,line.split(":")[0]])
            else:
                pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
                found_url_match = re.search(pattern, line)
                #line_escaped = str(escape(line))
                #for url in url_list:
                #line_url_replaced = line_escaped
                if not found_url_match:
                    lines_inner.append([2,line])
                else:
                    found_url = found_url_match.group(0)
                    #line_url_replaced = line_escaped.replace(found_url, "<a href=\"" + escape(found_url) + "\">" + escape(found_url) + "</a>")
                    lines_inner.append([3,line,escape(found_url)])
                    app.logger.debug(line)
                
        
        return render_template('index.html', lines=lines_inner)
            

@app.route('/sub', methods=['post','get'])
def post():
    try:
        app.logger.debug(request.args)
        #post_text = request.form["note"]
        req = request.args
        post_text = req.get("note")
        post_text = post_text.replace("'","")
        #post_data = request.get_json()
        app.logger.debug(type(post_text))
        app.logger.debug(post_text)
    except Exception as e:
        app.logger.debug("exeption!")
        pass

    #post_text = quote(escape(post_text))
    post_text = escape(post_text)
    #subprocess.run("algia n " + "'" + post_text + "'", shell=True, stdout=PIPE, stderr=PIPE, text=True, encoding="utf-8")
    subprocess.run(["algia","n", post_text], text=True, encoding="utf-8")
    return index()

app.run(host='0.0.0.0', port=8080, debug=True)

    
