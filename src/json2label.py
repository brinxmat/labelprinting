#encoding: utf-8

"This module parses the json and calls the template-mapping module"

import sys, getopt, json, dymoxmlconverter

def querydo( jsondata ):
    "Creates the XML"
    biblio = jsondata["biblio"]
    title = jsondata["title"]
    creator = jsondata["creator"]
    publicationDate = jsondata["publicationDate"]
    holdingBranch = jsondata["holdingBranch"]
    callNumber = jsondata["callNumber"]
    barcode = jsondata["barcode"]
    copyNumber = jsondata["copyNumber"]
    
    print biblio.encode("utf-8"), title.encode("utf-8"), creator.encode("utf-8"), publicationDate.encode("utf-8"), holdingBranch.encode("utf-8"), callNumber.encode("utf-8"), barcode.encode("utf-8"), copyNumber.encode("utf-8")
    
myJson = json.loads(jsonstr)
if (type(myJson) == list):
    for obj in myJson:
        querydo(obj)
else:
    querydo(myJson)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hi", ["help", "input"])
        except getopt.error, msg:
             raise Usage(msg)
        for o, a in opts:
            if o in ("-h", "--help"):
                Usage(null)
            elif o in ("-i", "--input"):
                with open ("template/standard.txt", "r") as templateFile:
                    template=templateFile.read()

       print template % (biblio,title,creator,publicationDate,holdingBranch,callNumber,barcode,copyNumber)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
