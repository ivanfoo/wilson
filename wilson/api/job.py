from wilson import app
from flask import request, jsonify

@app.route("/job", methods=['POST'])
def runPlaybook():
    data = request.get_json(silent=True)
    return jsonify(data), 202

