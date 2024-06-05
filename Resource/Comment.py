from .base import *

# 随机选择推荐文章
def select_random_article():
    driver.get("https://www.xuexi.cn/")
    time.sleep(5)  # 等待页面加载
    articles = driver.find_elements(By.CSS_SELECTOR, 'a[href*="lgpage/detail/index.html?id="]')
    random_article = random.choice(articles)
    random_article.click()
    time.sleep(5)  # 等待文章页面加载

# 添加指定评论内容
def add_comment(comment_text):
    comment_box = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="写评论…"]')
    comment_box.send_keys(comment_text)
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[class*="submit"]')
    submit_button.click()
    time.sleep(5)  # 等待评论提交

# 删除评论
def delete_comment():
    delete_button = driver.find_element(By.CSS_SELECTOR, 'button[class*="delete"]')
    delete_button.click()
    time.sleep(5)  # 等待评论删除



# # 发表观点
# def post_opinion(session, content):
#     post_url = "https://www.xuexi.cn/forum/publish"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     data = {
#         "content": content
#     }
#     response = session.post(post_url, headers=headers, data=data)
#     return response.status_code
