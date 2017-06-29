# stylesheet-stealer
A script for formatting `CSS` stylesheets found on the internet into a standard, readable form.

## Running the script
First off, make sure you are using `Python 3.0` or later to ensure everyting works properly.

The main script file is `parser.py`. To run it, use the command line as shown:

    py parser.py <input-file-name> <output-file-name>

Where `<input-file-name>` is an unformatted (or poorly formatted) `CSS` file and `<output-file-name>` is the file you want the program to generate. This output file will contain the formatted `CSS` code.

Optionally, you can omit the input and output file names and the program will automatically try and open `unformatted.css` as the input file and `formatted.css` as the output file. If it doesn't find the input file in the script's directory, the program will halt.
