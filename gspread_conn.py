from __future__ import print_function
import gspread

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1w-8QWAwsZvdHZopO2lzTMkWCFnmhtSj7kvtNnOFpkPY'
SAMPLE_RANGE_NAME = 'Hoja 1!A1:B100'

def searchIngredients(id):
    gc = gspread.oauth(credentials_filename='/home/administrador/credentials.json')
    sheet = gc.open_by_key(SAMPLE_SPREADSHEET_ID).sheet1
    code = sheet.find(id, in_column=0)
    try:
        ingredients = sheet.cell(code.row,2).value
        return ingredients
    except Exception:
        return "El codigo no existe"



if __name__ == "__main__":
    print(searchIngredients("4"))
