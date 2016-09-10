from wilson import app
from flask import request, jsonify

@app.route('/status/<job>', methods=['GET'])
def showResults(job):
    return jsonify({"job": {"id": job, "response": 202, "status": "completed"}}), 200

