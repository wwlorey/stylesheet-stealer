import sys

progName, fileInName, fileOutName = sys.argv
fileIn = open(fileInName, 'r')
fileOut = open(fileOutName, 'w')

css = fileIn.read().replace('\n', '') #not super necessary thing to do
                                      #(remove '\n' instances) but is a good
                                      #safety measure
length = len(css)
for pos in range(0, length):
    ### character processing ###
    #commas and colons
    if css[pos] == ',' or css[pos] == ':':
        prevChar = ''
        nextChar = ' '
    #opening curly brackets
    elif css[pos] == '{':
        prevChar = ' '
        nextChar = '\n'
    #semicolons
    elif css[pos] == ';':
        prevChar = ''
        nextChar = '\n'
    #closing curly brackets
    elif css[pos] == '}':
        prevChar = '\n'
        nextChar = '\n\n'
    #everyting else
    else:
        nextChar = ''
        prevChar = ''

    fileOut.write("%s%s%s" % (prevChar, css[pos], nextChar))

fileIn.close()
fileOut.close()
