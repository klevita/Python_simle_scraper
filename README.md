# Python_simle_scraper
# Запуск

<p> `` pip3 install requests ``</p>
<p>  ``pip3 install beautifulsoup4 ``</p>
 <p> ``python main.py ``</p>

# Как работает
<p> В переменную nextPageHref необходимо записать ссылку первой страницы поиска в habr вырезав из начала 'https://habr.com'. </p>
<p> На каждый article парсер создаст html файл в папке из которой был запущен парсер, также парсер умеет переходить на следующую страницу поиска чтобы вытащить прям все статьи </p>
