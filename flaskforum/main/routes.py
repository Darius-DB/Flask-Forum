from flask import render_template, request
from flaskforum import app
from flaskforum.models import Question


@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    questions = Question.query.order_by(
        Question.date_added.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', questions=questions)


@app.route('/about')
def about():
    return render_template('about.html', title='About')