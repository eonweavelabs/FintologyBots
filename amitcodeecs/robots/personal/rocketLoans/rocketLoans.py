from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Rocket Loans
# -----------------------------------------------------

def rocketLoans(driver, data, product_id):
    try:
        # data = {
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
        #         "equipmentPrice": 20000,
        #         "vendorName": "vendorName",
        #         "securityword": "Fluffy"
        #     }
        # }
        
        email = data.get("email")
        personal = data.get("personal")
        citizenship = personal.get("citizenship")
        firstName = personal.get("firstName")
        middleName = personal.get("middleName")
        lastName = personal.get("lastName")
        dob = personal.get("dob")
        ssn = personal.get("ssn")
        membership = personal.get("membership")
        housingStatus = personal.get("housingStatus")
        grossIncome = personal.get("grossIncome")
        mobileNumber = personal.get("mobileNumber")
        rent = personal.get("rent")
        employmentType = personal.get("employmentType")
        state = personal.get("state")
        zipcode = personal.get("zipcode")
        city = personal.get("city")
        homeAddress = personal.get("homeAddress")
        motherMaidenName = personal.get("motherMaidenName")
        nameofbusiness = personal.get("nameofbusiness")
        businessaddress = personal.get("businessaddress")
        businessphonenumber = personal.get("businessphonenumber")
        businessStartDate = personal.get("businessStartDate")
        date = personal.get("date")
        legalstructureofbusiness = personal.get("legalstructureofbusiness")
        typeoffinancialinstitute = personal.get("typeoffinancialinstitute")
        taxIdNumber = personal.get("taxIdNumber")
        lineofbusiness = personal.get("lineofbusiness")
        numberofemployees = personal.get("numberofemployees")
        yearinbusiness = personal.get("yearinbusiness")
        countryofbusinessformation = personal.get("countryofbusinessformation")
        securitywordhint = personal.get("securitywordhint")
        securityword = personal.get("securityword")
        vendorName = personal.get("vendorName")
        equipmentPrice = personal.get("equipmentPrice")

        driver.get(
            "https://www.rocketloans.com/"
        )
        random_sleep(20)
        driver.switch_to.frame(0)
        
        # Select Language
        # select_element = driver.find_element(by=By.XPATH, value='//*[@id=":0.targetLanguage"]/select')
        # select = Select(select_element)
        # select.select_by_value('en')

        # Company Name
        write_delay(driver, '//*[@id="tfa_1"]', nameofbusiness)
        random_sleep(2)
        
        # DBA
        write_delay(driver, '//*[@id="tfa_2"]', nameofbusiness)
        random_sleep(2)
        
        # Fed Tax ID
        write_delay(driver, '//*[@id="tfa_20"]', taxIdNumber)
        random_sleep(2)
        
        # Business Phone
        write_delay(driver, '//*[@id="tfa_811"]', businessphonenumber)
        random_sleep(2)
        
        # Entity Type
        write_delay(driver, '//*[@id="tfa_10"]', legalstructureofbusiness)
        random_sleep(2)
        
        # Industry
        write_delay(driver, '//*[@id="tfa_21"]', lineofbusiness)
        random_sleep(2)
        
        # Physical Address
        write_delay(driver, '//*[@id="tfa_22"]', businessaddress)
        random_sleep(2)
        
        # Physical City
        write_delay(driver, '//*[@id="tfa_23"]', city)
        random_sleep(2)
        
        # Physical state
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_171"]')
        select = Select(select_element)
        select.select_by_value(state)

        # Physical ZIP/Postal Code
        write_delay(driver, '//*[@id="tfa_25"]', zipcode)
        random_sleep(2)
        
        # Mailing Address
        send_click(driver, '//*[@id="tfa_921-L"]')
        random_sleep(2)
        # write_delay(driver, '//*[@id="tfa_981"]', homeAddress)

        # Mailing City
        # write_delay(driver, '//*[@id="tfa_982"]', city)

        # Mailing State
        # select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_984"]')
        # select = Select(select_element)
        # select.select_by_value(state)

        # Mailing ZIP/Postal Code
        # write_delay(driver, '//*[@id="tfa_986"]', zipcode)

        # State of Inc
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_26"]')
        select = Select(select_element)
        select.select_by_value(state)
        random_sleep(2)
        
        # Business Start Date
        write_delay(driver, '//*[@id="tfa_27"]', businessStartDate)
        random_sleep(2)
        
        # Estimated annual revenue
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_334"]')
        select = Select(select_element)
        select.select_by_value("tfa_629")
        random_sleep(2)
        # write_delay(driver, '//*[@id="tfa_334"]', grossIncome)

        # Net profit for last year
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_336"]')
        select = Select(select_element)
        select.select_by_value("tfa_639")
        random_sleep(2)
        # write_delay(driver, '//*[@id="tfa_336"]', grossIncome)

        # Business finance request
        # financeRequest = personal.get("financeRequest")
        # write_delay(driver, '//*[@id="tfa_782"]', financeRequest)
        random_sleep(2)
        # Equipment Description
        equipmentDescription = personal.get("equipmentDescription")
        write_delay(driver, '//*[@id="tfa_234"]', equipmentDescription)
        random_sleep(2)
        # Equipment Condition
        write_delay(driver, '//*[@id="tfa_765"]', "New")
        random_sleep(2)
        # Equipment price
        write_delay(driver, '//*[@id="tfa_236"]', equipmentPrice)
        random_sleep(2)
        # Equipment Vendor
        # write_delay(driver, '//*[@id="tfa_238"]', vendorName)
        random_sleep(2)
        # NEXT PAGE
        send_click(driver, '//*[@id="wfPgIndex-1-buttons"]')
        random_sleep(2)

        # ------------------
        # Page - 2
        # ------------------
        
        # First Name
        write_delay(driver, '//*[@id="tfa_42"]', firstName)
        random_sleep(2)
        # Middle Name
        write_delay(driver, '//*[@id="tfa_999"]', middleName)
        random_sleep(2)
        # Last Name
        write_delay(driver, '//*[@id="tfa_43"]', lastName)
        random_sleep(2)
        
        # Suffix
        # write_delay(driver, '//*[@id="tfa_1000"]', "")
        random_sleep(2)
        # Email Address
        write_delay(driver, '//*[@id="tfa_342"]', email)
        random_sleep(2)
        # Mobile Phone
        write_delay(driver, '//*[@id="tfa_344"]', mobileNumber)
        random_sleep(2)
        # Title
        write_delay(driver, '//*[@id="tfa_769"]', "Owner")

        # Preferred Method of Contact
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_47"]')
        select = Select(select_element)
        select.select_by_value('tfa_49')
        random_sleep(2)
        
        # Same address
        send_click(driver, '//*[@id="tfa_646-L"]')
        
        # Home Address
        # write_delay(driver, '//*[@id="tfa_708"]', homeAddress)

        # Home City
        # write_delay(driver, '//*[@id="tfa_709"]', city)

        # Home State
        # select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_710"]')
        # select = Select(select_element)
        # select.select_by_value(state)

        # Home ZIP Code
        # write_delay(driver, '//*[@id="tfa_762"]', zipcode)

        # Social Security Number
        write_delay(driver, '//*[@id="tfa_44"]', ssn)
        random_sleep(2)
        # Date of Birth
        write_delay(driver, '//*[@id="tfa_231"]', dob)
        random_sleep(2)
        # Ownership%
        write_delay(driver, '//*[@id="tfa_45"]', 100)
        random_sleep(2)
        # Do you have additional guarantors?
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_424"]')
        select = Select(select_element)
        select.select_by_value('tfa_426')

        # NEXT PAGE
        send_click(driver, '//*[@id="wfPageNextId2"]')
        random_sleep(2)
        
        # ------------------
        # Page - 3
        # ------------------

        # How will this additional equipment be used?
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_239"]')
        select = Select(select_element)
        select.select_by_value('tfa_241')
        random_sleep(2)
        # write_delay(driver, '//*[@id="tfa_239"]', "Usage details")

        # How many employees do you have?
        write_delay(driver, '//*[@id="tfa_328"]', numberofemployees)
        random_sleep(2)
        # Current fleet size in operation for this company?
        write_delay(driver, '//*[@id="tfa_252"]', 10)
        random_sleep(2)
        
        # Do you have any tax liens?
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_337"]')
        select = Select(select_element)
        select.select_by_value('tfa_340')

        # Have you ever filed for bankruptcy?
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_620"]')
        select = Select(select_element)
        select.select_by_value('tfa_623')

        # Bank Statement
        # write_delay(driver, '//*[@id="tfa_356"]', "Bank statement details")

        # Driver License
        # write_delay(driver, '//*[@id="tfa_783"]', "Driver license details")

        # How did you hear about us?
        # write_delay(driver, '//*[@id="tfa_357"]', "Referral")
        select_element = driver.find_element(by=By.XPATH, value='//*[@id="tfa_357"]')
        select = Select(select_element)
        select.select_by_value('tfa_363')

        # Promo Code
        # write_delay(driver, '//*[@id="tfa_764"]', "PROMO123")

        # Full Name here
        write_delay(driver, '//*[@id="tfa_792"]', firstName + " " + lastName)

        # Date
        # write_delay(driver, '//*[@id="tfa_812"]', date)
        send_click(driver, '//*[@id="tfa_812"]')

        # I'm not a robot
        # send_click(driver, '//*[@id="recaptcha-anchor"]')
        random_sleep(2)

        # SUBMIT
        send_click(driver, '//*[@id="submit_button"]')
        random_sleep(10)
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]')
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        full_name = firstName + " " + lastName
        card_name = "Rocket Loans"
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
        full_name = firstName + " " + lastName
        card_name = "Rocket Loans"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
