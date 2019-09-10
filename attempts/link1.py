from selenium import webdriver
driver = webdriver.Firefox(executable_path = 'F:\\Yogita\\Knock-Knock\\ml\\Outp\\Project sem 8\\_Project\\geckodriver-v0.24.0-win64\\geckodriver.exe')
# driver.get("http://192.168.43.1:8080/")
# driver.get("http://192.168.43.120:5000/buzz")
#
# # elem1 = driver.find_element_by_link_text("Tasker events control")
# # elem1.click()
# # elem2 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[2]/button[2]')
# # elem2.click()
# # elem2 = driver.find_element_by_link_text("5")
# # elem2.click()
#
#
# for i in range(5):
#     elem = driver.find_element_by_xpath("/html/body/form/button")
#     elem.click()

driver.get("https://www.google.com/", verify=False)
