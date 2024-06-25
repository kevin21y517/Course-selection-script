from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import keyboard

# 初始化webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://aais5.nkust.edu.tw/selcrs_std')  # 打開目標網頁


# 等待直到按下ENTER鍵開始自動點擊
# keyboard.wait('enter')



# 開始自動點擊，直到按下ESC鍵停止
try:
    while not keyboard.is_pressed('esc'):
        # 登入和其他操作...
        username_input = driver.find_element(By.ID, 'UserAccount')
        username_input.send_keys('UserAccount')
        password_input = driver.find_element(By.ID, 'Password')
        password_input.send_keys('Password')
        driver.find_element(By.ID, 'Login').click()
        time.sleep(3.0)
        driver.get('https://aais5.nkust.edu.tw/selcrs_std/AddSelect/AddSelectPage')
        time.sleep(1.0)
        driver.refresh()
        time.sleep(2.0)
        driver.find_element(By.ID, 'scr_selcode').send_keys('2166')
        time.sleep(0.5)
        driver.find_element(By.ID, 'courseSearch').click()
        time.sleep(1.0)
        driver.find_element(By.ID, '2166').click()
        time.sleep(1.0)
        try:
            # 嘗試找到顯示特定訊息的元素，這裡需要根據實際情況調整選擇器
            message_element = driver.find_element(By.XPATH, "//div[contains(text(), '加選間隔太短')]")
            if message_element:
                print("檢測到加選間隔太短的訊息，正在重新加載頁面...")
                time.sleep(6)  # 等待頁面重新加載
        except NoSuchElementException:
            # 如果沒有找到特定訊息的元素，則繼續操作
            pass

        driver.find_element(By.ID, 'btnLogout').click()
        time.sleep(1.0)
except Exception as e:
    print(f"發生錯誤: {e}")
finally:
    # 清理，關閉瀏覽器
    driver.quit()
