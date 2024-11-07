# Python_simle_scraper
# Запуск
 ``
 pip3 install requests <br>
 pip3 install beautifulsoup4<br>
 python main.py
 ``
# Как работает
<p> В переменную nextPageHref необходимо записать ссылку первой страницы поиска в habr вырезав из начала 'https://habr.com'. </p>
<p> На каждый article парсер создаст html файл в папке из которой был запущен парсер, также парсер умеет переходить на следующую страницу поиска чтобы вытащить прям все статьи </p>
