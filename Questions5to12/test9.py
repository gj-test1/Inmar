from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox();
driver.get("http://practiceselenium.com/practice-form.html");

driver.find_element_by_name("firstname").send_keys("MyFirst")
driver.find_element_by_name("lastname").send_keys("MyLast")
driver.find_element_by_id("sex-1").click()
driver.find_element_by_id("exp-5").click()
driver.find_element_by_id("datepicker").send_keys("none")
driver.find_element_by_id("tea3").click()
driver.find_element_by_id("tool-0").click()
driver.find_element_by_id("continents").click()
Select(driver.find_element_by_id("continents")).select_by_visible_text("Asia")
driver.find_element_by_xpath("//select[@id='continents']/option[3]").click()
driver.find_element_by_id("submit").click()

if driver.title != "Welcome":
    print "Not back in the home page!!!";
else:
    print "OK, we are back in the home page!!!";
