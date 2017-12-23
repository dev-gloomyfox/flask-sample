from flask import Flask, request, jsonify

from models import Sample

app = Flask(__name__)


@app.route('/<message>')
def url_sample(message):
    return jsonify(result=0, value=message)


@app.route('/get', methods=['GET'])
def get_sample():
    message = request.args.get('message')
    return jsonify(result=0, value=message)


@app.route('/post', methods=['POST'])
def post_sample():
    message = request.json['message']
    return jsonify(result=0, value=message)


@app.route('/file', methods=['POST'])
def file_sample():
    file = request.files['file']
    message = request.form['message']
    return jsonify(result=0, value=message, filename=file.filename)


@app.route('/object')
def object_sample():
    sample = Sample(0, 'Object Sample')
    return jsonify(sample.__dict__)


if __name__ == '__main__':
    app.run()