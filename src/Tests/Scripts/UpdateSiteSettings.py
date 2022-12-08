from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class updateSiteSettings(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        hp = HomePage(driver)
        hp.pageValidation()
        hp.mainInformationOfThePage()
        hp.changeMainInformationOfRandomPage()
        hp.mainInformationOfThePage()


    # def test002(self):
    #     driver = self.driver
    #     driver.get(HomePage.get_base_url())
    #     hp = HomePage(driver)
    #     hp.pageValidation()
    #
    #
    #     hp.findAndClick("siteSettingsBtn_ID")
    #     region = driver.find_element(By.XPATH, "(//option[@selected='selected'])[1]").text
    #     language = driver.find_element(By.XPATH, "(//option[@selected='selected'])[2]").text
    #     # currency = driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text.split(" ")[3]
    #     # currency = driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text[2:]
    #     currency = driver.find_element(By.XPATH, "(//option[@selected='selected'])[3]").text[-4:-1]
    #     print("Site Ayarları= Bölge: " + region + " | Dil: " + language + " | Para Birimi: " + currency)
    #     driver.back()
    #
    #
    #     hp.findAndClick("siteSettingsBtn_ID")
    #
    #     ddmenuRegion = driver.find_element(By.ID, "locale-overlay-select-region_code")
    #     regionMenusu = Select(ddmenuRegion)
    #     randomRegionInt = random.randrange(1, len(regionMenusu.options))
    #     regionMenusu.select_by_index(randomRegionInt)
    #
    #     ddmenuLanguage = driver.find_element(By.ID, "locale-overlay-select-language_code")
    #     languageMenusu = Select(ddmenuLanguage)
    #     randomLanguageInt = random.randrange(1, len(languageMenusu.options))
    #     languageMenusu.select_by_index(randomLanguageInt)
    #
    #     ddmenuCurrency = driver.find_element(By.ID, "locale-overlay-select-currency_code")
    #     currencyMenusu = Select(ddmenuCurrency)
    #     randomCurrencyInt = random.randrange(1, len(currencyMenusu.options))
    #     currencyMenusu.select_by_index(randomCurrencyInt)
    #
    #     hp.findAndClick("saveBtn_Name")
    #
    #
    #     hp.findAndClick("siteSettingsBtn_ID")
    #     region = driver.find_element(By.XPATH, "(//option[@selected='selected'])[1]").text
    #     language = driver.find_element(By.XPATH, "(//option[@selected='selected'])[2]").text
    #     # currency = driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text.split(" ")[3]
    #     # currency = driver.find_element(By.XPATH,"(//option[@selected='selected'])[3]").text[2:]
    #     currency = driver.find_element(By.XPATH, "(//option[@selected='selected'])[3]").text[-4:-1]
    #     print("Site Ayarları= Bölge: " + region + " | Dil: " + language + " | Para Birimi: " + currency)
    #     driver.back()