from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


base_url = "https://www.etsy.com/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.acceptButton_CSS = "button[data-uia='cookie-disclosure-button-accept']"



    def get_acceptButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.acceptButton_CSS)



    def scrollToElementMid(self, element):
        scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
        "var elementTop = arguments[0].getBoundingClientRect().top;"
        "window.scrollBy(0, elementTop-(viewPortHeight/2));"
        self.driver.execute_script(scrollElementIntoMiddle, element)

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def moveToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scrollHeight(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def pageValidation(self):
        siteUrl = self.driver.current_url
        assert "etsy" in siteUrl
        baslik = self.driver.title
        print("<------------------------------------------------------------------------------------------------>")
        print("Bulunduğunuz sitenin ismi " + baslik.split("-")[0] + "URL adresi ise " + siteUrl + " olarak doğrulanmıştır.")
        print("<------------------------------------------------------------------------------------------------>")



    def findAndClick(self, strElement):
        match strElement:
            case "acceptButton_CSS": self.myElement = self.get_acceptButton_CSS()
        self.scrollToElementMid(self.myElement)
        EC.element_to_be_clickable(self.myElement)
        self.myElement.click()

    def findAndSend(self, strElement, strText):
        match strElement:
            case "emailInput_ID": self.myElement = self.get_emailInput_ID()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        self.myElement.send_keys(strText)

    def findAndVerify(self, strElement, textElement):
        match strElement:
            case "heroTitle_CSS": self.myElement = self.get_heroTitle_CSS()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        assert textElement in self.myElement.text
        print("Verified text: "+self.myElement.text)

    @staticmethod
    def get_base_url():
        return base_url
