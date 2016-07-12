#!/usr/bin/env python
# encoding=iso-8859-1

import sys, getopt, json
reload(sys)
sys.setdefaultencoding('iso-8859-1')

def querydo( jsondata ):
    retVal = {}
    retVal["biblio"] = jsondata.get("biblio", "")
    retVal["title"] = jsondata.get("title", "")
    retVal["creator"] = jsondata.get("creator", "")
    retVal["publicationDate"] = jsondata.get("publicationDate","")
    retVal["holdingBranch"] = jsondata.get("holdingBranch","")
    retVal["callNumber"] = jsondata.get("callNumber", "")
    retVal["barcode"] = jsondata.get("barcode")
    retVal["copyNumber"] = jsondata.get("copyNumber", "")
    return retVal

def formatdymoxml():
    with open ("template/standard.xml", "r") as templateFile:
        return templateFile.read()

def formatpostscript():
    with open ("template/standard.ps", "r") as templateFile:
        return templateFile.read()

def getpostscrptpreamble():
    with open ("template/PS_preamble.ps", "r") as preamble:
        return preamble.read()

def format( data, type ):

    if (type == "xml"):
        template = formatdymoxml()
    elif (type == "PostScript"):
        template = formatpostscript()

    print template.format(data.get("biblio", ""), 
        data.get("title", ""), 
        data.get("creator", ""), 
        data.get("publicationDate", ""),
        data.get("holdingBranch", ""),
        data.get("callNumber", ""),
        data.get("barcode"),
        data.get("copyNumber", ""))

def convert( data, target ):
    myJson = json.loads(data)
    if (type(myJson) == list):
        for obj in myJson:
            format(querydo(obj), target)
    else:
        format(querydo(myJson), target)

def main( argv ):

    data = {}
    output = "xml"

    try: opts, args = getopt.getopt(argv, "hi:o:",["help=","input=","output="])

    except getopt.GetoptError:
        print 'failed to assign values'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'dymoxmlconv -i <json> | dymoxmlconv --input <json>'
            sys.exit()
        elif opt in ("-i", "--input"):
            data = arg
        elif opt in ("-o", "--output"):
            output = arg

    return convert(data, output)

if __name__ == "__main__":
   main(sys.argv[1:])

