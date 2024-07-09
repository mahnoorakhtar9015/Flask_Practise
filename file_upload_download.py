from io import BytesIO
from flask import Flask, render_template, request, send_file

from flask_sqlalchemy import SQLAlchemy
import os



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'pdf_database.db')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method=='POST':
        file = request.files['file']
        upload=Upload(filename=file.filename  , data=file.read())
        db.session.add(upload)
        db.session.commit()
       
        return f'Uploaded {file.filename}'
    return render_template('file_upload.html')


@app.route('/download/<upload_id>')


def download_file(upload_id):
    upload=Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True )

if __name__ == "__main__":
    app.run(debug=True)
    
        
