import re 

def is_valid(s):
    if (re.match(r'^[a-zA-Z0-9]{10}$',s) and re.search(r'[A-Z].*[A-Z]',s) 
        and re.search(r'\d.*\d.*\d',s ) and len(set(s))==len(s)):
        return True


for _ in range(int(input())):
    if is_valid(input()):
        print('Valid')
    else:
        print('Invalid')