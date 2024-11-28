from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from selenium.webdriver.support.ui import Select
from Utils.upload_screenshots import upload_screenshot
from Utils.send_click import send_click
from Utils.write_delay import write_delay
from selenium.webdriver.common.keys import Keys
import traceback

# ------------------------------------------------------------------------------
# Bank Of America Advantage Travel Rewards Card
# ------------------------------------------------------------------------------

def advantageTravelRewardsCard(driver, data, product_id):
    try:
        # data = {
        #     "personal": {
        #         "firstName": "John",
        #         "lastName": "Doe",
        #         "dob": "1990-01-01",
        #         "ssn": "123-45-6789",
        #         "city": "New York",
        #         "zipcode": "10001",
        #         "state": "NY",
        #         "housingStatus": "own",
        #         "businessName": "Doe Enterprises",
        #         "businessNameOnCard": "Doe Enterprises LLC",
        #         "homeAddress": "123 Main St",
        #         "country": "USA",
        #         "mobileNumber": "1234567890",
        #         "taxId": "AB123456C",
        #         "countryOfOperations": "USA",
        #         "numberOfEmployees": "50",
        #         "typeOfIndustry": "Retail",
        #         "industrySubtype": "E-commerce",
        #         "grossIncome": "500000",
        #         "yearsInBusiness": "5",
        #         "monthsEstablished": "60",
        #         "jobTitle": "CEO",
        #         "sourceOfIncome": "Business",
        #         "occupation": "Business Owner",
        #         "housingPayment": "2000"
        #     },
        #     "email": "john.doe@example.com"
        # }

        driver.get(
            "https://www.bankofamerica.com/smallbusiness/credit-cards/products/travel-rewards-business-credit-card/?campaign=4053417~2P~en_US"
        )
        random_sleep(15)
        driver.get(
            "https://secure.bankofamerica.com/applynow/initialize-workflow.go?requesttype=BCC&campaignid=4064976&productoffercode=VR&mktg_track=DPRO&track=5589620050"
        )
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        ssn = data.get("personal").get("ssn")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}
        
        business_name = data.get("personal").get("businessName")
        business_name_on_card = data.get("personal").get("businessNameOnCard")
        home_address = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        state = data.get("personal").get("state")
        zipcode = data.get("personal").get("zipcode")
        country = data.get("personal").get("country")
        mobile_number = data.get("personal").get("mobileNumber")
        tax_id = data.get("personal").get("taxId")
        country_of_operations = data.get("personal").get("countryOfOperations")
        number_of_employees = data.get("personal").get("numberOfEmployees")
        type_of_industry = data.get("personal").get("typeOfIndustry")
        industry_subtype = data.get("personal").get("industrySubtype")
        gross_sales = data.get("personal").get("householdIncome")
        years_in_business = data.get("personal").get("yearsInBusiness")
        months_established = data.get("personal").get("monthsEstablished")
        job_title = data.get("personal").get("jobTitle")
        source_of_income = data.get("personal").get("sourceOfIncome")
        occupation = data.get("personal").get("position")
        housing_payment = data.get("personal").get("housingPayment")
        name_on_card = f"{firstName} {lastName}"
        

        # Business Information
        write_delay(driver, '//*[@id="search_v_1"]', business_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="bcc_businessNameOnCard_v_1"]', business_name_on_card)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_hasDba_no_v_1-real"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcardsbusiness_addr1_v_1"]', home_address)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcardsbusiness_city_v_1"]', city)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="sbcardsbusiness_state_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        # random_sleep(1)
        # write_delay(driver, '//*[@id="sbcardsbusiness_state_v_1"]', state)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcardsbusiness_zip_v_1"]', zipcode)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcardsbusiness_country_v_1"]', country)
        random_sleep(1)
        write_delay(driver, '//*[@id="zz_business_tb_bcc_busphone_v_1"]', mobile_number)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_sbMianOffice_no_v_1-real"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="taxId_v_1"]', tax_id)
        random_sleep(1)
        
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="countryOfFormation_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value('1000249')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        # write_delay(driver, '', '1000249')
        random_sleep(1)
        # write_delay(driver, '//*[@id="stateOfFormation_v_1"]', state)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="stateOfFormation_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        # random_sleep(1)
        # write_delay(driver, '//*[@id="sbcardsbusiness_state_v_1"]', state)
        random_sleep(1)
        random_sleep(1)
        
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="businessStructure_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value('SoleProprietorWCC')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        # random_sleep(1)
        # write_delay(driver, '//*[@id="sbcardsbusiness_state_v_1"]', state)
        random_sleep(1)
        # write_delay(driver, '//*[@id="businessStructure_v_1"]', '')
        random_sleep(1)
        write_delay(driver, '//*[@id="ctryOfBussOpts_v_1"]', country_of_operations)
        random_sleep(1)
        write_delay(driver, '//*[@id="businessNumberOfEmployees_v_1"]', number_of_employees)
        random_sleep(1)
        # write_delay(driver, '//*[@id="typeOfIndustry_v_1"]', type_of_industry)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="typeOfIndustry_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value("SERVICES")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        # random_sleep(1)
        # write_delay(driver, '//*[@id="sbcardsbusiness_state_v_1"]', state)
        random_sleep(1)
        random_sleep(1)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="industrySubType_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value('SERVICES_ADVERTISING')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        # random_sleep(1)
        # write_delay(driver, '//*[@id="sbcardsbusiness_state_v_1"]', state)
        random_sleep(1)
        # write_delay(driver, '//*[@id="industrySubType_v_1"]', industry_subtype)
        random_sleep(1)
        write_delay(driver, '//*[@id="grossSales_v_1"]', gross_sales)
        random_sleep(1)
        write_delay(driver, '//*[@id="yearsInBusiness_v_1"]', years_in_business)
        random_sleep(1)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="monthsEstablished_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value('1')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        # write_delay(driver, '//*[@id="monthsEstablished_v_1"]', months_established)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_nonOperatingEntity_no_v_1-real"]')
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_nonUSBusinessActivity_no_v_1-real"]')
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_nonGovernmentalOrganization_no_v_1-real"]')
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_gamblingActivities_no_v_1"]/label')
        random_sleep(1)
        # send_click(driver, '//*[@id="zz_bi_gamblingActivities_no_v_1-real"]')
        # random_sleep(1)
        send_click(driver, '//*[@id="auth_BorrowerConsent_v_1-real"]')
        random_sleep(1)

        # Personal Information
        write_delay(driver, '//*[@id="sbcards_firstName_v_1"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcards_lastName_v_1"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="Individual_JobTitle_v_1"]', job_title)
        random_sleep(1)
        write_delay(driver, '//*[@id="Individual_NameOnCard_v_1"]', name_on_card)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_issameasbusinessresidentialaddress_yes_v_1-real"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcard_home_telephoneNumber_v_1"]', mobile_number)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcards_email_tb_addr_v_1"]', email)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_uscitizen_yes_v_1-real"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="vl_citz_tb_ssn_v_1"]', ssn)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_bi_dual_citizenship_no_v_1-real"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="zz_ci_citizenship_sb_country_of_residence_v_1"]', country)
        random_sleep(1)
        write_delay(driver, '//*[@id="zz_ssndob_tb_icai_dateOfBirth_v_1"]', dob)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcards_AnnualInc_v_1"]', gross_sales)
        random_sleep(1)
        # write_delay(driver, '//*[@id="sbcards_SourceofInc_v_1"]', source_of_income)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="sbcards_SourceofInc_v_1"]'
                )
                select = Select(select_element)
                select.select_by_value('EmploymentIncome')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)

        random_sleep(1)
        # write_delay(driver, '//*[@id="sbcards_occuptlist_v_1-trunc"]', occupation)
        random_sleep(1)
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="sbcards_occuptlist_v_1-trunc"]'
                )
                select = Select(select_element)
                select.select_by_value('Engineer')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcards_housingStatus_v_1"]', housingStatusDict[housingStatus])
        random_sleep(1)
        write_delay(driver, '//*[@id="sbcards_housingpay_v_1"]', housing_payment)
        random_sleep(1)
        write_delay(driver, '//*[@id="vl_percentOfOwnershipSoleProp_v_1"]', '100')
        random_sleep(1)
        
        random_sleep(1)
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="controlling_manager_list_v_1"]')
                send_click(driver, '//*[@id="z83Iby5"]')
                
                # select_element = driver.find_element(
                #     by=By.XPATH,
                #     value='//*[@id="controlling_manager_list_v_1"]'
                # )
                # select = Select(select_element)
                # select.select_by_value('ae0a1815-3985-4381-9d13-5c4bd0270c8d')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        # write_delay(driver, '//*[@id="controlling_manager_list_v_1"]', controlling_manager)
        random_sleep(1)
        send_click(driver, '//*[@id="zz_sbcards_resp_termsConsent_v_1-real"]')
        random_sleep(1)
        send_click(driver, '//*[@id="z83I_n"]')
        random_sleep(10)
        
        # -------------------------
        # Page - 2
        # -------------------------
        
        send_click(driver, '//*[@id="h6YT9n"]')
        random_sleep(10)
        
        # -------------------------
        # Page - 3
        # -------------------------
        
        send_click(driver, '//*[@id="owner-1-Question1"]/fragment[5]/div/div/div[1]/div/label')
        random_sleep(1)
        send_click(driver, '//*[@id="business-ownership-checkbox"]/fragment[5]/div/div/div[1]/div/label')
        random_sleep(1)
        send_click(driver, '//*[@id="owner-1-Question2"]/fragment[2]/div/div/div[1]/div/label')
        random_sleep(1)
        send_click(driver, '//*[@id="owner-1-Question3"]/div[6]/fragment[2]/div/div/div[1]/div/label')
        random_sleep(1)
        send_click(driver, '//*[@id="pddSubmitButton"]')
        random_sleep(1)
        random_sleep(1)
        random_sleep(1)
        
        # ------------------------------------
        send_click(driver, '//*[@id="buttonSubmit"]')
        random_sleep(10)
        
        # ------------------------------------
        send_click(driver, '//*[@id="closeGoBackButton"]')
        random_sleep(10)
        
        # ------------------------------------
        send_click(driver, '//*[@id="zz_sbcards_BeniAttestation_v_1-label"]')
        random_sleep(1)
        send_click(driver, '//*[@id="y12Py0"]')
        random_sleep(10)
        

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Bank Of America Advantage Travel Rewards Card"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "Bank Of America Advantage Travel Rewards Card"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
