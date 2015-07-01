from selenium import webdriver

driver = webdriver.Firefox();
driver.get("http://www.seleniumframework.com/Practiceform/");
print "Original page has title of \"%s\" \n" % driver.title;

driver.find_element_by_xpath("//button[@onclick='newBrwTab()']").click()
print "Newly opened page has title of %s \n" % driver.title;



