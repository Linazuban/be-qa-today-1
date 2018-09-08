from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get('http://www.google.com')

# Open page
driver.get('http://www.google.com')

driver.find_element_by_name('q').send_keys("Be QA Today")
driver.find_element_by_name('q').submit()
assert driver.find_element_by_link_text('Be QA Today').is_displayed()

def cube():
    print ("number:"+number)
    cube(23)

