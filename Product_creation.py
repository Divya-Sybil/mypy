from idlelib import browser
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import Login_Screen

driver = webdriver.Firefox(executable_path=r'E:\Thrillophili\geckodriver.exe')
driver.get("http://staging-partners.thrillophilia.com/admin/login")

if Login_Screen.login() == True:
    print("login successfull")
else :
    print("login failed")

driver.find_element_by_xpath('//*[@id="admin-app"]/div[2]/div/div[3]/div[2]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="admin-app"]/div[2]/div/div[3]/div[2]/div[2]/div[3]/a').click()

def prod_basic_details(self=None):
   try:
        name = driver.find_elements_by_xpath("//*[@id='basic-details-form']/div[1]/label/input")
        name.sendKeys("Demo1")
        if (len(name)==0) :
            print("The Name cannot be blank")
        else :
            for bType in browser.find_elements_by_xpath ("//*[@type='radio']"):
                    if (not bType.geText().equals("Group", "Private")) :
                     driver.close()
                    else:
                        location_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="basic-details-form"]/div[3]/label/div[2]/div/div[1]')))
                        for element in location_elements:
                            print(element.text)
                        if (len(location_elements)==0):
                            print("The default is not selected")
                        else:
                            print("The default value is selected")


        product_overview = driver.find_elements_by_xpath('//*[@id="basic-details-form"]/div[4]/label/div[2]/div[2]/div[1]/p/span')
        product_overview.sendKeys("Product overview Demo")

        if (len(product_overview)==0):
            print ("The overview of the product cannot be blank")
            self.driverfind_elements_by_xpath('//*[@id="basic-details-form"]/div[4]/label/div[2]/div[2]/div[1]/p/span').send_keys(Keys.NULL)

        product_long_desc = driver.find_elements_by_xpath('// *[ @ id = "basic-details-form"] / div[5] / label / div[2] / div[2] / div[1]')
        product_long_desc.sendKeys("Product Long Description Demo")

        if (len(product_long_desc) == 0):
            print("The overview of the product cannot be blank")
            self.driverfind_elements_by_xpath('// *[ @ id = "basic-details-form"] / div[5] / label / div[2] / div[2] / div[1]').send_keys(Keys.NULL)

        for txt_field_list in browser.find_elements_by_Class("text-field-list"):
            if (len(txt_field_list)==0):
                print("The Highlights and Know before you go fields are not required")
        for selector_field in browser.find_elements_by_class("selector-field__value-container selector-field__value-container--is-multi selector-field__value-container--has-value css-1hwfws3"):
            if(len(selector_field)==0):
                print("The accessibilities and Things to Carry Fields are not required")

        trip_Slider = driver.find_element_by_class_name("rc-slider-rail").get_attribute("value")
        if (len(trip_Slider)>0 or len(trip_Slider)<=10):
            driver.find_elements_by_xpath('//*[@id="admin-app"]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/a')
       wait = WebDriverWait(browser, 5)
   except:
   print("Failed")

driver.close()
driver.quit()
