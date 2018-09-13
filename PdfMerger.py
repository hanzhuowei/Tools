# coding: utf-8
import os,sys
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

l_filepath = []
MergeName = "merged.pdf"


def Pdf_merger(files2merge, outputfile):
    merger = PdfFileMerger()
    output = file(outputfile, 'wb')
    for item_pdf in files2merge:
        merger.append(open(item_pdf, 'rb'))
    merger.write(output)


# Main funtion
if __name__ == '__main__':
    pathParser = argparse.ArgumentParser(description="the pdf merger")
    pathParser.add_argument("-p", required=True, help="give the path of the pdfs")
    pathParser.add_argument("--outfile", help='the file name of the merged pdf')
    path = pathParser.parse_args()

    try:
        if os.path.isdir(path.p):
            try: # the mounted WinShare has no write permission from python,
            # store the merged pdf to localself.
            # TBD
                # outputfile = path.outfile
                # outputfile = os.path.join(path.p, outputfile)
                # outputfile = os.path.join(path.p, MergeName)
                outputfile = MergeName
            except:
                print Error
            for each_file in os.listdir(path.p):
                abs_filepath = os.path.join(path.p, each_file)
                # print abs_filepath
                if os.path.isfile(abs_filepath):
                    if ".pdf" in abs_filepath:
                        l_filepath.append(abs_filepath)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    print ("Parsing PDF files finished, Start merging below files: \n")
    print ('\n'.join(l_filepath))

    if l_filepath:
        Pdf_merger(l_filepath, outputfile)
    print ("--------------------------")
    print ("--------------------------")
    print ("Merged to: \n" + outputfile)
