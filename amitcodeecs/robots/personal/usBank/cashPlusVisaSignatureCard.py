from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Us Bank Cash Plus Visa Signature Card
# -----------------------------------------------------------------

def cashPlusVisaSignatureCard(driver,data, product_id):
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
        #         "monthlymortage": 546,
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "occupation": "Test",
        #         "employmentType": "full-time",
        #         "bankAccount": "checking-and-savings",
        #         "state": 'DC',
        #         "zipcode": 20500,
        #         "city": "Washington",
        #         "homeAddress": "1600 Pennsylvania Avenue NW",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://onboarding.usbank.com/consumer/cards/WRH8D23H2R/8069/86937/start"
        )
        # send_click(
        #     driver, 
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)

        # citizenship = data.get("personal").get("citizenship")
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        bonvoyNumber = data.get("personal").get("bonvoyNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        grossIncome = data.get("personal").get("householdIncome")
        monthlymortage = data.get("personal").get("monthlyPayment")
        bankAccount = data.get("personal").get("bankAccount")
        occupation = data.get("personal").get("position")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMP",
            "part-time": "EMP",
            "freelance": "EMP",
            "internship": "EMP",
        }
        
        bankAccountDist = {
            "checking-and-savings": "CAS",
            "checking": "CHK",
            "savings": "SAV",
            "neither": "NON",
        }
        
        random_sleep(20)
        
        # Apply manually
        # send_click(
        #     driver, 
        #     '/html/body/div[3]/div/div/main/div/div/div/div[2]/div/div[1]/button'
        # )
        # random_sleep(2)
        
        # Page 1: Personal Info
        write_delay(driver, '//*[@id="input_firstName"]', firstName)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_lastName"]', lastName)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_email"]', email)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_phoneNumber"]', mobileNumber)
        random_sleep(1)
        
        send_click(driver, '//*[@id="app"]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        random_sleep(3)

        # Page 2: Address and SSN
        write_delay(driver, '//*[@id="input_dob"]', dob)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_ssn"]', ssn)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_address1"]', homeAddress)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_zipCode"]', zipcode)
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_city"]', city)
        random_sleep(1)
        
        send_click(driver, '//*[@id="select_state"]')
        random_sleep(1)
        
        # Assuming you have some logic to select the state dropdown
        # Replace with actual logic for selecting the state value
        send_click(driver, f"//option[@value='{state}']")
        random_sleep(1)
        
        write_delay(driver, '//*[@id="input_housingPayment"]', str(monthlymortage))
        random_sleep(1)
        
        send_click(driver, '//*[@id="identity"]/div[5]/button')
        random_sleep(3)

        # Page 3: Annual Income and Employment Info
        write_delay(driver, '//*[@id="input_totalAnnualIncome"]', str(grossIncome))
        random_sleep(1)
        
        # Employment type
        send_click(driver, '//*[@id="select_sourceOfAnnualIncome"]')
        random_sleep(1)
        
        # Logic to select primary source of income (replace with actual selection logic)
        send_click(driver, f"//option[@value='{'FULLTIME'}']")
        random_sleep(1)
        
        # Occupation
        send_click(driver, '//*[@id="select_occupation"]')
        random_sleep(1)
        
        # Logic to select
        send_click(driver, f"//option[@value='{'CEO'}']")
        random_sleep(1)
        
        send_click(driver, '//*[@id="aml"]/div[3]/button')
        random_sleep(3)

        # Page 4: Authorized User
        send_click(driver, '//*[@id="preBalanceTransferChoice2"]')  # Selecting 'No'
        random_sleep(1)
        
        send_click(driver, '//*[@id="bt-presubmit-form"]/div[4]/button')
        random_sleep(3)
        
        # Page 4: Authorized User
        send_click(driver, '//*[@id="addAuthorizedUserChoice2"]')  # Selecting 'No'
        random_sleep(1)
        
        send_click(driver, '//*[@id="authorized-user"]/div[3]/button')
        random_sleep(3)

        # Page 5: Continue without filling (assuming no additional fields)
        send_click(driver, '//*[@id="usb-button-continue"]/button')
        random_sleep(3)

        # Page 6: Final Submission
        send_click(driver, '//*[@id="btn-submit-large"]')  # Submitting the form
       
        random_sleep(1)
        random_sleep(10)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Us Bank Cash Plus Visa Signature Card"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        # product_id = "661cb8fd5418a96c1c8c25f5"    
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Us Bank Cash Plus Visa Signature Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

