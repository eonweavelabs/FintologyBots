from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Kapitus
# ------------------------------------------------------

def kapitus(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dobMonth": "10",
        #         "dobDay": "06",
        #         "dobYear": "2000",
        #         "ssn": 124365888,
        #         "homeAddress": "123 street",
        #         "city": "Jaipur",
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "mobileNumber": 7349303040,
        #         "creditScore": "700",
        #     },
        #     "business": {
        #         "requestedAmount": 50000,
        #         "useOfFunds": "Purchase Equipment",
        #         "dba": "My Business",
        #         "legalBusinessName": "My Legal Business",
        #         "businessAddress": "456 Business St",
        #         "businessCity": "Business City",
        #         "businessState": "AK",
        #         "businessZipcode": 12345,
        #         "businessPhone": 1234567890,
        #         "website": "https://mybusiness.com",
        #         "taxId": "12-3456789",
        #         "annualRevenue": 1000000,
        #         "entity": "LLC",
        #         "industryType": "Retail",
        #         "businessStartDate": "01/01/2010",
        #         "existingLoan": "NO",
        #         "lenderName": "",
        #         "loanOwnership": "",
        #         "howDidYouHear": "Online",
        #     }
        # }
        driver.get("https://kapitus.com/fast-application/")
        random_sleep(15)
        send_click(driver, '//*[@id=" "]/div/div[1]/section/div[2]/button')
        random_sleep(5)

        # Personal Information
        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dobMonth = data.get("personal").get("dobMonth")
        dobDay = data.get("personal").get("dobDay")
        dobYear = data.get("personal").get("dobYear")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        state = data.get("personal").get("state")
        zipcode = data.get("personal").get("zipcode")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        creditScore = data.get("personal").get("creditScore")

        # Business Information
        requestedAmount = data.get("business").get("requestedAmount")
        useOfFunds = data.get("business").get("useOfFunds")
        dba = data.get("business").get("dba")
        legalBusinessName = data.get("business").get("legalBusinessName")
        businessAddress = data.get("business").get("businessAddress")
        businessCity = data.get("business").get("businessCity")
        businessState = data.get("business").get("businessState")
        businessZipcode = data.get("business").get("businessZipcode")
        businessPhone = data.get("business").get("businessPhone")
        website = data.get("business").get("website")
        taxId = data.get("business").get("taxId")
        annualRevenue = data.get("business").get("annualRevenue")
        entity = data.get("business").get("entity")
        industryType = data.get("business").get("industryType")
        businessStartDate = data.get("business").get("businessStartDate")
        existingLoan = data.get("business").get("existingLoan")
        lenderName = data.get("business").get("lenderName")
        loanOwnership = data.get("business").get("loanOwnership")
        howDidYouHear = data.get("business").get("howDidYouHear")

        # random_sleep(20)

        # Fill out the form
        write_delay(driver, '//*[@id="form-field-firstname"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-lastname"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-email"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-phone"]', mobileNumber)
        random_sleep(1)
        send_click(driver, '//*[@id="form-field-isFactoring"]')
        random_sleep(1)
        send_click(driver, '//*[@id="form-field-PrivacyConsent"]')
        random_sleep(1)
        send_click(driver, '//*[@id="Apply-Now-Button"]')
        random_sleep(1)
        send_click(driver, '//*[@id="ButtonGroupItem3"]')
        random_sleep(1)
        send_click(driver, '//*[@id="Checkbox1"]')
        random_sleep(1)
        send_click(driver, '//*[@id="b4-Bottom"]/div/div/div[2]/button')
        random_sleep(1)
        
        

        # Business Financing
        write_delay(driver, '//*[@id="input_115_86"]', requestedAmount)
        random_sleep(1)
        send_click(driver, '//*[@id="label_115_134_11"]')
        # send_click(driver, f'//*[@id="choice_115_134_{useOfFunds}"]')
        random_sleep(1)
        send_click(driver, '//*[@id="gform_next_button_115_133"]')
        random_sleep(1)

        # Business Information
        write_delay(driver, '//*[@id="input_115_53"]', dba)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_177"]', legalBusinessName)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_160_1"]', businessAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_160_3"]', businessCity)
        random_sleep(1)
        # write_delay(driver, '//*[@id="input_115_160_4"]', businessState)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="input_115_160_4"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value(businessState)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_160_5"]', businessZipcode)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_161"]', businessPhone)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_189"]', website)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_162"]', taxId)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_87"]', annualRevenue)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_164"]', entity)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_96"]', industryType)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_123"]', businessStartDate)
        random_sleep(1)
        
        # send_click(driver, f'//*[@id="choice_115_174_{existingLoan}"]')
        # random_sleep(1)
        # if existingLoan == "YES":
        #     write_delay(driver, '//*[@id="input_115_187"]', lenderName)
        #     random_sleep(1)
        #     write_delay(driver, '//*[@id="input_115_176"]', loanOwnership)
        #     random_sleep(1)
        send_click(driver, '//*[@id="gform_next_button_115_1"]')
        random_sleep(10)

        # Personal Information
        write_delay(driver, '//*[@id="input_115_50"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_51"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_47"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_45"]', mobileNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_166_1"]', homeAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_166_3"]', city)
        random_sleep(1)
        # write_delay(driver, '//*[@id="input_115_166_4"]', state)
        
        
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="input_115_166_4"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_166_5"]', zipcode)
        random_sleep(1)
        # write_delay(driver, '//*[@id="input_115_97"]', creditScore)
        
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="input_115_97"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('$100,000 - $249,999')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_172_1"]', dobMonth)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_172_2"]', dobDay)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_172_3"]', dobYear)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_200"]', ssn)
        random_sleep(1)
        write_delay(driver, '//*[@id="input_115_88"]', howDidYouHear)
        random_sleep(1)
        send_click(driver, '//*[@id="gform_next_button_115_178"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Kapitus"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "Kapitus"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
