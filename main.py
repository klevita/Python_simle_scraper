import requests
from bs4 import BeautifulSoup
   
defaultUrl = 'https://habr.com'

def createFile(name, content):
    print('Записываю файл - ' + name)
    print(content)
    with open(name + '.html', "w", encoding="utf-8") as text_file:
        text_file.write(content)

headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

session = requests.session()
nextPageHref = "/ru/search/page5/?q=микро+фронтенд&target_type=posts&order=date"

while(nextPageHref):
    url = defaultUrl + nextPageHref
    response = session.get(url, headers=headers)
    
    if response.status_code == 200:
        print('Перехожу на страницу - ' + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = soup.findAll('a', class_='tm-title__link', href=True)
        nextPageLink = soup.find('a', {'data-test-id': 'pagination-next-page'}, href=True)

        if(nextPageLink):
            nextPageHref = nextPageLink['href']
        else:
            nextPageHref = 0

        for a in links:
            title = a.text
            href = a['href']


            if title:
                
                contents = session.get(defaultUrl + a['href'], headers=headers).text
                if len(contents):
                    createFile(title[0: 30], contents)
    else:
        nextPageHref = 0
        print(response.status_code)