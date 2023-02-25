from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/sub', methods=['post'])
def post():
    try:
        post_data = request.get_json()
        post_text = post_data["tweet"]
    except Exception as e:
        app.logger.debug("exeption!")
        return ""

    subprocess.run(["algia","n", post_text], text=True, encoding="utf-8")
    return ""

app.run(host='0.0.0.0', port=10000, debug=False)

    
