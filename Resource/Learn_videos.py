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
