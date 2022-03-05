from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions import action_builder
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
ActionBuilder = n
Actionsbuilder = new Actions(Driver.Browser.Instance);
IAction dragAndDrop = builder.ClickAndHold(fromElement)
    .MoveByOffset(-1, -1)
    .MoveToElement(toElement)
    .Release(toElement)
    .Build();
dragAndDrop.Perform();