from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Fund Through
# ------------------------------------------------------

def fundThrough(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Krishan",
        #         "lastName": "Pratap",
        #         "title": "Ms.",
        #         "phone": 7349303040,
        #         "companyName": "My Company",
        #         "invoicePlatform": "Platform A",
        #         "businessRegistered": "State A",
        #         "businessIndustry": "Industry A",
        #         "annualRevenue": 876655,
        #         "invoiceBusinesses": "Yes",
        #         "fundingAmount": 50000,
        #         "fundingReason": "Expansion",
        #         "fundingUrgency": "Immediately",
        #         "referralSource": "Internet",
        #     }
        # }
        driver.get("https://www.fundthrough.com/getstarted/?_gl=1*2eh991*_gcl_au*MTAxODk4NzIwMy4xNzI2NjU4NjE3*_ga*MjAzOTg0NTk2OC4xNzI2NjU4NjE0*_ga_VX9RQJSWQP*MTcyNzQxMzU3OC4yLjAuMTcyNzQxMzU3OC42MC4wLjA.")
        random_sleep(15)

        personal = data.get("personal")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        title = personal.get("title")
        phone = personal.get("phone")
        email = data.get("email")
        companyName = personal.get("companyName")
        invoicePlatform = personal.get("invoicePlatform")
        businessRegistered = personal.get("businessRegistered")
        businessIndustry = personal.get("businessIndustry")
        annualRevenue = personal.get("annualRevenue")
        invoiceBusinesses = personal.get("invoiceBusinesses")
        fundingAmount = personal.get("fundingAmount")
        fundingReason = personal.get("fundingReason")
        fundingUrgency = personal.get("fundingUrgency")
        referralSource = personal.get("referralSource")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="FirstName"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="LastName"]', lastName)
        random_sleep(1)

        # Title
        write_delay(driver, '//*[@id="Title"]', title)
        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="Phone"]', phone)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="Email"]', email)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="Company"]', companyName)
        random_sleep(1)

        # Invoice Platform
        # write_delay(driver, '//*[@id="Do_you_use_any_of_these_invoice_platform__c"]', invoicePlatform)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="Do_you_use_any_of_these_invoice_platform__c"]'
                )                   
                select = Select(select_element)
                select.select_by_value('Cortex')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)

        # Business Registered
        # write_delay(driver, '', businessRegistered)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="Where_is_your_business_registered__c"]'
                )                   
                select = Select(select_element)
                select.select_by_value('United States')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Business Industry
        # write_delay(driver, '', businessIndustry)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="What_Industry_is_your_business_in__c"]'
                )                   
                select = Select(select_element)
                select.select_by_value('Other services')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Annual Revenue
        write_delay(driver, '//*[@id="AnnualRevenue"]', annualRevenue)
        random_sleep(1)

        # Invoice Businesses
        # write_delay(driver, '', invoiceBusinesses)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="Do_you_invoice_businesses__c"]'
                )                   
                select = Select(select_element)
                select.select_by_value(invoiceBusinesses)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Funding Amount
        # write_delay(driver, '', fundingAmount)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="How_much_funding_are_you_looking_for__c"]'
                )
                select = Select(select_element)
                select.select_by_value('Over $500k')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Funding Reason
        # write_delay(driver, '', fundingReason)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="Primary_Reason_for_Funding__c"]'
                )
                select = Select(select_element)
                select.select_by_value(fundingReason)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Funding Urgency
        # write_delay(driver, '', fundingUrgency)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="How_quickly_do_you_need_the_money__c"]'
                )
                select = Select(select_element)
                select.select_by_value(fundingUrgency)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Referral Source
        # write_delay(driver, '', referralSource)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="How_Did_You_Hear_About_Us__c"]'
                )
                select = Select(select_element)
                select.select_by_value('LinkedIn')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="mktoForm_1212"]/div[24]/span/button')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Fund Through"
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
        card_name = "Fund Through"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
