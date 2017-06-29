import sys

# Read command line arguments
progName, fileInName, fileOutName = sys.argv

# Open the input & output files
fileIn = open(fileInName, 'r')
fileOut = open(fileOutName, 'w')

# Remove all newlines & tabs from the input as a safety measure
css = fileIn.read().replace('\n', '').replace('\t', '')

length = len(css)
for pos in range(0, length):
    ### Character processing ###
    # Commas and colons
    if css[pos] == ',' or css[pos] == ':':
        prevChar = ''
        nextChar = ' '
    # Opening curly brackets
    elif css[pos] == '{':
        prevChar = ' '
        nextChar = '\n'
    # Semicolons
    elif css[pos] == ';':
        prevChar = ''
        nextChar = '\n'
    # Closing curly brackets
    elif css[pos] == '}':
        prevChar = '\n'
        nextChar = '\n\n'
    # Everyting else
    else:
        nextChar = ''
        prevChar = ''

    # Write the current character(s) to the output file
    fileOut.write("%s%s%s" % (prevChar, css[pos], nextChar))

fileIn.close()
fileOut.close()
