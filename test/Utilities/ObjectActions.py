class ObjectActions:
    @staticmethod
    def set_text(driver, xpath, text):
        driver.find_element(xpath[0], xpath[1]).send_keys(text)

    @staticmethod
    def click(driver, xpath):
        driver.find_element(xpath[0], xpath[1]).click()

    @staticmethod
    def get_text(driver, xpath):
        return driver.find_element(xpath[0], xpath[1]).text
