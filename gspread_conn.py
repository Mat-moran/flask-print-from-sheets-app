from __future__ import print_function
from google.auth import credentials
import gspread
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1w-8QWAwsZvdHZopO2lzTMkWCFnmhtSj7kvtNnOFpkPY'
SAMPLE_RANGE_NAME = 'Hoja 1!A1:B100'

def searchIngredients(id):
    credentials ={}
    gc = gspread.service_account_from_dict(credentials)
    sheet = gc.open_by_key(SAMPLE_SPREADSHEET_ID).sheet1
    code = sheet.find(id, in_column=0)
    try:
        ingredients = sheet.cell(code.row,2).value
        lote = sheet.cell(code.row,3).value
        return ingredients, lote
    except Exception:
        return "El codigo no existe"


def searchIngredients2(id):
    df = pd.read_csv("database2.csv", sep=";")
    print(df)
    row = df.loc[df['CODIGO'] == int(id)]
    print(id)
    print('ROW: ',row.values[0])
    return row.values[0]


if __name__ == "__main__":
    print(searchIngredients("4"))
