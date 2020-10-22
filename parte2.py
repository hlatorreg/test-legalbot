import pdfplumber
import re
import os

"""
Lee el archivo con pdfplumber
(no convierte a imagen)
"""
def _read(path:str):
    return pdfplumber.open(path)

"""
Limpia el texto de saltos de linea
en caso de ser necesario
"""
def _clean(text:str):
    return re.sub(r"\n", '', text)

"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
    pdf = _read(pdf_path)
    for page in pdf.pages:
        print(page.extract_text())

dir_a = './sociedades-pdf'
for filename in os.listdir(dir_a):
    print('--------------------- start of text ---------------------')
    pdf_to_text(f"{dir_a}/{filename}")
    print('---------------------- end of text ----------------------')

dir_b = './sociedades-b-pdf'
for filename in os.listdir(dir_b):
    print('--------------------- start of text ---------------------')
    pdf_to_text(f"{dir_b}/{filename}")
    print('---------------------- end of text ----------------------')