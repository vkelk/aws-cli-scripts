import logging
import os
import re


def expand_variables(string: str) -> str:
    """
    Replace all instances of variables with their ENVIRONMENT VARIABLES values.

    This method will search a string for all variables designated by the
    '$' prefix and replace it with values from the list.

    string[in]     String to search

    Returns string - string with variables replaced
    """
    finds = re.findall(r'\$(\w+)', string)
    for variable in finds:
        try:
            string = string.replace('$' + variable, str(os.environ[variable]))
        except KeyError:
            logging.warning(f"Variable {variable} not found")
    return string 


if __name__ == "__main__":
    text = """
    This a string for testing env variables expanding.
    The os variable is $os, and the temporary folder is $tmp.
    Testing some $nonexisting variables using the $ sign such as $40 and 40$
    Using some nonspaced items: $homedrive$homepath
    Quotes: '$homedrive$homepath'
    Double-quotes: "$homedrive$homepath"
    """

    print(expand_variables(text))
