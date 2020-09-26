from selenium import webdriver
from os import system
from time import sleep


def txt_to_wordlist():
    with open('script.txt') as file:
        list = [line.strip() for line in file]
        words = " ".join(list)
        return words.split()


profile_path = '--user-data-dir=/Users/davidohayon/Library/Application Support/Google/Chrome/'

system("osascript -e \'quit app \"Google Chrome\"\'")

name = input('Enter the name of user or group: ')

options = webdriver.ChromeOptions()
options.add_argument(profile_path)
driver = webdriver.Chrome(options=options)

sleep(1)
driver.execute_script("window.open();")
sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.get('https://web.whatsapp.com/')

sleep(2.5)

msg = txt_to_wordlist()
driver.find_element_by_xpath(f'//span[@title="{name}"]').click()
msg_box = driver.find_elements_by_class_name('_3FRCZ')[1]

for i in range(len(txt_to_wordlist())):
    msg_box.send_keys(msg[i])
    driver.find_element_by_class_name('_1U1xa').click()
    sleep(.2)

sleep(1)
driver.close()
sleep(1)
driver.quit()

system('open -a "Google Chrome"')
