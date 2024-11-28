from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from selenium.webdriver.common.keys import Keys

from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click

from Utils.data_extraction import UserManager
def quickSilver(driver, data, product_id):
    try:
        
        firstName=data.get("personal").get("firstName")
        middleName=data.get("personal").get("middleName")
        lastName=data.get("personal").get("lastName")
        homeAddress=data.get("personal").get("homeAddress")
        city=data.get("personal").get("city")
        state=data.get("personal").get("state")
        zipcode=data.get("personal").get("zipcode")
        mobileNumber=data.get("personal").get("mobileNumber")
        email=data.get("email")
        ssn=data.get("personal").get("ssn").replace('-', '')
        dob=data.get("personal").get("dob")
        employmentType=data.get("personal").get("employmentType")
        householdIncome=data.get("personal").get("householdIncome")
        monthlyPayment=data.get("personal").get("monthlyPayment")
        position=data.get('personal').get("position")
        housingStatus=data.get("personal").get("housingStatus")
        employmentTypeDict={
            "full-time":"FULL_TIME",
            "part-time":"PART_TIME",
            "freelance": "OTHER",
            "internship": "OTHER"
        }
        us_citizen=True
        driver.get('https://www.capitalone.com/credit-cards/quicksilver/')
        random_sleep(15)
        send_click(driver, "//a[@data-initial-value='Apply Now']")
                
        random_sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        
        write_delay(driver, '//input[@id="firstName"]', UserManager.first_name())    
        
        if(len(UserManager.middle_name())):
            write_delay(driver, '//input[@id="middleName"]', UserManager.middle_name()[0])
        write_delay(driver, '//input[@id="lastName"]', UserManager.last_name())
        write_delay(driver, '//input[@id="dateOfBirth"]', UserManager.dob())
        write_delay(driver, '//input[@id="socialSecurity"]', UserManager.ssn())
        
        if(us_citizen==True):
            send_click(driver, '//label[@for="usacitizen-radio-0"]')
            send_click(driver, '//label[@for="dualcitizen-radio-1"]')
        
        send_click(driver, "//button[text()='Continue']")
        

        random_sleep(5)
        write_delay(driver, '//input[@id="address.residential.addressLine1"]', UserManager.home_address())
        write_delay(driver, '//input[@id="address.residential.addressLine1"]', f' {UserManager.city()}', clear=False)
        
        random_sleep(5)
        
        driver.find_element(by=By.XPATH, value='//input[@id="address.residential.addressLine1"]').send_keys(Keys.DOWN)
        
        driver.find_element(by=By.XPATH, value='//input[@id="address.residential.addressLine1"]').send_keys(Keys.ENTER)
        random_sleep(2)
        write_delay(driver, '//input[@id="address.residential.zipcode"]', UserManager.zipcode())
        random_sleep(2)
        for _ in range(len(UserManager.city())+3):
            driver.find_element(by=By.XPATH, value='//input[@id="address.residential.city"]').send_keys(Keys.BACK_SPACE)
            random_sleep(0.5)
        write_delay(driver, '//input[@id="address.residential.city"]', UserManager.city())
        

        send_click(driver, '//select[@name="address.residential.state"]')
        send_click(driver, f'//option[@value="{UserManager.state()}"]')
        
        write_delay(driver, '//input[@id="email"]', UserManager.email())
        write_delay(driver, '//input[@id="phone"]', UserManager.phone())
        
        random_sleep(2)
        send_click(driver, "//button[text()='Continue']")

        random_sleep(10)
        send_click(driver, '//select[@name="employmentStatus"]')
        send_click(driver, '//option[@label="Employed"]')
        write_delay(driver, '//input[@id="occupation"]', UserManager.position())
        

       

        write_delay(driver, '//input[@id="totalAnnualIncome"]', UserManager.household_income())
        write_delay(driver, '//input[@id="monthlyRentMortgage"]', UserManager.monthly_payment())
        

        send_click(driver, '//select[@name="bankAccounts"]')
        send_click(driver, f'//option[@label="Checking And Savings"]')
        random_sleep(2)
        send_click(driver, "//button[text()='Continue']")
        random_sleep(10)

        send_click(driver, "//button[text()='Continue']")
        random_sleep(10)
        if("Make sure your information looks right" in driver.page_source):
            send_click(driver, "//button[text()='Continue']")
            
        random_sleep(10)
        if("Additional Information" in driver.page_source):
            send_click(driver, '//label[@for="paperlessConsent"]')
            send_click(driver, "//button[text()='Continue']")
            random_sleep(2)
            send_click(driver, '//button[text()="Submit Application"]')
            random_sleep(30)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Capital One Quick Silver.png")
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="Capital One Quick Silver"
        filepath=f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        
    except Exception as e:
        input("Error in application")
        print(e)
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="Capital One Quick Silver"
        
        filepath=f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        