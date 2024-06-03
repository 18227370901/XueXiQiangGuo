import requests
from bs4 import BeautifulSoup

# 登录学习强国
def login(username, password):
    login_url = "https://www.xuexi.cn/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
        "username": username,
        "password": password
    }
    session = requests.Session()
    response = session.post(login_url, headers=headers, data=data)
    return session

# 获取文章列表
def get_articles(session):
    articles_url = "https://www.xuexi.cn/lgdata/1000000000000000002/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(articles_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="item")
    return articles

# 阅读文章
def read_article(session, article_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(article_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="content")
    print(content.text)


# 获取视频列表
def get_videos(session):
    videos_url = "https://www.xuexi.cn/lgdata/1000000000000000002/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(videos_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    videos = soup.find_all("div", class_="item")
    return videos

# 观看视频
def watch_video(session, video_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(video_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    video_id = soup.find("div", class_="player").get("data-vid")
    play_url = f"https://www.xuexi.cn/a191dbc3067d516c2c9fc68bddf1133b/data9a916106ca7970a8dc087a191dbc3067.js?vid={video_id}"
    session.get(play_url, headers=headers)
    print(f"已观看视频：{video_url}")


# 获取每日答题列表
def get_daily_questions(session):
    daily_questions_url = "https://www.xuexi.cn/lgdata/1000000000000000002/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = session.get(daily_questions_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.find_all("div", class_="item")
    return questions

# 回答每日答题
def answer_daily_questions(session, questions):
    for question in questions:
        question_url = question["href"]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = session.get(question_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        answer = soup.find("div", class_="answer").text
        print(f"问题：{question_url} 答案：{answer}")


# 发表观点
def post_opinion(session, content):
    post_url = "https://www.xuexi.cn/forum/publish"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
        "content": content
    }
    response = session.post(post_url, headers=headers, data=data)
    return response.status_code

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


# 主函数
def main():
    username = "your_username"
    password = "your_password"
    session = login(username, password)
    #文章学习
    articles = get_articles(session)
    for article in articles:
        article_url = article["href"]
        read_article(session, article_url)
    #视频学习
    videos = get_videos(session)
    for video in videos:
        video_url = video["href"]
        watch_video(session, video_url)

    #每日答题
    questions = get_daily_questions(session)
    answer_daily_questions(session, questions)
    #评论
    content = "这是我的观点"
    post_opinion(session, content)
    #浏览本地频道
    channel_id = "your_channel_id"
    browse_local_channel(session, channel_id)

if __name__ == "__main__":
    main()
