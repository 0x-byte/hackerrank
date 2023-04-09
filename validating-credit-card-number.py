import re

def is_valid(cc_number):
    return bool(re.match(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$', cc_number))


for _ in range(int(input())):
    if is_valid(input()):
        print('Valid')
    else:
        print('Invalid')
'''


def is_valid(cc_number):
    if not re.match(r'^[\d]{16}$|^([\d]{4}-){3}[\d]{4}$', cc_number):
        print(1)
        return False
    
    if re.match(r'(\d)(-?(\1)){3}', cc_number):
        print(2)
        return False
    
    if not re.match(r'^[456]', cc_number):
        print(3)
        return False
    
    
    return True

for _ in range(int(input())):
    if is_valid(input()):
        print('Valid')
    else:
        is_valid(input())

'''