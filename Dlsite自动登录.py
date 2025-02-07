from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 配置浏览器驱动
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开登录页面
driver.get('https://login.dlsite.com/login?user=self')

# 查找元素并输入信息
driver.find_element(By.NAME, 'login_id').send_keys('用户id')
driver.find_element(By.NAME, 'password').send_keys('密码')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

# 验证登录（根据页面内容调整）
if driver.current_url == 'https://www.dlsite.com/home/mypage':
    print("登录成功！")
    # 后续操作...
else:
    print("登录失败！")

# 关闭浏览器
# driver.quit()
