from flask import abort, render_template, redirect, url_for, flash, request
from flaskforum import app, db
from flask_login import current_user, login_required
from flaskforum.models import Answer
from flaskforum.answers.forms import AnswerForm


@app.route('/edit_answer/<int:answer_id>', methods=['GET', 'POST'])
@login_required
def edit(answer_id):
    form = AnswerForm()
    answer = Answer.query.get_or_404(answer_id)
    if answer.author != current_user:
        abort(403)
    if form.validate_on_submit():
        answer.content = form.content.data
        db.session.commit()
        flash('Your answer was updated', 'succes')
        return redirect(url_for('edit', answer_id=answer.id))
    elif request.method == 'GET':
        form.content.data = answer.content
    return render_template('answer.html', title='Edit Answer', answer=answer, form=form)


@app.route('/answer/<int:answer_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if answer.author != current_user:
        abort(403)
    db.session.delete(answer)
    db.session.commit()
    flash('Your answer was deleted!', 'success')
    return redirect(url_for('home'))
