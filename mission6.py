import pickle
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/channel.html'
p_obj = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for i in p_obj:
    line = ""
    for content, num in i:
        line = line + content*num
    print(line)
