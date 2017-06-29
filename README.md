# stylesheet-stealer
A script for formatting `CSS` stylesheets found on the internet into a standard, readable form.

## Running the script
First off, make sure you are using `Python 3.0` or later to ensure everyting works properly.

The main script file is `parser.py`. To run it, enter one of the following commands into the command prompt:

    py parser.py <input-file-name> <output-file-name>

OR

    py parser.py <input-file-name>

OR

    py parser.py

Where `<input-file-name>` is an unformatted (or poorly formatted) `CSS` file and `<output-file-name>` is the file you want the program to generate. This output file will contain the formatted `CSS` code.

**Note**:  As seen above, you may *omit* the output file name, or both the output file name and input file name. If both are omitted, the program attempts to open `unformatted.css` as the input file and `formatted.css` as the output file, ending the program if the input file is not found. If only the output file is omitted, the given input file is used, of course, as input and `formatted.css` is opened as the output file.
