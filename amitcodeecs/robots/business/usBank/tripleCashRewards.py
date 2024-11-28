from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from selenium.webdriver.support.select import Select
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click

from Utils.data_extraction import UserManager
def tripleCashRewards(driver, data, product_id):
    try:
        
        driver.get(
            "https://www.usbank.com/business-banking/business-credit-cards/business-triple-cash-back-credit-card.html")
        counter=0
        while counter<11:
            try:
                
                url=driver.find_element(by=By.XPATH, value='//a[contains(@aria-label, "Apply for U.S. Bank Triple Cash Rewards Visa® Business Card")]').get_attribute("href")
                driver.get(url)
                random_sleep(8)
                break
            except Exception as e:
                random_sleep(2)
                counter+=1
                print(e)
    
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
        mobileNumber = data.get("personal").get("mobileNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        grossIncome = data.get("personal").get("householdIncome")


        numberOfEmployees = data.get("business").get("numberOfEmployees")
        occupation = data.get("personal").get("position")
        employer = data.get("personal").get("currentEmployer")
        income = data.get("personal").get("householdIncome")
        business_legal_name = data.get("business").get("businessName")
        numberOfEmployees = data.get("business").get("numberOfEmployees")
        business_grossSales = data.get("business").get("grossSales")
        einNumber = data.get("business").get("einNumber")
        businessAddress = data.get("business").get("businessAddress")
        businessZipcode = data.get("business").get("businessZipcode")
        businessEmail = data.get("business").get("businessEmail")
        businessCity = data.get("business").get("businessCity")
        businessState = data.get("business").get("businessState")
        businessPhone = data.get("business").get("businessPhone")
        dateBusinessCommenced = data.get("business").get("dateBusinessCommenced")
        entity=data.get("business").get("entity")
        title=data.get("business").get("title")
        businessPercent=data.get('business').get('businessPercent')

        industryType=data.get('business').get('industryType')
        entityDict={
            "llc":"LLC",
            "corporation": "CORP",
            "partnership": "PARTNER",
            "sole-prop": "SLP",
            "Non-Profit": "NONPROF"
        }
        titleDict={
            "ceo": "chief-executive-officer",
            "member": "managing-member",
            "owner": "owner"
        }

        naicsIndustryLegendDict={
            "business-consulting": "541611 - Administrative Management and General Management Consulting Services",
            "marketing": "541613 - Marketing Consulting Services",
            "education-support-services": "611710 - Educational Support Services",
            "administration": "923130 - Administration of Human Resource Programs (except Education, Public Health, and Veterans' Affairs Programs)",
            "software-saas":"541690 - Other Scientific and Technical Consulting Services",
            "construction-or-real-estate": "531390 - Other Activities Related to Real Estate"
        }
        business_grossSales="450000"
        # if not firstName or not lastName or not dob or not motherMaidenName or not ssn or not homeAddress or not city or not zipcode or not state or not email or not mobileNumber or not residencyStatus or not grossIncome or not occupation or not employer or not income or not business_legal_name or not numberOfEmployees or not business_grossSales or not einNumber or not businessAddress or not businessZipcode or not businessEmail or not businessCity or not businessState or not businessPhone:
        #     raise Exception("Missing personal data.")
        random_sleep(15)

        sleepcount=1
        while sleepcount<1000:
            if(sleepcount%250==0):
                driver.refresh()
            try:
                driver.find_element(by=By.XPATH, value="//select[@id='select_businessType']")
                random_sleep(1)
                driver.find_element(by=By.XPATH, value="//select[@id='select_businessType']").click()
                break
            except:
                random_sleep(0.1)
                sleepcount+=1

        random_sleep(5)
        send_click(driver, f"//option[@value='{entityDict.get(UserManager.business_entity())}']")
        random_sleep(1)
        write_delay(driver, '#input_taxIdentifier', UserManager.ein_number())

        random_sleep(1)
        write_delay(driver,  '#input_legalBusinessname', UserManager.business_name().replace("&", ""))

        random_sleep(1)

        write_delay(driver, '#input_businessNameOnCard', UserManager.business_name().replace("&", ""))
        random_sleep(1)
        Select(driver.find_element(By.CSS_SELECTOR,'#select_countryOfFormation')).select_by_index(1)

        random_sleep(1)
        year = UserManager.date_business_commenced().split("-")[0]
        write_delay(driver, '#input_dateOfEstablishment', year)

        random_sleep(1)
        write_delay(driver, '//*[@id="input_email"]', UserManager.email())

        random_sleep(1)
        write_delay(driver, '//*[@id="input_phoneNumber"]', UserManager.phone())

        random_sleep(1)
        write_delay(driver, '//input[@id="input_businessPhoneNumber"]', UserManager.business_phone())


        random_sleep(1)
        write_delay(driver, '//input[@id="input_grossAnnualSales"]', UserManager.gross_sales())

        send_click(driver , "//button[@id='primary-large']")

        random_sleep(15)

        # input("ruk jaooo first page")



        
        
        random_sleep(1)
        random_sleep(1)
        
        
        
        
        
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        random_sleep(5)
        while True:
            try:
                driver.find_element(by=By.CSS_SELECTOR, value="#input_business-address-collectionaddress1")
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)
        

        
        random_sleep(5)
        write_delay(driver, '#input_business-address-collectionaddress1', UserManager.business_address())
        
        random_sleep(1)
        
        
        random_sleep(3)
        driver.execute_script("window.scrollBy(0,200)")
        random_sleep(2)
        send_click(driver, "//select[@id='select_business-address-collectionstate']")
        random_sleep(1)
        driver.find_element(by=By.XPATH, value="//select[@id='select_business-address-collectionstate']").find_element(by=By.XPATH, value=f".//option[@value='{UserManager.business_state()}']").click()
        random_sleep(1)
        
        random_sleep(1)
        write_delay(driver, '#input_business-address-collectionzipCode', UserManager.business_zipcode())
        random_sleep(1)
        driver.find_element(by=By.CSS_SELECTOR, value='#input_business-address-collectioncity').clear()
        random_sleep(2)
        write_delay(driver, '#input_business-address-collectioncity', UserManager.business_city())

        random_sleep(1)
        # random_sleep(1)
        # send_click(driver, "//input[@id='input_businessAddressaddress2']")
        
        random_sleep(2)
        
        send_click(driver, "//button[text()='Save & continue']")
        random_sleep(4)

        # input("stop2 second page ruk jao")
        while "What industry most closely fits your business?" not in driver.page_source:
            send_click(driver, "//button[text()='Save & continue']")
            random_sleep(2)
        write_delay(driver, '//input[@name="businessIndustry"]', naicsIndustryLegendDict.get(UserManager.industry_type()))
        random_sleep(1)
        send_click(driver , "//span[@class='search__list-item-btn-splitter']")

        random_sleep(1)
        send_click(driver, '//button[@aria-label="Save & continue"]')
        
        random_sleep(2)
        
        
        while True:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="input_firstName"]')
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)
                
        write_delay(driver, '//*[@id="input_firstName"]', UserManager.first_name())
        
        random_sleep(1)
        write_delay(driver, '//*[@id="input_lastName"]', UserManager.last_name())
        
        
        
        
        
        random_sleep(1)
        
        random_sleep(2)
        
        while True:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="input_dateOfBirth"]')
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)
                
        write_delay(driver, '//*[@id="input_dateOfBirth"]', UserManager.dob())
        
        random_sleep(1)
        write_delay(driver, '//*[@id="input_ssn"]', UserManager.ssn())
        
        random_sleep(1)
        if(UserManager.home_address()==UserManager.business_address()):
            send_click(driver, '//*[@id="input_address-checkbox"]')
        else:
            random_sleep(2)
            write_delay(driver, '//input[@id="input_address-collection-inputaddress1"]', UserManager.home_address())
            
            driver.find_element(by=By.XPATH, value='//input[@id="input_address-collection-inputcity"]').clear()
            random_sleep(2)
            write_delay(driver, '//input[@id="input_address-collection-inputcity"]', UserManager.city())
            
            
            random_sleep(3)
            driver.execute_script("window.scrollBy(0,300)")
            random_sleep(2)
            send_click(driver, "//select[@id='select_address-collection-inputstate']")
            random_sleep(1)
            driver.find_element(by=By.XPATH, value="//select[@id='select_address-collection-inputstate']").find_element(by=By.XPATH, value=f".//option[@value='{UserManager.state()}']").click()
            random_sleep(1)
            write_delay(driver, '//input[@id="input_address-collection-inputzipCode"]', UserManager.zipcode())
            random_sleep(5)
            

        write_delay(driver, '//*[@id="input_annualIncome"]', UserManager.household_income())
        
        random_sleep(1)
        
        random_sleep(1)
        
        random_sleep(5)
        

        while True:
            try:
                driver.find_element(by=By.XPATH, value="//select[@id='select_businessOwnerType']")
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)
                
        
        send_click(driver, "//select[@id='select_businessOwnerType']")
        random_sleep(1)
        driver.find_element(by=By.XPATH, value="//select[@id='select_businessOwnerType']").find_element(by=By.XPATH, value=f".//option[@value='{titleDict.get(UserManager.business_title())}']").click()
        random_sleep(1)
        random_sleep(1)
        if(UserManager.business_percent()=="100"):
            send_click(driver, '//*[@id="isSoleOwnerChoice1"]')
        else:
            send_click(driver, '//*[@id="isSoleOwnerChoice2"]')
            write_delay(driver, '//input[@id="input_primaryBizOwnerShipPercentage"]', UserManager.business_percent())
            random_sleep(2)
            send_click(driver, "//button[text()='Save & continue']")
            random_sleep(5)
            if(int(UserManager.business_percent())<=75):
                send_click(driver, "//input[@id='coOwnerPercentageChoice2']")

        
        while True:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="addEmployeeCardsChoice2"]')
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)
                
    
        
        send_click(driver, '//*[@id="addEmployeeCardsChoice2"]')
        random_sleep(1)
        
        random_sleep(5)
        while True:
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="billingOptionTypeChoice1"]')
                break
            except:
                send_click(driver, "//button[text()='Save & continue']")
                random_sleep(5)

        random_sleep(2)  
    
        send_click(driver, '//*[@id="billingOptionTypeChoice1"]')
        random_sleep(1)
        
        random_sleep(5)

        
        send_click(driver, "//button[text()='Save & continue']")
        
        random_sleep(4)

        send_click(driver , "//input[@id='prebt-radio-groupChoice2']")
        random_sleep(2)
        
        send_click(driver, "//button[text()='Save & continue']")
        
        
        random_sleep(10)
        send_click(driver, "//button[text()='Save & continue']")
        random_sleep(10)
        send_click(driver, "//button[text()='Accept terms & submit']")
        
        
        random_sleep(20)
        
        random_sleep(20)
        
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="US Bank Triple Cash Rewards"
        filepath=f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        
    except Exception as e:
        input("Error in application")
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="US Bank Triple Cash Rewards"
        print(e)
        
        filepath=f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        