from flask import Flask, render_template, request
from flask_cors import CORS
from models import *

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        create_feedback(name, email, subject, message)
    data = read_feedback()
    return render_template('feedback.html', data=data)



@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    # id = request.form.get('id')
    # print(id)
    delete_feedback(id)
    data = read_feedback()
    return render_template('feedback.html', data=data)


@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    if request.method == 'GET':
        data = get_feedback_by_id(id)
        return render_template('edit.html', data=data)
    if request.method == 'POST':
        delete_feedback(id)
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        update_feedback(name, email, subject, message)
    data = read_feedback()
    return render_template('feedback.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
