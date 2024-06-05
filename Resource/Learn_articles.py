from .base import *

# 学习文章
def learn_articles():
    driver.get("https://www.xuexi.cn/lgpage/detail/index.html?id=ARTICLE_ID")  # 替换为实际文章ID
    for i in range(6):
        time.sleep(60)  # 每篇文章学习1分钟
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到页面底部
        time.sleep(5)  # 等待滚动完成
        if i < 5:
            next_article_btn = driver.find_element(By.XPATH, 'NEXT_ARTICLE_BUTTON_XPATH')  # 替换为下一篇文章按钮的XPath
            next_article_btn.click()
            time.sleep(5)  # 等待新文章加载
