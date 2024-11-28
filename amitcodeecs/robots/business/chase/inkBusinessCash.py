from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from random import randint

from Utils.data_extraction import UserManager

from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
from time import sleep


def inkBusinessCash(driver, data, product_id):
    try:
        
        driver.get("https://creditcards.chase.com/business-credit-cards/ink/cash")
        retry_counter=0
        while retry_counter<600:
            try:
                
                url=driver.find_element(by=By.XPATH, value='//a[contains(@data-id, "ApplyNow")]').get_attribute("href")
                driver.get(url)
                random_sleep(3)
                driver.switch_to.window(driver.window_handles[-1])
                break
            except:
                sleep(0.1)
                retry_counter+=1
        wait = WebDriverWait(driver, 100)
        # firstName = data.get("personal").get("firstName")
        # middleName = data.get("personal").get("middleName")
        # lastName = data.get("personal").get("lastName")
        # dob = data.get("personal").get("dob")
        # motherMaidenName = data.get("personal").get("motherMaidenName")
        # ssn = data.get("personal").get("ssn")
        # homeAddress = data.get("personal").get("homeAddress")
        # city = data.get("personal").get("city")
        # zipcode = data.get("personal").get("zipcode")
        # state = data.get("personal").get("state")
        # email = data.get("email")
        # mobileNumber = data.get("personal").get("mobileNumber")
        # residencyStatus = data.get("personal").get("housingStatus")
        # householdIncome = data.get("personal").get("householdIncome")
        # numberOfEmployees = data.get("business").get("numberOfEmployees")
        # occupation = data.get("personal").get("position")
        # employer = data.get("personal").get("currentEmployer")
        # householdIncome = data.get("personal").get("householdIncome")
        # business_legal_name = data.get("business").get("businessName")
        # numberOfEmployees = data.get("business").get("numberOfEmployees")
        # business_grossSales = data.get("business").get("grossSales")
        # einNumber = data.get("business").get("einNumber")
        # businessAddress = data.get("business").get("businessAddress")
        # businessZipcode = data.get("business").get("businessZipcode")
        # businessEmail = data.get("business").get("businessEmail")
        # businessCity = data.get("business").get("businessCity")
        # businessState = data.get("business").get("businessState")
        # businessPhone = data.get("business").get("businessPhone")
        # # businessPhone = data.get("personal").get("mobileNumber")        ########################
        # dateBusinessCommenced = data.get("business").get("dateBusinessCommenced")
        # title=data.get("business").get("title")
        # entity=data.get("business").get("entity")
        # monthlySpend=data.get("business").get("monthlySpend")
        # industryType=data.get("business").get("industryType")
        # businessPercent=str(data.get("business").get("businessPercent"))
        titleDict={
            "ceo": "PRESIDENT",
            "owner": "OWNER",
            "partner": "PARTNER",
            "member" : "MEMBER",
        }
        entityDict={
            "llc": "LIMITED_LIABILITY",
            "corporation": "CORPORATION",
            "partnership": "PARTNERSHIP",
            "sole proprietorship": "SOLE_PROPRIETORSHIP"
        }

        businessCategoryDict={
            "business-consulting": "Professional, Scientific, Tech Services",
            "marketing": "Professional, Scientific, Tech Services",
            "software-saas": "Professional, Scientific, Tech Services",
            "education-support-services": "Educational Services",
            "administration": "Public Administration",
            "construction-or-real-estate": "Real Estate and Rental and Leasing"
        }

        businessTypeDict={
            "business-consulting": "Mgmt, Scientific & Tech Consulting Svcs",
            "marketing": "Mgmt, Scientific & Tech Consulting Svcs",
            "software-saas": "Mgmt, Scientific & Tech Consulting Svcs",
            "education-support-services": "Educational Support Services",
            "administration": "Admin of Human Resources Programs",
            "construction-or-real-estate": "Activities Related to Real Estate"
        }

        businessSubTypeDict={
            "business-consulting": "Admin & General Mgt Consulting Services",
            "marketing": "Marketing Consulting Services",
            "software-saas": "Other Scientific & Tech Consulting Svcs",
            "education-support-services": "Educational Support Services",
            "administration": "Administration of Education Programs",
            "construction-or-real-estate": "Other Activities Related to Real Estate"
        }

        
        

        # if not firstName or not lastName or not dob or not motherMaidenName or not ssn or not homeAddress or not city or not zipcode or not state or not email or not mobileNumber or not residencyStatus or not householdIncome or not occupation or not householdIncome or not business_legal_name or not numberOfEmployees or not business_grossSales or not einNumber or not businessAddress or not businessZipcode or not businessEmail or not businessCity or not businessState or not businessPhone:
        #     raise Exception("Missing personal data.")

        # Select(driver.find_element(By.ID,
        #        "#select-authorizingOfficerTitle-select-validate")).select_by_index(1)
        random_sleep(15)
        sleepcount=1
        while sleepcount<1000:
            if(sleepcount%250==0):
                driver.refresh()
            try:
                driver.find_element(by=By.XPATH, value='//select[@id="select-authorizingOfficerTitle-select-validate"]').click()
                break
            except:
                random_sleep(0.1)
                sleepcount+=1


        random_sleep(10)
        driver.find_element(by=By.XPATH, value='//select[@id="select-authorizingOfficerTitle-select-validate"]').click()
        random_sleep(2)
        tempdropdown=driver.find_element(by=By.XPATH, value='//select[@id="select-authorizingOfficerTitle-select-validate"]').find_elements(by=By.TAG_NAME, value="option")
        for temptitle in tempdropdown:
            if(titleDict.get(UserManager.business_title()).lower() in temptitle.text.lower()):
                temptitle.click()
                break

        
        random_sleep(2)
        write_delay(driver,"#blx-nameBlock-firstName-text-validate-input-field", UserManager.first_name())
        random_sleep(1)
        if "middleName" in data.get("personal", {}):
            write_delay(driver,"#blx-nameBlock-middleName-text-validate-input-field", UserManager.middle_name())
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
        write_delay(driver,"#blx-nameBlock-lastName-text-validate-input-field", UserManager.last_name())
        random_sleep(1)
        write_delay(driver, "#dateOfBirth-text-validate-input-field", UserManager.dob())
        
        random_sleep(1)
        write_delay(driver, "#mothersMaidenName-text-validate-input-field", UserManager.mother_maiden_name())
        
        random_sleep(1)
        write_delay(driver, "#maskedSocialSecurityNumber-text-validate-input-field", UserManager.ssn())
        
        random_sleep(1)
        write_delay(driver, "#streetAddress-blx-residentialAddressBlock-text-validate-input-field", UserManager.home_address())
        
        random_sleep(1)
        write_delay(driver, "#zipCode-blx-residentialAddressBlock-text-validate-input-field", UserManager.zipcode())
        
        random_sleep(1)
        for _ in range(len(UserManager.city())+3):
            driver.find_element(by=By.CSS_SELECTOR, value="#city-blx-residentialAddressBlock-text-validate-input-field").send_keys(Keys.BACK_SPACE)
            random_sleep(0.5)
        write_delay(driver, "#city-blx-residentialAddressBlock-text-validate-input-field", UserManager.city())
        
        random_sleep(1)
        
        driver.find_element(by=By.XPATH, value="//select[@id='select-state-blx-residentialAddressBlock-select-validate']").click()
        driver.find_element(by=By.XPATH, value="//select[@id='select-state-blx-residentialAddressBlock-select-validate']").find_element(by=By.XPATH, value=f".//option[@value='{UserManager.state()}']").click()
        random_sleep(1)
        write_delay(driver, "#emailAddressId-text-validate-input-field", UserManager.email())
        
        random_sleep(1)
        write_delay(driver, "#phoneNumberId-text-validate-input-field", UserManager.phone())
        
        random_sleep(1)
        write_delay(driver, "#grossAnnualIncome-text-validate-input-field", UserManager.household_income())
        
        random_sleep(1)
        driver.find_element(by=By.XPATH, value="//select[@id='select-businessStructureId-select-validate']").click()
        random_sleep(1)
        driver.find_element(by=By.XPATH, value=f"//option[@value='{entityDict.get(UserManager.business_entity())}']").click()
        random_sleep(1)
        write_delay(driver, "#businessLegalName-text-validate-input-field", UserManager.business_name())
        
        random_sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="input-alternateIdentificationOptionId-1"]').click()
        random_sleep(1)
        write_delay(driver, "#socialSecurityNumber-text-validate-input-field", UserManager.ein_number())
        
        random_sleep(1)
        if(UserManager.home_address()==UserManager.business_address()):

            driver.find_element(By.CSS_SELECTOR, "#input-businessAddressSameAsPersonalId-0").click()
        else:
            driver.find_element(By.CSS_SELECTOR, "#input-businessAddressSameAsPersonalId-1").click()
            random_sleep(1)
            write_delay(driver, "#streetAddress-businessPrimaryAddressMultiTypeBlock-text-validate-input-field", UserManager.business_address())
            
            random_sleep(1)
            write_delay(driver, "#zipCode-businessPrimaryAddressMultiTypeBlock-text-validate-input-field", UserManager.business_zipcode())
            
            random_sleep(1)
            for _ in range(len(UserManager.business_city())+3):
                driver.find_element(by=By.CSS_SELECTOR, value="#city-businessPrimaryAddressMultiTypeBlock-text-validate-input-field").send_keys(Keys.BACK_SPACE)
                random_sleep(0.5)
            write_delay(driver, "#city-businessPrimaryAddressMultiTypeBlock-text-validate-input-field", UserManager.business_city())
            
            random_sleep(1)
            
            driver.find_element(by=By.XPATH, value="//select[@id='select-state-businessPrimaryAddressMultiTypeBlock-select-validate']").click()
            driver.find_element(by=By.XPATH, value="//select[@id='select-state-businessPrimaryAddressMultiTypeBlock-select-validate']").find_element(by=By.XPATH, value=f".//option[@value='{UserManager.business_state()}']").click()
        random_sleep(1)
        
        write_delay(driver, "#numberOfEmployees-text-validate-input-field", UserManager.number_of_employees())
        
        random_sleep(1)
        write_delay(driver, "#phoneNumber-text-validate-input-field", UserManager.business_phone())
        
        random_sleep(1)
        dateBusinessCommenced=UserManager.date_business_commenced().split('-')
        dateBusinessCommenced=dateBusinessCommenced[1]+dateBusinessCommenced[0]
        write_delay(driver, "#dateOfEstablishment-text-validate-input-field", dateBusinessCommenced)
        
        random_sleep(1)
        write_delay(driver, "#annualRevenue-text-validate-input-field", UserManager.gross_sales())
        
        random_sleep(3)

        send_click(driver,'#select-businessCategoryId-select-validate')
        random_sleep(1)
        print(businessCategoryDict.get(UserManager.industry_type()))
        driver.find_element(by=By.CSS_SELECTOR, value='#select-businessCategoryId-select-validate').find_element(by=By.XPATH, value=f'//option[text()="{businessCategoryDict.get(UserManager.industry_type())}"]').click()
        random_sleep(4)
        driver.find_element(by=By.CSS_SELECTOR, value='#select-businessSubCategoryId-select-validate').click()
        random_sleep(1)
        print(businessTypeDict.get(UserManager.industry_type()))
        driver.find_element(by=By.CSS_SELECTOR, value='#select-businessSubCategoryId-select-validate').find_element(by=By.XPATH, value=f'//option[text()="{businessTypeDict.get(UserManager.industry_type())}"]').click()
        random_sleep(4)
        driver.find_element(by=By.CSS_SELECTOR, value='#select-businessSubTypeId-select-validate').click()
        random_sleep(1)
        print(businessSubTypeDict.get(UserManager.industry_type()))
        driver.find_element(by=By.CSS_SELECTOR, value='#select-businessSubTypeId-select-validate').find_element(by=By.XPATH, value=f'//option[text()="{businessSubTypeDict.get(UserManager.industry_type())}"]').click()
        random_sleep(3)
        write_delay(driver, "#estimatedMonthlySpending-text-validate-input-field", UserManager.monthly_spend())
        
        random_sleep(1)
        write_delay(driver, '//*[@id="ownershipPercentage-text-validate-input-field"]', UserManager.business_percent())
        random_sleep(1)
        # write_delay(driver, '//*[@id="ownershipPercentage-text-validate-input-field"]', Keys.TAB)
        random_sleep(1)
        try:
            driver.find_element(By.XPATH, '//*[@id="input-additionalBeneficiaryOwnersHeader-radio-1"]')
            random_sleep(1)
            driver.find_element(By.XPATH, '//*[@id="input-additionalBeneficiaryOwnersHeader-radio-1"]').click()
        except: pass
        random_sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#input-navigationAdvisory").click()
        print('-------------')
        
        driver.find_element(By.CSS_SELECTOR, "#SUBMIT-nav-ctr-btn").click()
        random_sleep(30)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="CONFIRMATION_ADVISORY"]')))
        
        
        
        if("Thanks for your request. Unfortunately, we couldn't approve your application." in driver.page_source):
            status="Denied"
        else:
            status="Pending"
        
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="Chase Ink Business Card"
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
        print(e)
        full_name=data.get('preApproval').get('firstName')+' '+data.get('preApproval').get('lastName')
        card_name="Chase Ink Business Card"
        
        filepath=f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag=0
        except:
            flag=1
            filepath=''
        upload_screenshot(filepath, data.get('application_id'), product_id, flag)
        