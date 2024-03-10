import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from TestData.LinkData import LinkPageData




def test_linkmatrix(getData):

    #Nav_Xpath = "//*[@class = 'nav__link opioid-addiction']"
    Link_Text = getData["Link_Text"]
    service_obj = Service("/Users/rphilip/Documents/BrowserDriver/msedgedriver.exe")
    driver = webdriver.Edge(service=service_obj)
    driver.maximize_window()
    driver.get("https://www.sublocade.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class= 'save-preference-btn-handler onetrust-close-btn-handler']")))
    driver.find_element(By.XPATH, "//button[@class= 'save-preference-btn-handler onetrust-close-btn-handler']").click()

    if getData["Open_Modal"] == "Yes":
        link = driver.find_element(By.LINK_TEXT, Link_Text)
        link.click()
        driver.find_element(By.LINK_TEXT,"Accept").click()
        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
        #switch focus to child window
            if(w!=p):
                driver.switch_to.window(w)
                break
    elif getData["New_Tab"] == "Yes":
        link = driver.find_element(By.LINK_TEXT, Link_Text)
        link.click()
        p = driver.current_window_handle
        chwd = driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                driver.switch_to.window(w)
                break
    else:
        #wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class = 'nav__link opioid-addiction']"))).click()
        #wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//li/ul/li/a[contains(.,'About opioid addiction')]"))).click()
        link = driver.find_element(By.LINK_TEXT, Link_Text)
        link.click()

    Actual_URL = driver.current_url
    print("Expected URL : "+getData["Expected_URL"])
    print("Actual_URL : "+Actual_URL)
    assert (getData["Expected_URL"] == Actual_URL)
    #driver.close()


@pytest.fixture(params=LinkPageData.getLinkData())
def getData(request):
    return request.param