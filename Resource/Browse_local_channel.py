from .base import *

# 浏览本地频道
def browse_local_channel(session, channel_id):
    channel_url = f"https://www.xuexi.cn/channel/{channel_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(channel_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="article")
    for article in articles:
        print(article.text)
