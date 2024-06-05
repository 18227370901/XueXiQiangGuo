from .base import *

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
