from selenium import webdriver
driver = webdriver.Firefox(executable_path = 'F:\\Yogita\\ml\\geckodriver-v0.24.0-win64\\geckodriver.exe')
driver.get("http://192.168.43.1:8080/")
elem1 = driver.find_element_by_link_text("Tasker events control")
elem1.click()
elem2 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[2]/button[2]')
elem2.click()
