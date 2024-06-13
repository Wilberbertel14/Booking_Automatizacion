from pages.home_page import BasePage
from pages.web_elements import HomeWebElements
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context.driver)
        self.context = context
        self.url = HomeWebElements.url
        self.elements = HomeWebElements()

    def navigate(self):
        self.context.driver.get(self.url)
    
    def is_home_page(self):
        return self.url == self.context.driver.current_url
    
    def click_menu_option(self, menu_option):
        locator = getattr(self.elements, f"button_{menu_option}")
        self.wait.until(EC.presence_of_element_located(locator)).click()