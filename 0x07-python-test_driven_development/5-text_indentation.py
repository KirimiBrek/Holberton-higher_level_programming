Skip to content
lroudge
/
holbertonschool-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
holbertonschool-higher_level_programming/0x07-python-test_driven_development/5-text_indentation.py
@lroudge
lroudge Change task 4 for a more pythonic code + add tests
 1 contributor
Executable File  20 lines (15 sloc)  472 Bytes
#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
