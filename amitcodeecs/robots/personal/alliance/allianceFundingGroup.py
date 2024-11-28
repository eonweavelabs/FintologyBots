from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Alliance Funding Group
# -----------------------------------------------------

def fundingGroup(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "citizenship": "Indiam",
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "membership": 456836297456,
        #         "housingStatus": "Own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "rent": 15000,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #         "nameofbusiness": "My Business Name",
        #         "businessaddress": "456 Business Rd., Suite 100, New York",
        #         "businessphonenumber": 1234567890,
        #         "legalstructureofbusiness": "Corporation",
        #         "typeoffinancialinstitute": "Bank",
        #         "taxIdNumber": "12-3456789",
        #         "lineofbusiness": "Retail",
        #         "numberofemployees": 50,
        #         "yearinbusiness": 10,
        #         "countryofbusinessformation": "USA",
        #         "securitywordhint": "Pet's name",
        #         "securityword": "Fluffy",
        #         "dba": "My DBA",
        #         "businessType": "Retail",
        #         "inBusinessSince": "2010",
        #         "website": "https://mybusiness.com",
        #         "contactTitle": "CEO",
        #         "ownershipPercent": 100,
        #         "contactExt": "123",
        #         "equipDesc": "Office Equipment",
        #         "equipCost": 50000,
        #         "equipYear": 2022,
        #         "preferredTerm": 36,
        #         "reasonForUpdate": "Expansion",
        #         "comments": "No comments",
        #         "attachment1": "path/to/attachment1",
        #         "attachment1Type": "Invoice"
        #     }
        # }

        email = data.get("email")
        personal = data.get("personal")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        dob = personal.get("dob")
        ssn = personal.get("ssn")
        state = personal.get("state")
        zipcode = personal.get("zipcode")
        city = personal.get("city")
        homeAddress = personal.get("homeAddress")
        mobileNumber = personal.get("mobileNumber")
        nameofbusiness = personal.get("nameofbusiness")
        businessaddress = personal.get("businessaddress")
        businessphonenumber = personal.get("businessphonenumber")
        legalstructureofbusiness = personal.get("legalstructureofbusiness")
        taxIdNumber = personal.get("taxIdNumber")
        lineofbusiness = personal.get("lineofbusiness")
        dba = personal.get("dba")
        businessType = personal.get("businessType")
        inBusinessSince = personal.get("inBusinessSince")
        website = personal.get("website")
        contactTitle = personal.get("contactTitle")
        ownershipPercent = personal.get("ownershipPercent")
        contactExt = personal.get("contactExt")
        equipDesc = personal.get("equipDesc")
        equipCost = personal.get("equipCost")
        equipYear = personal.get("equipYear")
        preferredTerm = personal.get("preferredTerm")
        reasonForUpdate = personal.get("reasonForUpdate")
        comments = personal.get("comments")
        attachment1 = personal.get("attachment1")
        attachment1Type = personal.get("attachment1Type")

        driver.get("https://afg.com/apply-for-financing/")
        random_sleep(20)

        # --------------------
        # STEP - 1
        # --------------------
        
        driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="companyNameTextBox"]', nameofbusiness)
        random_sleep(2)
        write_delay(driver, '//*[@id="dbaTextBox"]', dba)
        random_sleep(2)
        # write_delay(driver, '//*[@id="businessTypeDropDownList"]', businessType)
        
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="businessTypeDropDownList"]')
                send_click(driver, '//*[@id="businessTypeDropDownList"]/option[3]')
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="businessTypeDropDownList"]'
                # )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
                
        random_sleep(2)
        write_delay(driver, '//*[@id="inBusinessSinceTextBox"]', inBusinessSince)
        random_sleep(2)
        write_delay(driver, '//*[@id="businessNatureTextBox"]', lineofbusiness)
        random_sleep(2)
        write_delay(driver, '//*[@id="physicalAddressTextBox"]', businessaddress)
        random_sleep(2)
        write_delay(driver, '//*[@id="cityTextBox"]', city)
        random_sleep(2)
        
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="stateDropDownList"]')
                send_click(driver, '//*[@id="stateDropDownList"]/option[3]')
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="stateDropDownList"]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
                
        write_delay(driver, '//*[@id="zipTextBox"]', zipcode)

        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="stateOfIncorporationDropDownList"]')
                send_click(driver, '//*[@id="stateOfIncorporationDropDownList"]/option[3]')
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="stateOfIncorporationDropDownList"]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        
        write_delay(driver, '//*[@id="businessPhoneTextBox"]', businessphonenumber)
        random_sleep(2)
        write_delay(driver, '//*[@id="websiteTextBox"]', website)
        random_sleep(2)
        write_delay(driver, '//*[@id="taxNumberTextBox"]', taxIdNumber)
        random_sleep(2)
        send_click(driver, '//*[@id="nextButton"]')
        random_sleep(2)
        
        # --------------------
        # STEP - 2
        # --------------------
        
        write_delay(driver, '//*[@id="contact1FirstNameTextBox"]', firstName)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1LastNameTextBox"]', lastName)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1TitleTextBox"]', contactTitle)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1OwnershipTextBox"]', ownershipPercent)
        random_sleep(2)
        # write_delay(driver, '//*[@id="contact1SameBusinessAddressRadioButtonList_0"]', homeAddress)
        send_click(driver, '//*[@id="contact1SameBusinessAddressRadioButtonList_0"]')
        # random_sleep(2)
        # write_delay(driver, '//*[@id="contact1CityTextBox"]', city)
        # random_sleep(2)
        # write_delay(driver, '//*[@id="contact1CityTextBox"]', state)
        # random_sleep(2)
        # write_delay(driver, '//*[@id="contact1ZipTextBox"]', zipcode)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1CellTextBox"]', mobileNumber)
        random_sleep(2)
        # write_delay(driver, '//*[@id="contact1BusinessPhoneTextBox"]', businessphonenumber)
        # random_sleep(2)
        # write_delay(driver, '//*[@id="contact1BusinessExtTextBox"]', contactExt)
        write_delay(driver, '//*[@id="contact1EmailTextBox"]', email)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1SSNTextBox"]', ssn)
        random_sleep(2)
        write_delay(driver, '//*[@id="contact1DateOfBirthTextBox"]', dob)
        random_sleep(2)
        send_click(driver, '//*[@id="nextButton"]')
        random_sleep(2)
        
        # ------------------------
        # STEP - 3
        # ------------------------
        
        write_delay(driver, '//*[@id="equipDescTextBox"]', equipDesc)
        random_sleep(2)
        write_delay(driver, '//*[@id="equipCostTextBox"]', equipCost)
        random_sleep(2)
        write_delay(driver, '//*[@id="equipYearTextBox"]', equipYear)
        random_sleep(2)
        write_delay(driver, '//*[@id="preferredTermTextBox"]', preferredTerm)
        random_sleep(2)
        write_delay(driver, '//*[@id="reasonForAcquisitionTextBox"]', reasonForUpdate)
        random_sleep(2)
        write_delay(driver, '//*[@id="commentsTextBox"]', comments)
        random_sleep(2)
        send_click(driver, '//*[@id="confirmLabel"]')
        random_sleep(2)
        send_click(driver, '//*[@id="creditReleaseLabel"]')
        random_sleep(2)
        send_click(driver, '//*[@id="submitButton"]')

        # ------------------------
        # Page - 4
        # ------------------------
        
        # Handle attachments
        # driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="attachment1"]', attachment1)
        write_delay(driver, '//*[@id="attachment1TypeDropDownList"]', attachment1Type)

        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]')
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        full_name = data.get("preApproval").get("firstName") + " " + data.get("preApproval").get("lastName")
        card_name = "Alliance Funding Group"
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
        full_name = data.get("preApproval").get("firstName") + " " + data.get("preApproval").get("lastName")
        card_name = "Alliance Funding Group"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
