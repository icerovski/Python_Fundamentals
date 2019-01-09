# 1. Blank Receipt

def print_dashes():
    print('------------------------------')

def print_head():
    print('CASH RECEIPT')
    print_dashes()

def print_body():
    print('Charged to____________________')
    print('Received by___________________')

def print_footer():
    print_dashes()
    print('\u00A9 SoftUni')

def print_book():
    print_head()
    print_body()
    print_footer()

print_book()