import sys
import os.path

# Read command line arguments
if len(sys.argv) == 3: # All expected arguments are present
    fileInName = sys.argv[1]
    fileOutName = sys.argv[2]
elif len(sys.argv) == 2: # No output file was given
    fileInName = sys.argv[1]

    # Defult to a standard output file
    fileOutName = 'formatted.css'
else: # Neither input or output file was given, or something else weird happened
    # Default to standard input/output files
    fileInName = 'unformatted.css'
    fileOutName = 'formatted.css'


# Open the input & output files
# Check to make sure the input file exists
if(os.path.isfile(fileInName)):
    fileIn = open(fileInName, 'r')
else:
    print("\nPlease see the readme for instructions on command line arguments.\n")

    # End the program
    sys.exit()

fileOut = open(fileOutName, 'w')


# Remove all newlines & tabs from the input string
cssText = fileIn.read().replace('\n', '').replace('\t', '')


# Iterate through the input file string and output formatted CSS to the output file
textLength = len(cssText)
for i in range(0, textLength):
    # Get the current char and next char in the input file string
    char = cssText[i]
    if i + 1 >= textLength:
        nextInputChar = None
    else:
        nextInputChar = cssText[i + 1]

    # Process characters

    # Commas and colons
    if char == ',' or char == ':':
        prevOutputChar = ''
        nextOutputChar = ' '

    # Opening curly brackets
    elif char == '{':
        prevOutputChar = ' '
        nextOutputChar = '\n'

    # Semicolons
    elif char == ';':
        prevOutputChar = ''
        nextOutputChar = '\n'

    # Closing curly brackets
    elif char == '}':
        if nextInputChar == '}':
            prevOutputChar = '\n'
        else:
            prevOutputChar = '\n'
            nextOutputChar = '\n\n'

    # Everyting else
    else:
        nextOutputChar = ''
        prevOutputChar = ''

    # Write the current character(s) to the output file
    fileOut.write("%s%s%s" % (prevOutputChar, char, nextOutputChar))


fileIn.close()
fileOut.close()


# The program is finished
print("\nDone!\n")
