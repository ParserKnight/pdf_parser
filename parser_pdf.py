from PyPDF2 import PdfFileReader
import re
import requests
import wget
import time

def parse_pdf():
    links = list() 

    with open('Springer Ebooks.pdf', 'rb') as f:
        pdf = PdfFileReader(f)

        for pageNum in range(0,pdf.numPages):
            pageObj = pdf.getPage(pageNum)
            text = str(pageObj.extractText().encode('utf-8'))
            links.extend(re.findall(r'\\nhttp://(.+?)\\n.',text))

    for element in links:
        link = 'http://'+element
        r = requests.get(link)
        link_de_descarga=re.findall(r'/content/pdf(.+?).pdf',str(r.content))[0]
        nombre_del_libro = re.findall(r'<h1>(.+?)</h1>',str(r.content))[0]
        print(nombre_del_libro+"\n")
        link_de_descarga_completo = 'https://link.springer.com/content/pdf' + link_de_descarga + '.pdf'
        wget.download(link_de_descarga_completo, 'libros/'+nombre_del_libro+'.pdf')
        print("\n")
        time.sleep(5)

if __name__=="__main__":
    parse_pdf()