import sys

print('Choose a formatter:', end = '')
formatter_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
user_input = input()
while user_input != None:
    if user_input == '!help':
        print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
        print('Choose a formatter:', end = '')
        user_input = input()
    elif user_input == '!done':
        sys.exit()
    elif user_input not in formatter_list:
        print('Unknown formatting type or command')
        print('Choose a formatter:', end = '')
        user_input = input()
    else:
        print('Choose a formatter:', end = '')
        user_input = input()
