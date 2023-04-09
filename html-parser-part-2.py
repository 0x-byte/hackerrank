from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print (">>> Multi-line Comment", data,sep='\n')
        else:
            print (">>> Single-line Comment", data,sep='\n')
    def handle_data(self, data):
        if data != '\n':
            print (">>> Data", data,sep='\n')

n = int(input())
html_code = ""
for i in range(n):
    html_code += input()+'\n'

parser = MyHTMLParser()
parser.feed(html_code)
