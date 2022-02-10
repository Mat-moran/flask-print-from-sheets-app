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


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = RegistrationForm()
    if form.validate_on_submit():

        ing, lote = searchIngredients(form.code.data)
        # myList = iter(item for item in db if item["id"] == form.code.data)
        # result = next(myList, {"id":"error", "ing":["error"]})
        # text = ', '.join(result['ing'])
        # print(text)
        text = "INGREDIENTES: " + ing + " LOTE: " + lote 
        print("Ingredientes", ing)
        print("Lote", lote)
        l = zpl.Label(25,40)
        height = 2
        l.origin(0,2)
        l.write_text(text, char_height=1, char_width=1, line_width=28, justification='L', max_line=11)
        
        zpl_text = l.dumpZPL()
        # l.preview()
        # zpl_text = reformatText(text=ing, chars_per_line=60, label_object=l)

        print(zpl_text)
        txt = """
^XA
^FX Seccion cabecera
^FO1,10
^A0N,10,10
^FB405,3,0,L,0
^FDEAU DE PARFUM - AGUA DE PERFUME. EVITAR LA EXPOSICION DIRECTA DE ESTE PRODUCTO AL SOL. USO TOPICO. EVITAR EL CONTACTO CON OJOS Y MUCOSAS.^FS

^FX Seccion lote
^FO1,35
^A0N,15,15
^FB350,11,0,L,0
^FDREF: 1035     CANT: 100ML      Lote: B257 15-08-2021^FS

^FX Seccion ingredientes
^FO1,60
^A0N,12,12
^FB405,11,0,L,0
^FDALCOHOL DENAT, PARFUM (FRAGRANCE), AQUA (WATER), ETHYLHEXYL METHOXYCINNAMATE, BUTYL METHOXYDIBENZOYLMETHANE, ETHYLHEXYL SALICYLATE, LIMONENE, HEXYL  CINNAMAL, EUGENOL, CITRONELLOL, BENZYL  BENZOATE, LINALOOL, GERANIOL, COUMARIN, BHT, EVERNIA FURFURACEA (TREE MOSS) EXTRACT, BUTYLPHENYL METHYLPROPIONAL, CINNAMYL ALCOHOL, ALPHA-ISOMETHYL IONONE, BENZYL  ALCOHOL, ISOEUGENOL, CITRAL, BENZYL CINNAMATE, BENZYL  SALICYLATE, FARNESOL, AMYL CINNAMAL, CINNAMAL, CI19140, CI 42051-47005, CI 16035^FS

^FX Seccion del nombre de empresa y telefono
^FO1,170
^A0N,13,13
^FB405,11,0,L,0
^FDINTENSO FRAGANCIAS.   TLF: 633759203^FS
^FO1,185
^A0N,13,13
^FB405,11,0,L,0
^FDC/HOYO 11.   TORREMOLINOS^FS

^FX Seccion de las imagenes
^FX Fourth section (the two boxes on the bottom).
^FO230,150^GB50,50,3^FS
^FO280,150^GB50,50,3^FS
^FO330,150^GB50,50,3^FS
^XZ

"""
        with open('file_to_print.txt', 'w') as file:
            # file.write(zpl_text)
            file.write(txt)

        os.system('lpr -P ZTC-GK420t file_to_print.txt')



    return render_template('form.html', title='form', form=form)

if __name__ == "__main__":
    app.run(debug=True)
