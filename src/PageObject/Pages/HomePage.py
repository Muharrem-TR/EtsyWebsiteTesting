import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

base_url = "https://www.etsy.com/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.siteSettingsBtn_ID = "locale-picker-trigger"
        self.saveBtn_Name = "save"




    def get_siteSettingsBtn_ID(self):
        return self.driver.find_element(By.ID, self.siteSettingsBtn_ID)
    def get_saveBtn_Name(self):
        return self.driver.find_element(By.NAME, self.saveBtn_Name)



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

    def mainInformationOfThePage(self):
        siteUrl = self.driver.current_url
        self.findAndClick("siteSettingsBtn_ID")
        region = self.driver.find_element(By.XPATH,"(//option[@selected='selected'])[1]").text
        language = self.driver.find_element(By.XPATH,"(//option[@selected='selected'])[2]").text
        # currency = self.driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text.split(" ")[3]
        # currency = self.driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text[2:]
        currency = self.driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text[-4:-1]
        print("<------------------------------------------------------------------>")
        print("Site Ayarları= Bölge: "+region+" | Dil: "+language+" | Para Birimi: "+currency)
        print("<------------------------------------------------------------------>")
        self.driver.get(siteUrl)

    def changeMainInformationOfRandomPage(self):
        siteUrl = self.driver.current_url
        self.findAndClick("siteSettingsBtn_ID")
        ddmenuRegion = self.driver.find_element(By.ID, "locale-overlay-select-region_code")
        regionMenusu = Select(ddmenuRegion)
        randomRegionInt = random.randrange(1, len(regionMenusu.options))
        regionMenusu.select_by_index(randomRegionInt)

        ddmenuLanguage = self.driver.find_element(By.ID, "locale-overlay-select-language_code")
        languageMenusu = Select(ddmenuLanguage)
        randomLanguageInt = random.randrange(1, len(languageMenusu.options))
        languageMenusu.select_by_index(randomLanguageInt)

        ddmenuCurrency = self.driver.find_element(By.ID, "locale-overlay-select-currency_code")
        currencyMenusu = Select(ddmenuCurrency)
        randomCurrencyInt = random.randrange(1, len(currencyMenusu.options))
        currencyMenusu.select_by_index(randomCurrencyInt)

        self.findAndClick("saveBtn_Name")
        self.driver.get(siteUrl)



    def findAndClick(self, strElement):
        match strElement:
            case "siteSettingsBtn_ID": self.myElement = self.get_siteSettingsBtn_ID()
            case "saveBtn_Name": self.myElement = self.get_saveBtn_Name()
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
            case "siteSettingsMsg_CSS": self.myElement = self.get_siteSettingsMsg_CSS()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        assert textElement in self.myElement.text
        print("Verified text: "+self.myElement.text)

    @staticmethod
    def get_base_url():
        return base_url

