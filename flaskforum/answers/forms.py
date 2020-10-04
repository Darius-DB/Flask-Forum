from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    content = TextAreaField('Add Your Answer', validators=[DataRequired()])
    submit = SubmitField('Answer')
