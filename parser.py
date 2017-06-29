import sys
import os.path


# Returns an empty string if char is a space, returns space (' ') otherwise
def insertSpaceCheck(char):
    if char is ' ':
        return ''
    else:
        return ' '


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


# Stack (really a list being used as a stack) that keeps track of what curly
# braces have been encountered
braceStack = []

# Stack for parentheses
parenthStack = []

# Bool used in keeping track of whether an '@' has been seen in the current context
seenAtSymbol = False

# Bool used in formatting curly braces in media queries
insertTabBeforeBrace = False


# Iterate through the input file string and output formatted CSS to the output file
textLength = len(cssText)
for i in range(0, textLength):

    # Get the prev char, current char, and next char in the input file string
    char = cssText[i]

    if i + 1 >= textLength:
        nextInputChar = None
    else:
        nextInputChar = cssText[i + 1]

    if i - 1 < 0:
        prevInputChar = None
    else:
        prevInputChar = cssText[i - 1]


    nextOutputChar = ''
    prevOutputChar = ''


    # Process characters

    # @ symbol
    if char == '@':
        seenAtSymbol = True

    # Commas
    elif char == ',':
        nextOutputChar = insertSpaceCheck(nextInputChar)

    # Colons
    elif char == ':':
        # This block checks to see if the current char is within parenthesis OR
        # curly braces as well as in a media query (including some stipulations)
        # before inserting a space after the colon
        if len(parenthStack) > 0 or len(braceStack) > 0:
            if not seenAtSymbol: # Not currently in a media query
                nextOutputChar = insertSpaceCheck(nextInputChar)
            else: # Currently in the media query
                if len(braceStack) % 2 == 0: # The char is within attr. assignment in the media query
                    nextOutputChar = insertSpaceCheck(nextInputChar)

    # Opening parentheses
    elif char == '(':
        parenthStack.append(char)

    # Opening curly brackets
    elif char == '{':
        braceStack.append(char)

        # Check to see if the next line needs to be indented twice (it is in a media query
        # in the attribute assignment section)
        if seenAtSymbol and (len(braceStack) % 2 == 0):
            nextOutputChar = '\n\t\t'
        else:
            nextOutputChar = '\n\t'

        prevOutputChar = insertSpaceCheck(prevInputChar)

    # Semicolons
    elif char == ';':
        if nextInputChar != '}':
            if seenAtSymbol:
                nextOutputChar = '\n\t\t'
            else:
                nextOutputChar = '\n\t'
        else:
            # Tab the next ending brace if it's in a media query
            if seenAtSymbol:
                insertTabBeforeBrace = True

    # Closing parentheses
    elif char == ')':
        parenthStack.pop() # Remove the last parenthesis

    # Closing curly brackets
    elif char == '}':
        braceStack.pop() # Remove the last brace in the stack

        if insertTabBeforeBrace:
            prevOutputChar = '\n\t'
            insertTabBeforeBrace = False

            if not (nextInputChar == '}'):
                nextOutputChar = '\n\n\t'


        else:
            if nextInputChar == '}':
                prevOutputChar = '\n'
            else:
                prevOutputChar = '\n'
                nextOutputChar = '\n\n'

            if len(braceStack) == 0 and seenAtSymbol:
                # Clear the '@' flag
                seenAtSymbol = False

    # Endings of selector fields in media queries
    elif nextInputChar == '}' and seenAtSymbol and not (len(braceStack) == 1):
        insertTabBeforeBrace = True


    # Write the current character(s) to the output file
    fileOut.write("%s%s%s" % (prevOutputChar, char, nextOutputChar))


fileIn.close()
fileOut.close()


# The program is finished
print("\nDone!\n")
