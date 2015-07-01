from selenium import webdriver

browser = webdriver.Firefox();
browser.get('http://cbsnews.com');

page_title = browser.title;
print page_title;

browser.close();