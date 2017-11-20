from html.parser import  HTMLParser
import  urllib.request

url = '''http://www.pythonchallenge.com/pc/def/equality.html'''
class MyHtmlParser(HTMLParser):
    ls_comments = list()
    def handle_comment(self, data):
        self.ls_comments.append(data)

parser = MyHtmlParser()
html_page = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
parser.feed(str(html_page.read()))
page_source_content = parser.ls_comments[1]
result = ''.join(i for i in page_source_content if (i.isalpha() and page_source_content.count(i) == 1))
print(result)


#method1:dict.get(key,param)
print('method1:')
occurrences = {}
content = page_source_content.strip()
for c in content:occurrences[c] = occurrences.get(c,0) + 1
avg = len(content)//len(occurrences)
print(''.join([c for c in occurrences if occurrences[c] < avg]))

#method2:
print('method2:')
import  collections
occurrences = collections.OrderedDict() #An OrderedDict is a dict that remembers the order that keys were first inserted
for c in content:occurrences[c] = occurrences.get(c, 0) + 1
avg = len(content)//len(occurrences)
print(''.join([c for c in occurrences if occurrences[c] < avg]))

#method3:
print('method3:')
import  string
res = list((filter(lambda x: x in string.ascii_letters and content.count(x) == 1, content)))
print (''.join(res))


