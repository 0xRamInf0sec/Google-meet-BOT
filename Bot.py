from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import pyfiglet
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

def gmail():
    driver.get(
        "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("YOUR_EMAIL_ADDRESS")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@name='password']").send_keys("YOUR_PASSWORD")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
    driver.get(link)
    time.sleep(4)
    pg.hotkey('ctrl','d')
    pg.hotkey('ctrl','e')
    for i in range(5):
        pg.press('tab')
    time.sleep(2)
    pg.press('enter')
    print("Entered Class")
    time.sleep(60*60)
    for i in range(7):
        pg.press('tab')
    time.sleep(1)
    pg.press('enter')
    print('Meeting ended')

if __name__ == "__main__":
    banner = pyfiglet.figlet_format("G MEET BOT")
    print(banner)
    link = input("Enter the link : ")
    driver=webdriver.Chrome(chrome_options=opt,executable_path="C:/Users/User/Desktop/chromedriver.exe")
    gmail()

