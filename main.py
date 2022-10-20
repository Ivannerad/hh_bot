import argparse
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from helpers import hh_login, find_with_filters, apply
from selenium_class import SeleniumWith


def main():
    login = input('Login:')
    password = input('Password:')
    search_url = input('Search url:')
    letter_path = input('Letter path, just press enter if no letter:')
    
    if letter_path != '':
        with open(letter_path, 'r') as file:
            covering_letter = file.read()
    else:
        covering_letter = None

    with SeleniumWith() as driver:
        driver.get('https://hh.ru/')
        driver.maximize_window()
        # Wait to find elements
        driver.implicitly_wait(20)

        driver = hh_login(driver, password, login)
        driver = find_with_filters(driver, search_url)
        
        # covering_letter = 'Пожалуйста рассмотрите мое резюме.'
        driver = apply(driver, search_url, covering_letter=covering_letter)

        time.sleep(10)
    

if __name__ == '__main__':
    main()
    