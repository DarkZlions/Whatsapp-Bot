from selenium import webdriver
import requests
import os
import time
import zipfile

def validBrowser(b: str):
    return 'chrome' in b or 'edge' in b or 'firebox' in b or 'safari' in b


browserpreference = str()


browserIsAllowed = False

while not browserIsAllowed:
    browserpreference = str(input("Type your browser (Only available are: 'Chrome', 'Edge' (not Edge legacy), 'FireFox', 'Safari'): "))
    if validBrowser(browserpreference):
        browserIsAllowed = True
    else:
        print("{} isn't supported by this bot.".format(browserpreference))


try:
    if not os.path.exists('C:/webdriver/'):
        os.mkdir('C:/webdriver/', 0o755)
except OSError:
    print("Error can't find and create directory: 'C:/webdriver' ")
else:
    print("Created a new directory in: 'C:/webdriver' ")

chrome_url_83 = 'https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip'
chrome_url_84 = 'https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_win32.zip'
chrome_url_85 = 'https://chromedriver.storage.googleapis.com/85.0.4183.38/chromedriver_win32.zip'

edge_url_86_0_606_0 = 'https://msedgedriver.azureedge.net/86.0.606.0/edgedriver_win64.zip'
edge_url_86_0_605_0 = 'https://msedgedriver.azureedge.net/86.0.605.0/edgedriver_win64.zip'
edge_url_86_0_604_0 = 'https://msedgedriver.azureedge.net/86.0.604.0/edgedriver_win64.zip'
edge_url_85_0_564_30 = 'https://msedgedriver.azureedge.net/85.0.564.30/edgedriver_win64.zip'
edge_url_85_0_564_23 = 'https://msedgedriver.azureedge.net/85.0.564.23/edgedriver_win64.zip'
edge_url_85_0_564_18 = 'https://msedgedriver.azureedge.net/85.0.564.18/edgedriver_win64.zip'
edge_url_84_0_524_0 = 'https://msedgedriver.azureedge.net/84.0.524.0/edgedriver_win64.zip'
edge_url_84_0_523_0 = 'https://msedgedriver.azureedge.net/84.0.523.0/edgedriver_win64.zip'
edge_url_84_0_522_59 = 'https://msedgedriver.azureedge.net/84.0.522.59/edgedriver_win64.zip'

firefox_url_0_27_0 = 'https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win64.zip'
firefox_url_0_26_0 = 'https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip'
firefox_url_0_25_0 = 'https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-win64.zip'

browser = None

if 'chrome' in browserpreference:
    if os.path.exists('C:/webdriver/chromedriver.exe'):
        browser = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
    else:
        v = int(0)
        r = None
        validVersion = False
        while not validVersion:
            v = int(input("Type in your Chrome version(Supported version: 83, 84, 85): "))

            if v == 83:
                r = requests.get(chrome_url_83, allow_redirects=True)
            elif v == 84:
                r = requests.get(chrome_url_84, allow_redirects=True)
            elif v == 85:
                r = requests.get(chrome_url_85, allow_redirects=True)
            else:
                print("{} isn't a supported version of Chrome.".format(v))
                continue

            validVersion = True

        filename = 'C:/webdriver/chrome_webdriver_{}.zip'
        open(filename.format(v), 'wb').write(r.content)
        with zipfile.ZipFile(filename.format(v), "r") as zip_ref:
            zip_ref.extractall('C:/webdriver/')

        browser = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')

elif 'edge' in browserpreference:
    if os.path.exists('C:/webdriver/msedgedriver.exe'):
        browser = webdriver.Edge(executable_path='C:/webdriver/msedgedriver.exe')
    else:
        v = str('')
        r = None
        validVersion = False
        while not validVersion:
            v = str(input("Type in your Edge version(Supported version: 86.0.606.0, 86.0.605.0, 86.0.604.0, 85.0.564.30, 85.0.564.23, 85.0.564.18, 84.0.524.0, 84.0.523.0, 84.0.522.59: "))

            if "86.0.606.0" in v:
                r = requests.get(edge_url_86_0_606_0, allow_redirects=True)
            elif "86.0.605.0" in v:
                r = requests.get(edge_url_86_0_605_0, allow_redirects=True)
            elif "86.0.604.0" in v:
                r = requests.get(edge_url_86_0_604_0, allow_redirects=True)
            elif "85.0.564.30" in v:
                r = requests.get(edge_url_85_0_564_30, allow_redirects=True)
            elif "85.0.564.23" in v:
                r = requests.get(edge_url_85_0_564_23, allow_redirects=True)
            elif "85.0.564.18" in v:
                r = requests.get(edge_url_85_0_564_18, allow_redirects=True)
            elif "84.0.524.0" in v:
                r = requests.get(edge_url_84_0_524_0, allow_redirects=True)
            elif "84.0.523.0" in v:
                r = requests.get(edge_url_84_0_523_0, allow_redirects=True)
            elif "84.0.522.59" in v:
                r = requests.get(edge_url_84_0_522_59, allow_redirects=True)
            else:
                print("{} isn't a supported version of Edge.".format(v))
                continue

            validVersion = True

        filename = 'C:/webdriver/edge_webdriver_{}.zip'
        open(filename.format(v), 'wb').write(r.content)
        with zipfile.ZipFile(filename.format(v), "r") as zip_ref:
            zip_ref.extractall('C:/webdriver/')

        browser = webdriver.Edge(executable_path='C:/webdriver/msedgedriver.exe')

elif 'firefox' in browserpreference:
    if os.path.exists('C:/webdriver/geckodriver.exe'):
        browser = webdriver.Firefox(executable_path='C:/webdriver/geckodriver.exe')
    else:
        v = str('')
        r = None
        validVersion = False
        while not validVersion:
            v = str(input("Type in your FireFox version(Supported version: 0.27.0, 0.26.0, 0.25.0): "))

            if "0.27.0" in v:
                r = requests.get(firefox_url_0_27_0, allow_redirects=True)
            elif "0.26.0" in v:
                r = requests.get(firefox_url_0_26_0, allow_redirects=True)
            elif "0.25.0" in v:
                r = requests.get(firefox_url_0_25_0, allow_redirects=True)
            else:
                print("{} isn't a supported version of Firefox.".format(v))
                continue

            validVersion = True

        filename = 'C:/webdriver/firefox_driver.zip'
        open(filename, 'wb').write(r.content)
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall('C:/webdriver/')

        browser = webdriver.Firefox(executable_path='C:/webdriver/geckodriver.exe')

user_name = str(input("Type the username of person in: "))
message = str(input("Type in the message you want to send: "))
count = int(input("Type how many times the message should be send: "))

default_message_key = str(input("For other message key class type name else type 'default' to skip it: "))
if 'default' in default_message_key:
    default_message_key = '_3uMse'

default_button_key = str(input("For other button key class type name else type 'default' to skip it: "))
if 'default' in default_button_key:
    default_button_key = '_1U1xa'

print("Scan the QR-Code in the browser window to open 'whatsapp' !")

time.sleep(5)

browser.get('https://web.whatsapp.com/')

time.sleep(20)

i = 0
while i < count:

    user = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
    user.click()

    message_box = browser.find_element_by_xpath('//div[@class="{}"]'.format(default_message_key))
    message_box.send_keys(message)

    message_box = browser.find_element_by_xpath('//button[@class="{}"]'.format(default_button_key))
    message_box.click()
    i+=1

print("Program has exited.")