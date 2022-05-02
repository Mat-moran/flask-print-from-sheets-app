import os
import json
import zpl
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from gspread_conn import searchIngredients2


class RegistrationForm(FlaskForm):
    code = StringField('Codigo del perfume')
    submit = SubmitField('Imprimir')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lasjfldsjidjlfsajdjfa'


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = RegistrationForm()
    print("FORM VALIDATE: ", form.validate_on_submit())
    if form.validate_on_submit():

        try:
            id, ing, lote = searchIngredients2(form.code.data)
            print(id, ing, lote)
            txt = """
    ^XA
    ^FX Seccion cabecera
    ^FO10,10
    ^A0N,10,10
    ^FB405,3,0,L,0
    ^FDEAU DE PARFUM - AGUA DE PERFUME. EVITAR LA EXPOSICION DIRECTA DE ESTE PRODUCTO AL SOL. USO TOPICO. EVITAR EL CONTACTO CON OJOS Y MUCOSAS.^FS

    ^FX Seccion lote
    ^FO8,35
    ^A0N,15,15
    ^FB350,11,0,L,0
    ^FDREF: {0}     CANT: 100ML      Lote: {1}^FS

    ^FX Seccion ingredientes
    ^FO8,55
    ^A0N,12,12
    ^FB405,11,0,L,0
    ^FD{2}^FS

    ^FX Seccion del nombre de empresa y telefono
    ^FO8,170
    ^A0N,13,13
    ^FB405,11,0,L,0
    ^FDINTENSO FRAGANCIAS.   TLF: 633759203^FS
    ^FO10,185
    ^A0N,13,13
    ^FB405,11,0,L,0
    ^FDC. HOYO 11.   TORREMOLINOS^FS

    ^FX Seccion de las imagenes
    ^FX Fourth section (the two boxes on the bottom).
    ^FO230,150^GFA,288,288,6,,:K01,K03,K06,K0E,:J01E,:::J03F01,J01F03,J01F87,I019F8F,I019FCF,I01DFEF,I01CIF,:I01CIF8,I03DF7F8,I03FF7FC,I07FF3FC,:I0FFE3FC,I0FF63FC,I0FF46FE,I0FE04FC,:I0FE00FC,I07C0078,I03C0078,I01C007,J0E00C,J03,,:I02,01068I044,01048I044,01269126648,01562AEI54,01508A81554,0150AA87558,0150AA8155,01503A8661C,,:
    ^FO280,150^GFA,288,288,6,,L0E,K01F,:K01F8,:K01F,:I0E004,I07FFC,J0IFC,J03FFE,K07FE,001DC1FE,0017E0FF,002020FF,0020407F8,0040C07F8,0047007FC,0039003FC,L03FC,07IFC1,07IFC3FC,0324D83FE,0324C83FE,03IF83FE,0326D83FE,0124D83FE,01IF83FE,:0124987FE,01B4D07FE,01IF07DE,01B6D07DE,01B49079E,00B69079E,00IF078E,00B6F070E,00949070E,009690706,00IF0606,:00D6B0406,0056B0402,0052B0C02,007FF0C02,007FE08,,^FS
    ^FO330,150^GFA,270,270,6,N06,M03F,M0ED8,L03988,L0E608,K018C1,K06306,J018E0C,J071838,J0C606,I031C1C,I0E703,0018C0C,0063038,00CC06,033018,06C07,0F01C,1C07,181C,087,07C,06,I01JFE,001F8I0FC,007L07,00CL018,00FCJ03F8,008LF88,008M08,:::0080E318808,00803419808,0080671F808,0080651E808,00801598808,0080E718808,008M08,:00CM08,007L03,003F8I0FE,I03JFE,^FS
    ^XZ
    """.format(form.code.data, lote, ing)
            with open('file_to_print.txt', 'w') as file:
                # file.write(zpl_text)
                file.write(txt)

            os.system('lpr -P ZTC-GK420t file_to_print.txt')
        except Exception as e:
            print(e)
            pass



    return render_template('form.html', title='form', form=form)

if __name__ == "__main__":
    app.run(debug=True)
