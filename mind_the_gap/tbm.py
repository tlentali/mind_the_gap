from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import config

def get_info():
    options = webdriver.FirefoxOptions()
    options.headless = config.HEADLESS

    driver = webdriver.Firefox(executable_path=r'geckodriver', options=options)
    driver.get(config.URL_WAY)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    return res

def extract_info(res):
    soup = BeautifulSoup(res, 'lxml')


    box = soup.find('div', {'class': 'l-time'})
    for element in box(text=lambda text: isinstance(text, Comment)):
        element.extract()


    all_hackathons = box.find_all('span', {'class': 'h4 text-normal'})

    result = []
    for hackathon in all_hackathons:
        hack = hackathon.find('span')
    
        result.append(hack.get_text())
    return result
