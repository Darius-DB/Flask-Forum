from flask import render_template, redirect, url_for, abort, request, flash
from flaskforum import app, db
from flask_login import current_user, login_required
from flaskforum.models import Question, Answer
from flaskforum.questions.forms import QuestionForm
from flaskforum.answers.forms import AnswerForm


@app.route('/question/new/', methods=['GET', 'POST'])
@login_required
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(
            title=form.title.data,
            content=form.content.data,
            tag_1=form.tag_1.data,
            tag_2=form.tag_2.data,
            author=current_user
        )
        db.session.add(question)
        db.session.commit()
        flash('Your question was added!', 'success')
        return redirect(url_for('home'))
    return render_template('add_question.html', form=form, title='Add Question')


@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    answers = Answer.query.filter_by(question_id=question.id).all()
    if form.validate_on_submit():
        answer = Answer(
            content=form.content.data,
            author=current_user,
            question_id=question.id
        )
        db.session.add(answer)
        db.session.commit()
        flash('Your answer was added!', 'success')
        return redirect(url_for('question', question_id=question.id))
    return render_template('question.html', question=question, title=question.title, form=form, answers=answers)


@app.route('/question/<int:question_id>/update', methods=['GET', 'POST'])
@login_required
def update_question(question_id):
    question = Question.query.get_or_404(question_id)
    if question.author != current_user:
        abort(403)
    form = QuestionForm()
    if form.validate_on_submit():
        question.title = form.title.data
        question.content = form.content.data
        question.tag_1 = form.tag_1.data
        question.tag_2 = form.tag_2.data
        db.session.commit()
        flash('Your question has been updated!', 'success')
        return redirect(url_for('question', question_id=question.id))
    elif request.method == 'GET':
        form.title.data = question.title
        form.content.data = question.content
        form.tag_1.data = question.tag_1
        form.tag_2.data = question.tag_2
    return render_template('add_question.html', title='Update Question', form=form)


@app.route('/question/<int:question_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    if question.author != current_user:
        abort(403)
    db.session.delete(question)
    db.session.commit()
    flash('Your question has been deleted!', 'success')
    return redirect(url_for('home'))
