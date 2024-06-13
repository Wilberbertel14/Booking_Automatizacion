from selenium import webdriver
from selenium.webdriver.common.by import By

class HomeWebElements:
    url = "https://www.booking.com"
    
    button_alojamiento = (By.XPATH, "//a[contains(@id,'accommodations')]")
    button_vuelo = (By.XPATH, "//a[contains(@id,'flights')]")
    button_alquiler = (By.XPATH, "//span[@class='bui-tab__text'][contains(.,'Alquiler de coches')]")
    button_atraccion = (By.XPATH, "//a[contains(@id,'attractions')]")
    button_taxis = (By.XPATH, "//path[contains(@d,'M21.75 15.5V8a.75.75 0 0 0-1.5 0v7.5a.75.75 0 0 0 1.5 0zm-16.5 0V8a.75.75 0 0 0-1.5 0v7.5a.75.75 0 0 0 1.5 0zM3 8.75h3a.75.75 0 0 0 0-1.5H3a.75.75 0 0 0 0 1.5zm6.75 6.75v-6a.75.75 0 0 1 1.5 0v6a.75.75 0 0 0 1.5 0v-6a2.25 2.25 0 0 0-4.5 0v6a.75.75 0 0 0 1.5 0zM9 13.25h3a.75.75 0 0 0 0-1.5H9a.75.75 0 0 0 0 1.5zm5.304-4.971l3 7.5a.75.75 0 0 0 1.392-.557l-3-7.5a.75.75 0 0 0-1.392.557zm3-.558l-3 7.5a.75.75 0 0 0 1.392.557l3-7.5a.75.75 0 0 0-1.392-.557zM.75 5h22.5a.75.75 0 0 0 0-1.5H.75a.75.75 0 0 0 0 1.5zm0 15h22.5a.75.75 0 0 0 0-1.5H.75a.75.75 0 0 0 0 1.5z')]")
    validadoralojamiento = (By.XPATH, "//div[contains(@class,'b7ab62d599')]")
    validadorvuelo = (By.XPATH, "//*[@id='basiclayout']/div/div/div[1]/div/div/div/div/div[1]/div")
    validadoralquiler = (By.XPATH, "//*[@id='b2runway_internal_actionPage']/div[4]/main/div[1]/div/p")
    validadoratraccion = (By.XPATH, "//input[contains(@data-testid,'search-input-field')]")
    validadortaxis = (By.XPATH, "//h2[@class='sb-searchbox__subtitle-text'][contains(.,'Traslados cómodos para ir a tu alojamiento y volver al aeropuerto')]")
    
    