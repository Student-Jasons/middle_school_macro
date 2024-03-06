from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())



browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get("https://itmainjp.cafe24.com/app/regi/login.php")

browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input").send_keys("11132")
browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td[2]/input").send_keys("0826")
e = browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span/font")
print(e)
# /html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span/font/font[1]
# /html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span/font/font[2]
for i in range(1, 10):
    try:
        browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input").send_keys(browser.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span/font/font[{i}]").text)
        print(browser.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/span/font/font[{i}]").text)
    except:
        break
browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[6]/td/table/tbody/tr/td[5]/input").click()
browser.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/div[2]/input[1]").click()
browser.find_element(By.XPATH, "/html/body/table/tbody/tr[4]/td/table/tbody/tr/td/div[2]/input[1]").click()
browser.find_element(By.XPATH, "/html/body/table/tbody/tr[5]/td/input[1]").click()
browser.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td[1]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/a").click()
