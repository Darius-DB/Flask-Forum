from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    title = StringField('Question Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    tag_1 = SelectField('Choose Category', choices=[
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('Ruby', 'Ruby'),
        ('Go', 'Go'),
        ('SQL', 'SQL'),
        ('Swift', 'Swift')
    ], validators=[DataRequired()])
    tag_2 = SelectField('Choose Category', choices=[
        ('Web Development', 'Web Development'),
        ('Software Development', 'Software Development'),
    ], validators=[DataRequired()])
    submit = SubmitField('Ask Question')
