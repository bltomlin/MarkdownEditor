import sys

def header():
    """
	formats header 
	:return: formatted header
	"""
    print("Level: ")
    level = int(input())
    while level != None:
        if 0 < level <= 6:
            break
        else:
            print("The level should be within the range of 1 to 6")
            level = int(input())
    level = level * "#"
    print("Text: ")
    text = input()
    return " ".join([level, text]) + "\n"
    
def plain():
    """
	writes plain text
	:return: string
	"""
    print("Text:", end=" ")
    return input()

def bold():
    """
	formats bold text
	:return: formatted bold string
	"""
    print("Text:", end=" ")
    return "".join(["**", input(), "**"])

def italic():
    """
	formats italic text 
	:return: formatted italic string
	"""
    print("Text:", end=" ")
    return "".join(["*", input(), "*"])

def inline_code():
    """
	formats code 
	:return: formatted code
	"""
    print("Text:", end=" ")
    return "".join(["`", input(), "`"])

def new_line():
    """
	formats new line
	:return: new line
	"""
    return "\n"

def link():
    """
	formats a url link
	:return: formatted link
	"""
    print("Label:", end=" ")
    label = ''.join(["[", input(), "]"])
    print("URL: ", end=" ")
    url = ''.join(["(", input(), ")"])
    return ''.join([label, url])

def get_formatter():
    formatter = input()
    while formatter not in formatter_list:
        if formatter == "!help":
            print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
            print("Special commands: !help !done")
            print("Choose a formatter:", end=" ")
            formatter = input()
        elif formatter == "!done":
            sys.exit()
        elif formatter not in formatter_list:
            print("Unknown formatting type or command")
            print("Choose a formatter:", end=" ")
            formatter = input()
        else:
            print("Choose a formatter:", end=" ")
            formatter = input()
    return formatter

formatter_list = {"plain" : plain, "bold" : bold, "italic" : italic, "header" : header, "link" : link,
    "inline-code" : inline_code, "new-line" : new_line}

final_string = ''

while True:
    print("Choose a formatter:", end=" ")
    formatter = get_formatter()
    final_string += formatter_list[formatter]()
    print(final_string)
