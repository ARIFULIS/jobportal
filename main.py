from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/job-board'
db = SQLAlchemy(app)
db.init_app(app)


class contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=('GET', 'POST'))
def contact():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = contacts(msg=message, name=name, email=email, phone=phone, date=datetime.now())
        db.session.add(entry) 
        db.session.commit()
    return render_template('contact.html')


@app.route("/job_list")
def job_list():
    return render_template('job_listing.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/blog_details")
def blog_details():
    return render_template('single-blog.html')


@app.route("/job_details")
def job_details():
    return render_template('job_details.html')


@app.route("/elements")
def elements():
    return render_template('elements.html')




if __name__ == '__main__':
    app.run(debug=True)