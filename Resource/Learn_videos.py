from .base import *

# 学习视频
def learn_videos():
    driver.get("https://www.xuexi.cn/lgpage/detail/index.html?id=VIDEO_ID")  # 替换为实际视频ID
    for i in range(6):
        video = driver.find_element(By.TAG_NAME, 'video')
        driver.execute_script("arguments[0].play();", video)  # 播放视频
        time.sleep(60)  # 每个视频播放1分钟
        driver.execute_script("arguments[0].pause();", video)  # 暂停视频
        if i < 5:
            next_video_btn = driver.find_element(By.XPATH, 'NEXT_VIDEO_BUTTON_XPATH')  # 替换为下一个视频按钮的XPath
            next_video_btn.click()
            time.sleep(5)  # 等待新视频加载


# # 获取视频列表
# def get_videos(session):
#     videos_url = "https://www.xuexi.cn/lgdata/1000000000000000002/index.html"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     response = session.get(videos_url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")
#     videos = soup.find_all("div", class_="item")
#     return videos

# # 观看视频
# def watch_video(session, video_url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     response = session.get(video_url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")
#     video_id = soup.find("div", class_="player").get("data-vid")
#     play_url = f"https://www.xuexi.cn/a191dbc3067d516c2c9fc68bddf1133b/data9a916106ca7970a8dc087a191dbc3067.js?vid={video_id}"
#     session.get(play_url, headers=headers)
#     print(f"已观看视频：{video_url}")
