from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Amex Lowes Business Rewards Card
# -----------------------------------------------------------------

def AmexLowesBusinessRewardsCard(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "occupation": "Agriculture",
        #         "firstName": "Krishan Pratap",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "grossIncome": 546843,
        #         "nonTaxableIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "legalBusinessName": "My Business",
        #         "businessNameOnCard": "Business Card Name",
        #         "businessAddress": "123 Business St.",
        #         "businessZip": 10001,
        #         "city": "Business City",
        #         "state": "AK",
        #         "businessMobileNumber": 1234567890,
        #         "industryType": "Retail",
        #         "companyStructure": "LLC",
        #         "yearInBusiness": 5,
        #         "numberOfEmployees": 50,
        #         "grossBusiness": 1000000,
        #         "estimatedMonthly": 50000,
        #         "federalTax": "12-3456789",
        #         "roleInCompany": "Owner",
        #         "nameOnCard": "Krishan Pratap",
        #         "homePhoneNumber": 9876543210,
        #         "totalAnnual": 120000
        #     }
        # }
        # product_id = "668fb416133bed94c15bad51"
        
        driver.get(
            "https://www.americanexpress.com/en-us/credit-cards/referral/prospect/CC199E07F40F2D5A3E734316AA1F099C8DD14181370D95FDEDB9DE7E3F9750CB40B679F1568A4033B87A826F6C26F7DB70535E77337815CDD58332E71954B060DFE557E87DD83E4A14BD0B0A0046800C1346C97E59130E9323B4D86C8FDFDBB1499A5CFF7FB7C024F539B8F7FBD115A3512377C538F829D8BF38177756250EA291454460C28512726759A0457BCDFF6A059511E271B021B571AFC3100F6D5969FE65FB1753CA38E4BE9CD8C759420E8C27C9BB12D051E3502168A7B77A38E445C39A2DBCF9399352?CORID=L~I~B~A~G~E~t~K~i-1725776481018-1686437536&GENCODE=349992798545913&XLINK=MYCP&extlink=US-MGM-SPA_WEB_MYCA-copypaste-1110-201329-K44D%3A9969&ref=LIBAGEtKi&v=2"
        )
        random_sleep(15)
        # send_click(driver, '//*[@id="mainContent"]/div/main-container/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/span/div/button')
        # random_sleep(15)

        email = data.get("email")
        personal = data.get("personal")
        business = data.get("personal")

        random_sleep(20)

        # Email
        write_delay(driver, '//*[@id="email-39"]', email)
        random_sleep(1)

        # Legal Business Name
        write_delay(driver, '//*[@id="business-name-43"]', business.get("legalBusinessName"))
        random_sleep(1)

        # Business Name on Card
        write_delay(driver, '//*[@id="business-name-on-card-47"]', business.get("businessNameOnCard"))
        random_sleep(1)
        
        # Not DBA
        send_click(driver, '//*[@id="business-info-form-section"]/fieldset[2]/div[2]/div/dls-checkbox-input/div/label')
        random_sleep(1)

        # Business Address
        write_delay(driver, '//*[@id="street-address-59"]', business.get("businessAddress"))
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="zip-code-68"]', business.get("businessZip"))
        random_sleep(1)

        # City
        # write_delay(driver, '//*[@id="city-72"]', business.get("city"))
        # random_sleep(1)


        # Business Mobile Number
        write_delay(driver, '//*[@id="phone-number-83"]', business.get("businessMobileNumber"))
        random_sleep(1)

        
        # Industry Type
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="industry-type-136-list-dropdown"]')
                send_click(driver, '//*[@id="industry-type-136-listitems"]/span/ul/li[10]')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        # Company Structure
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="company-structure-87-list-dropdown"]')
                send_click(driver, '//*[@id="company-structure-87-listitems"]/span/ul/li[4]')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1



        # Years in Business
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="years-in-business-99-list-dropdown"]')
                send_click(driver, '//*[@id="years-in-business-99-listitems"]/span/ul/li[5]')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1



        # Number of Employees
        write_delay(driver, '//*[@id="number-of-employees-106"]', business.get("numberOfEmployees"))
        random_sleep(1)

        # Gross Business Revenue
        write_delay(driver, '//*[@id="annual-business-revenue-110"]', business.get("grossBusiness"))
        random_sleep(1)
        
        # Company Role
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="role-in-company-123-list-dropdown"]')
                send_click(driver, '//*[@id="role-in-company-123-listitems"]/span/ul/li[3]')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        # Estimated Monthly Spend
        write_delay(driver, '//*[@id="estimated-monthly-spend-114"]', business.get("estimatedMonthly"))
        random_sleep(1)

        # Federal Tax ID
        # write_delay(driver, '//*[@id="federal-tax-id-110"]', business.get("federalTax"))
        # random_sleep(1)

        # # Role in Company
        # select = Select(driver.find_element(By.XPATH, '//*[@id="role-in-company-115-list-dropdown"]'))
        # select.select_by_value(business.get("roleInCompany"))
        # random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="first-name-144"]', personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="last-name-152"]', personal.get("lastName"))
        random_sleep(1)

        # Same address
        send_click(driver, '//*[@id="personal-info-form-section"]/fieldset[1]/div[2]/div[2]/dls-checkbox-input/div/label')
        random_sleep(1)

        # Home Phone Number
        write_delay(driver, '//*[@id="phone-number-182"]', business.get("homePhoneNumber"))
        random_sleep(1)

        # SSN
        write_delay(driver, '//*[@id="ssn-225"]', personal.get("ssn"))
        random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="date-of-birth-190"]', personal.get("dob"))
        random_sleep(1)

        # Total Annual Income
        write_delay(driver, '//*[@id="annual-income-194"]', business.get("totalAnnual"))
        random_sleep(1)
        
        # non-taxable-income
        write_delay(driver, '//*[@id="non-taxable-income-198"]', business.get("nonTaxableIncome"))
        random_sleep(1)

        # Submit Button
        send_click(driver, '//*[@id="submit"]')
        random_sleep(15)

        # Screenshot and upload
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Amex Lowes Business Rewards Card"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
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
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Amex Lowes Business Rewards Card"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
