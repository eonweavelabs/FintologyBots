from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Opploans
# -----------------------------------------------------------------

def Opploans(driver, data, product_id):
    try:
        driver.get(
            "https://secure.opploans.com/register"
        )
        random_sleep(15)

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")

        random_sleep(20)
        
        # Email Address
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)
        
        # Primary Phone Number
        write_delay(driver, '//*[@id="phone"]', personal.get("mobileNumber"))
        random_sleep(1)
        
        # Legal First Name
        write_delay(driver, '//*[@id="firstName"]', personal.get("firstName"))
        random_sleep(1)
        
        # MI (Middle Initial)
        if len(personal.get("middleName")):
            write_delay(driver, '//*[@id="middleName"]', personal.get("middleName"))
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
        
        # Legal Last Name
        write_delay(driver, '//*[@id="lastName"]', personal.get("lastName"))
        random_sleep(1)
        
        # DOB
        write_delay(driver, '//*[@id="dateOfBirth"]', personal.get("dob"))
        random_sleep(1)
        
        # SSN or Individual tax id
        write_delay(driver, '//*[@id="socialSecurity"]', personal.get("ssn"))
        random_sleep(1)
        
        # Residential Address
        write_delay(driver, '//*[@id="address.residential.addressLine1"]', personal.get("homeAddress"))
        random_sleep(1)
        
        # ZIP Code
        write_delay(driver, '//*[@id="address.residential.zipcode"]', personal.get("zipcode"))
        random_sleep(1)
        
        # City
        write_delay(driver, '//*[@id="address.residential.city"]', personal.get("city"), clear=True)
        random_sleep(1)
        
        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="address.residential.state"]')
                select = Select(select_element)
                select.select_by_value(personal.get("state"))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Total Annual Income
        write_delay(driver, '//*[@id="totalAnnualIncome"]', personal.get("grossIncome"))
        random_sleep(1)
        
        # Monthly Rent/Mortgage
        write_delay(driver, '//*[@id="monthlyRentMortgage"]', personal.get("monthlymortage"))
        random_sleep(1)
        
        # Business Role
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="business.authorizingSignature"]')
                select = Select(select_element)
                select.select_by_value('Owner')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Business Legal Structure
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="business.businessLegalStructure"]')
                select = Select(select_element)
                select.select_by_value('Other')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Legal Business Name
        write_delay(driver, '//*[@id="legalBusinessName"]', business.get("legalName"))
        random_sleep(1)
        
        # Select If Your Business Address Is The Same As Your Residential Address
        send_click(driver, '//*[@id="business-information-section"]/div[3]/div[3]/div/div/label')
        random_sleep(1)
        
        # Business Phone Number
        write_delay(driver, '//*[@id="business.businessPhoneNumber"]', business.get("phoneNumber"))
        random_sleep(1)
        
        # Business Ownership type
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(by=By.XPATH, value='//*[@id="business.ownershipTypeCode"]')
                select = Select(select_element)
                select.select_by_value('Privately Owned')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        # Employer Identification Number (EIN)
        write_delay(driver, '//*[@id="business.businessTaxId"]', business.get("taxId"))
        random_sleep(1)
        
        # Business industry
        write_delay(driver, '//*[@id="industryQuestions.search-input"]', business.get("industry"))
        random_sleep(1)
        
        # Annual Business Revenue
        write_delay(driver, '//*[@id="business.businessAnnualRevenue"]', business.get("annualRevenue"))
        random_sleep(1)
        
        # Business spend per month
        write_delay(driver, '//*[@id="business.businessMonthlySpendOnCardsAmount"]', business.get("monthlySpend"))
        random_sleep(1)
        
        # Is your business headquartered in the U.S.?
        send_click(driver, '//*[@id="additional-business-information-section"]/div[3]/div[6]/div/div/div/fieldset/div[1]/label')
        random_sleep(1)
        
        # Is your business legally formed, incorporated and/or registered in the U.S.?
        send_click(driver, '//*[@id="additional-business-information-section"]/div[3]/div[7]/div/div/div/fieldset/div[1]/label')
        random_sleep(1)
        
        # Is your business primarily based in the U.S.?
        send_click(driver, '//*[@id="additional-business-information-section"]/div[3]/div[8]/div/div/div/fieldset/div[1]/label')
        random_sleep(1)
        
        # Do you own 25% or more of the business?
        send_click(driver, '//*[@id="business-owners-section"]/div[3]/div/div[1]/fieldset/div[1]/label')
        random_sleep(1)
       
        # Do you own 25% or more of the business = 2
        send_click(driver, '//*[@id="business-owners-section"]/div[3]/div/div[2]/fieldset/div[2]/label')
        random_sleep(1)
        
        # Checkbox - 1
        send_click(driver, '//*[@id="decision-maker-section"]/div[3]/div/div/div/label')
        random_sleep(1)
        
        # checkbox - 2
        send_click(driver, '//*[@id="additional-information-section"]/div[3]/div/div[1]/div/label')
        random_sleep(1)
        
        # Continue
        send_click(driver, '//*[@id="root"]/div/div/main/div[3]/div/form/div/div[3]/button')
        random_sleep(1)
        
        # Continue = 2
        send_click(driver, '//*[@id="root"]/div/div/main/div[3]/div/form/div/div[4]/button')
        random_sleep(1)
        
        # Submit Application
        send_click(driver, '//*[@id="AdditionalAcknowledgements"]/div[2]/div[2]/div/button')
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Opploans"
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
        full_name = data.get("personal").get("firstName") + " " + data.get("personal").get("lastName")
        card_name = "Opploans"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
          