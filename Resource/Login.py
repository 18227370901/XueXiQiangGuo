from .base import *

# # 登录学习强国
# def login(username, password):
#     login_url = "https://www.xuexi.cn/login"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     data = {
#         "username": username,
#         "password": password
#     }
#     session = requests.Session()
#     response = session.post(login_url, headers=headers, data=data)
#     return session

# 配置Chrome浏览器
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# 启动WebDriver
service = Service('C:/Users/cheng/PycharmProjects/学习强国/chromedriver-win64/chromedriver')  # 请替换为你chromedriver的路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 登录学习强国
def login():
    driver.get("https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fpc.xuexi.cn%2Fpoints%2Fmy-points.html")
    time.sleep(5)  # 等待页面加载
    # 手动扫码登录或其他方式登录
