#How many rows to display for textareas by default
TextAreaRows = 10

CharFieldMaxLength = 500
TextFieldMaxLength = 10000
ImportFieldMaxLines = 1000
'''Technically this number isn't quite big enough to let the user input a full
500 characters for all 1000 entries, because it also counts the line breaks 
as characters, but whatever'''
ImportFieldMaxLength = CharFieldMaxLength * ImportFieldMaxLines

max_length_error = "Too many characters: %(show_value)d/%(limit_value)d."