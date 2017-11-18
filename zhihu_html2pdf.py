import os
import pdfkit

path = os.getcwd()
files= os.listdir(path)

for file in files:
    if file[-4:] == 'html':
        outname = file[:-5]+'.pdf'
        print(outname)
        pdfkit.from_file(file,outname)
