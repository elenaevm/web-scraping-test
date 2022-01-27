import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://contrataciondelestado.es/wps/portal/plataforma')
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href'))
    print('Contenido:', tag.contents)
    print('Atributos:', tag.attrs)
    print('\n')

tags