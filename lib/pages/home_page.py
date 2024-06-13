from pages.base_page import BasePage
from web_elements.home_web_elements import HomeWebElements
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def __init__(self, context):
        super().__init__(context.browser)  # cambiamos self.driver por context.browser
        self.context = context
        self.url = "https://www.booking.com"  # Define aquí la URL del home
        self.elements = HomeWebElements()

    def navigate(self):
        self.context.browser.get(self.url)
    
    def is_home_page(self):
        return self.url == self.context.browser.current_url  # Cambiamos self.context.driver por self.context.browser
    
    def click_menu_option(self, menu_option):
        locator = getattr(self.elements, f"button_{menu_option}")
        self.wait.until(EC.presence_of_element_located(locator)).click()