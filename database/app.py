from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

@app.route('/')
def index():
    data = Data.query.all()
    return render_template('upload.html', data=data)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        data = pd.read_csv(file)
        for index, row in data.iterrows():
            entry = Data(name=row['name'])
            db.session.add(entry)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
