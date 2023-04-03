from flask import Flask, jsonify, request, abort
from uuid import uuid4

app = Flask(__name__)

jobs = {}


@app.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify(list(jobs.values()))


@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    
    if 'job_name' not in data:
        abort(400)
    
    job_id = str(uuid4())
    job = {'id': job_id, 'job_name': data['job_name']}
    
    jobs[job_id] = job
    
    return jsonify(job), 201


@app.route('/jobs/<string:job_id>', methods=['GET'])
def get_job(job_id):
    if job_id not in jobs:
        abort(404)
    
    return jsonify(jobs[job_id])


@app.route('/jobs/<string:job_id>', methods=['PUT'])
def update_job(job_id):
    if job_id not in jobs:
        abort(404)

    data = request.get_json()
    
    if 'job_name' not in data:
        abort(400)
    
    jobs[job_id]['job_name'] = data['job_name']
    
    return jsonify(jobs[job_id])


@app.route('/jobs/<string:job_id>', methods=['DELETE'])
def delete_job(job_id):
    if job_id not in jobs:
        abort(404)
    
    del jobs[job_id]
    
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
