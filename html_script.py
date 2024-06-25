from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

# 初始化webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://aais6.nkust.edu.tw/selcrs_std')  # 打開目標網頁

course_code = '2155'
# 等待直到按下ENTER鍵開始自動點擊
# keyboard.wait('enter')

# 開始自動點擊，直到按下ESC鍵停止
# 登入和其他操作...
username_input = driver.find_element(By.ID, 'UserAccount')
username_input.send_keys('UserAccount')
password_input = driver.find_element(By.ID, 'Password')
password_input.send_keys('Password')
driver.find_element(By.ID, 'Login').click()
time.sleep(3.0)
driver.get('https://aais6.nkust.edu.tw/selcrs_std/AddSelect/AddSelectPage')
time.sleep(1.0)

try:
    while not keyboard.is_pressed('esc'):
        driver.find_element(By.ID, 'scr_selcode').send_keys(course_code)
        time.sleep(0.5)
        driver.find_element(By.ID, 'courseSearch').click()
        time.sleep(1.0)
        # 使用XPath定位包含特定文本"2154"的<td>元素
        td_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), '2155')]"))
        )
        # 使用JavaScript獲取<td>元素的文字顏色
        td_text_color = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).color;", td_element)
        if td_text_color == "rgb(133, 100, 4)":  # 或其他您認為代表綠色的值
            driver.find_element(By.ID, course_code).click()
            print("按鈕已點擊")
        else:
            print("按鈕背景色不是綠色")
except Exception as e:
    print(f"發生錯誤: {e}")
finally:
    # 清理，關閉瀏覽器
    driver.quit()
