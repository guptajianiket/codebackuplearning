from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("http://sites.tridiondemo.com/fontoui/?documentIds=tcm:5-7725")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//*[@id='index-app-root']/fds-app/fds-flex/fds-flex/fds-flex/fds-flex/editor-body/fds-block/fds-block/documents-list/fds-block/fx-templated-view-with-document-state-widgets/fds-block/fx-templated-view/fx-templated-view-content/cv-sheet-frame/cv-block-boundary/cv-block-body/cv-content/cv-frame[1]/cv-block-boundary/cv-block-body").send_keys("test00197369732649723")
driver.find_element(By.XPATH,"//*[@id='index-app-root']/fds-app/fds-flex/fds-flex/fds-flex/fds-flex/fds-masthead/fds-masthead-content/fds-flex/div/fds-button[5]/fds-button-style-masthead-default").click()
