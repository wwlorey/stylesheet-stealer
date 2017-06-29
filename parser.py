import sys
import os.path

# Read command line arguments
if len(sys.argv) == 3:
    fileInName = sys.argv[1]
    fileOutName = sys.argv[2]
else:
    # Default to the following files if the wrong number of arguments
    # is passed
    fileInName = 'unformatted.css'
    fileOutName = 'formatted.css'

# Open the input & output files
# Check to make sure the input file exists
if(os.path.isfile(fileInName)):
    fileIn = open(fileInName, 'r')
else:
    print("\nPlease include the input file as a parameter. See the readme for detials\n")

    # End the program
    sys.exit()

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

# The program is finished
print("\nDone!\n")
