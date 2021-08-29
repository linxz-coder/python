from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# open chrome
# chrome_browser
# open chrome and maximize window
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# instead of print, you can use assert, if it is false, it will give an error
assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name("btn-default")
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
#css selector
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOOOOL' in output_message.text

#close the browser (the two methods are the same)
chrome_browser.close()
# chrome_browser.quit()







