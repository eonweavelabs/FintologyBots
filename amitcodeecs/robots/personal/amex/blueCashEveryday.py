from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
from Utils.spawn_driver import start

from Utils.data_extraction import UserManager


def blueCashEveryday(driver, data, product_id):
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

        employmentTypeDict={
            "full-time":"Employed",
            "part-time":"Employed",
            "freelance": "Employed",
            "internship": "Employed"
        }

        
        driver.get('https://www.americanexpress.com/us/credit-cards/card/blue-cash-everyday/')
        random_sleep(10)
        # send_click(driver, '//a[contains(@aria-label, "Apply Now for the Blue")]')
        print("before click")
        send_click(driver, './/a[text()="Apply Now"]' ,index=-1, element=driver.find_element(by=By.XPATH, value="//div[@data-qe-id='reinforcementBanner']"))
        random_sleep(10)
        print("after click")
        # driver.find_element(By.XPATH, '//a[text()="Apply Now"]').click()
        # print(button)
        driver.find_element(by=By.XPATH, value='//input[@id="personalInfo.fullName.firstName"]').click()
        # driver.find_element(by=By.XPATH, value='//input[@id="personalInfo.fullName.firstName"]').send_keys(firstName)
        write_delay(driver, '//input[@id="personalInfo.fullName.firstName"]', UserManager.first_name())
        
        write_delay(driver, '//input[@id="personalInfo.fullName.middleName"]', UserManager.middle_name())
        
        write_delay(driver, '//input[@id="personalInfo.fullName.lastName"]', UserManager.last_name())
        
        write_delay(driver, '//input[@id="personalInfo.dateOfBirth"]', UserManager.dob())
        
        write_delay(driver, '//input[@id="personalInfo.email"]', UserManager.email())
        
        write_delay(driver, '//input[@id="personalInfo.phoneNumber.number"]', UserManager.phone())
        
        driver.execute_script("window.scrollBy(0, 100);")
        write_delay(driver, '//input[@id="personalInfo.homeAddress.streetAddress"]', UserManager.home_address())
        
        random_sleep(2)
        # write_delay(driver, '//input[@id="personalInfo.homeAddress.streetAddress"]', Keys.ENTER)
        
        
        driver.execute_script("window.scrollBy(0, 100);")
        for _ in range(len(UserManager.zipcode())+3):
            driver.find_element(By.XPATH, '//input[@id="personalInfo.homeAddress.zipCode"]').send_keys(Keys.BACK_SPACE)
            random_sleep(0.5)
        write_delay(driver, '//input[@id="personalInfo.homeAddress.zipCode"]', UserManager.zipcode())
        
        random_sleep(2)
        for _ in range(len(UserManager.city())+3):
            driver.find_element(by=By.XPATH, value='//input[@id="personalInfo.homeAddress.city"]').send_keys(Keys.BACK_SPACE)
            random_sleep(0.5)
        random_sleep(2)
        write_delay(driver, '//input[@id="personalInfo.homeAddress.city"]', UserManager.city())
        

        random_sleep(2)

        send_click(driver, '//select[@id="personalInfo.homeAddress.state"]')
        send_click(driver, f'//option[@value="{UserManager.state()}"]')

        driver.execute_script("window.scrollBy(0, 100);")

        write_delay(driver, '//input[@id="personalInfo.ssn"]', UserManager.ssn())
        
        write_delay(driver, '//input[@id="personalInfo.totalAnnualIncome"]', UserManager.household_income())
        
        driver.execute_script("window.scrollBy(0, 150);")
        random_sleep(2)
        try:send_click(driver, '//select[@id="personalInfo.incomeSource"]')
        except:
            driver.execute_script("window.scrollBy(0, 150);")
            random_sleep(2)
            send_click(driver, '//select[@id="personalInfo.incomeSource"]')
        send_click(driver, f'//option[text()="{employmentTypeDict.get(UserManager.employment_type())}"]')

        send_click(driver, '//input[@name="personalInfo.nonTaxableIncome"]')
        
        random_sleep(2)
        send_click(driver, '//button[@data-testid="continueButton"]')
        
        random_sleep(10)
        send_click(driver, '//input[@id="submit"]')
                
        
        random_sleep(60)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Amex Blue Cash Everyday.png")
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="Amex Blue Cash Everyday"
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
        card_name="Amex Blue Cash Everyday"
        
        filepath=f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        