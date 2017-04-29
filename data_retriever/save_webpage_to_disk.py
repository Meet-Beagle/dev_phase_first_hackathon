from urllib.request import Request, urlopen

# path1 = '42.974049,-81.205203|42.974298,-81.195755'
request=Request('http://www.embo.org/events/events-calendar')
response = urlopen(request)
pagecontent = response.read().decode('utf-8')

with open('data_retriever/mock_webpage.html', mode='w') as file:
    file.write(pagecontent)