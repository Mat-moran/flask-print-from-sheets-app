import os
import json
import zpl
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from gspread_conn import searchIngredients 


class RegistrationForm(FlaskForm):
    code = StringField('Codigo del perfume')
    submit = SubmitField('Imprimir')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lasjfldsjidjlfsajdjfa'

def reformatText(text, chars_per_line, label_object):
    textBuffer = ''
    chars = 0
    for l in text:
        if chars < chars_per_line:
            textBuffer = textBuffer + l
        else:
            label_object.write_text(textBuffer, char_height=1, char_width=1, line_width=40, justification='L')
            chars = 0
            textBuffer = ''


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = RegistrationForm()
    if form.validate_on_submit():

        ing = searchIngredients(form.code.data)
        # myList = iter(item for item in db if item["id"] == form.code.data)
        # result = next(myList, {"id":"error", "ing":["error"]})
        # text = ', '.join(result['ing'])
        # print(text)
        print(ing)
        l = zpl.Label(25,40)
        height = 2
        l.origin(0,2)
        # l.write_text(ing, char_height=1, char_width=1, line_width=40, justification='L')
        reformatText(text=ing, chars_per_line=10, label_object=l)
        l.endorigin()
        zpl_text = l.dumpZPL()
        # l.preview()

        with open('file_to_print.txt', 'w') as file:
            file.write(zpl_text)

        os.system('lpr -P ZTC-GK420t file_to_print.txt')



    return render_template('form.html', title='form', form=form)

if __name__ == "__main__":
    app.run(debug=True)
