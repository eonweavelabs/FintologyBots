from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Lighter Capital
# ------------------------------------------------------

def lighterCapital(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "companyName": "My Company",
        #         "website": "https://mycompany.com",
        #         "phoneNumber": 7349303040,
        #         "primaryBusinessLocation": "USA",
        #         "businessType": "Tech",
        #         "revenueAge6Months": "Yes",
        #         "currentMonthlyRevenueRange": "10000-50000",
        #         "numberOfCustomers": 100,
        #         "foundedMonth": "January",
        #         "foundedYear": 2010,
        #         "state": "AK",
        #         "comments": "No comments",
        #     }
        # }
        driver.get("https://www.lightercapital.com/apply-now")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        companyName = data.get("personal").get("companyName")
        website = data.get("personal").get("website")
        email = data.get("email")
        phoneNumber = data.get("personal").get("phoneNumber")
        primaryBusinessLocation = data.get("personal").get("primaryBusinessLocation")
        foundedMonth = data.get("personal").get("foundedMonth")
        foundedYear = data.get("personal").get("foundedYear")
        state = data.get("personal").get("state")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="FirstName"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="LastName"]', lastName)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="Company"]', companyName)
        random_sleep(1)

        # Website
        write_delay(driver, '//*[@id="Website"]', website)
        random_sleep(1)

        # Email Address
        write_delay(driver, '//*[@id="Email"]', email)
        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="Phone"]', phoneNumber)
        random_sleep(1)

        # Primary business Location
        write_delay(driver, '//*[@id="Country"]', primaryBusinessLocation)
        random_sleep(1)

        # Type "LIGHTER CAPITAL" and click NEXT
        write_delay(driver, '//*[@id="solvethispuzzle"]', "LIGHTER CAPITAL")
        random_sleep(1)
        send_click(driver, '//*[@id="mktoForm_3248"]/div[15]/span/button')
        random_sleep(1)

        # PAGE - 2
        # Business Type
        # write_delay(driver, '//*[@id="Tech_Company_Details__c"]', businessType)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Tech_Company_Details__c"]'
                )
                select = Select(select_element)
                select.select_by_value('Other')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # Have you been generating revenue for at least 6 months?
        # write_delay(driver, '//*[@id="Revenue_Age_6_Months__c"]', revenueAge6Months)
        random_sleep(1)

        # Current Monthly Revenue Range
        # write_delay(driver, '//*[@id="Current_Monthly_Revenue_Range__c"]', currentMonthlyRevenueRange)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Current_Monthly_Revenue_Range__c"]'
                )
                select = Select(select_element)
                select.select_by_value('100,000-200,000')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # Number of customers
        # write_delay(driver, '//*[@id="Number_of_Customers__c"]', numberOfCustomers)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Number_of_Customers__c"]'
                )
                select = Select(select_element)
                select.select_by_value('50 or more')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # Month founded
        # write_delay(driver, '//*[@id="Founded_Month__c"]', foundedMonth)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Founded_Month__c"]'
                )
                select = Select(select_element)
                select.select_by_value(foundedMonth)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # Year founded
        # write_delay(driver, '//*[@id="Founded_Year__c"]', foundedYear)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Founded_Year__c"]'
                )
                select = Select(select_element)
                select.select_by_value(foundedYear)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # State
        # write_delay(driver, '//*[@id="State"]', state)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="State"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        # Comments
        # write_delay(driver, '//*[@id="Applicant_Comments__c"]', comments)
        random_sleep(1)

        # SUBMIT
        send_click(driver, '//*[@id="mktoForm_3249"]/div[13]/span/button')
        random_sleep(15)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Lighter Capital"
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
        card_name = "Lighter Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
