import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45',
}

r = requests.get('https://ani.gamer.com.tw/', headers=headers)
if r.status_code == 200:
    print(f'success request：{r.status_code}')

    soup = BeautifulSoup(r.text, 'html.parser')
    newanime_item = soup.select_one('.timeline-ver > .newanime-block')
    anime_items = newanime_item.select('.newanime-date-area:not(.premium-block)')

    for anime_item in anime_items:
        anime_name = anime_item.select_one('.anime-name > p').text.strip()
        print(anime_name)
        anime_watch_number = anime_item.select_one('.anime-watch-number > p').text.strip()
        print(anime_watch_number)
        anime_episode = anime_item.select_one('.anime-episode').text.strip()
        print(anime_episode)
        anime_href = anime_item.select_one('a.anime-card-block').get('href')
        print('https://ani.gamer.com.tw/'+anime_href)

        print('----------')
else:
    print(f'fail request：{r.status_code}')
