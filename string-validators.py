if __name__ == '__main__':
    s = input()
    def check(s, method):
        return any(getattr(c, method)() for c in s)
    print(check(s, 'isalnum'))
    print(check(s, 'isalpha'))
    print(check(s, 'isdigit'))
    print(check(s, 'islower'))
    print(check(s, 'isupper'))