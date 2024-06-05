from .base import *

# 主函数
def main():
    # username = "your_username"
    # password = "your_password"
    # session = login(username, password)
    #登录
    login()
    #文章学习
    learn_articles()
    #视频学习
    learn_videos()
    # #文章学习
    # articles = get_articles(session)
    # for article in articles:
    #     article_url = article["href"]
    #     read_article(session, article_url)
    # #视频学习
    # videos = get_videos(session)
    # for video in videos:
    #     video_url = video["href"]
    #     watch_video(session, video_url)

    #每日答题
    questions = get_daily_questions(session)
    answer_daily_questions(session, questions)
    # #评论
    # content = "这是我的观点"
    # post_opinion(session, content)
    #随机选择文章
    select_random_article()
    #添加评论
    add_comment("中国共产党员，不忘初心，牢记使命！")
    #删除评论
    delete_comment()
    #浏览本地频道
    channel_id = "your_channel_id"
    browse_local_channel(session, channel_id)
    #趣味答题
    #fun_quiz()
    #判断趣味答题题目子类型
    result = judge_fun_quiz()
    print("识别结果：", result)
    #退出
    driver.quit()

if __name__ == "__main__":
    main()
