#!/usr/bin/env python

import sys, getopt, json

def querydo( jsondata ):
    retVal = {}
    retVal["biblio"] = jsondata.get("biblio", "").encode("utf-8")
    retVal["title"] = jsondata.get("title", "").encode("utf-8")
    retVal["creator"] = jsondata.get("creator", "").encode("utf-8")
    retVal["publicationDate"] = jsondata.get("publicationDate","").encode("utf-8")
    retVal["holdingBranch"] = jsondata.get("holdingBranch","").encode("utf-8")
    retVal["callNumber"] = jsondata.get("callNumber", "").encode("utf-8")
    retVal["barcode"] = jsondata.get("barcode")
    retVal["copyNumber"] = jsondata.get("copyNumber", "").encode("utf-8")
    return retVal

def formatdymoxml(data):
    with open ("template/standard.xml", "r") as templateFile:
        template=templateFile.read()

    print template.format(data.get("biblio", ""), data.get("title", ""), data.get("creator", ""), data.get("publicationDate", ""),data.get("holdingBranch", ""),data.get("callNumber", ""),data.get("barcode"),data.get("copyNumber", ""))

def convert( obj ):
    myJson = json.loads(obj)
    if (type(myJson) == list):
        for obj in myJson:
            formatdymoxml(querydo(obj))
    else:
        formatdymoxml(querydo(myJson))

def main( argv ):

    data = {}

    try: opts, args = getopt.getopt(argv, "hi:",["help=","input="])

    except getopt.GetoptError:
        print 'failed to assign values'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'dymoxmlconv -i <json> | dymoxmlconv --input <json>'
            sys.exit()
        elif opt in ("-i", "--input"):
            data = convert(arg)

if __name__ == "__main__":
   main(sys.argv[1:])

