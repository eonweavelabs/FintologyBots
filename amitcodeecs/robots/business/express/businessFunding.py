from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Express Business Funding
# ------------------------------------------------------

def expressBusinessFunding(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "date": "10/06/2024",
        #         "ssn": 124365888,
        #         "housingStatus": "own",
        #         "grossIncome": 876655,
        #         "mobileNumber": 7349303040,
        #         "employmentType": "full-time",
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "city": "Jaipur",
        #         "homeAddress": "123 street",
        #         "motherMaidenName": "motherMaidenName",
        #     },
        #     "business": {
        #         "companyLegalName": "Company Legal Name",
        #         "dbaTradeName": "Trade Name",
        #         "corporateTitle": "Corporate Title",
        #         "addressLine1": "Address Line 1",
        #         "addressLine2": "Address Line 2",
        #         "city": "City",
        #         "state": "State",
        #         "postalCode": "Postal Code",
        #         "country": "Country",
        #         "website": "Website",
        #         "telephone": "Telephone",
        #         "businessType": "Corporation",
        #         "corporationNumber": "Corporation Number",
        #         "dateEstablished": "01/01/2010",
        #         "yearsInOwnership": 5,
        #         "facilityAmountRequested": 100000,
        #         "typeOfBusiness": "Type of Business",
        #         "industry": "Industry",
        #         "projectedAnnualSales": 1000000,
        #         "previous12MonthSales": 900000,
        #         "projectedNetIncome": 100000,
        #         "previous12MonthNetIncome": 90000,
        #         "intendedUseOfFunds": "Expansion",
        #         "workedWithFactorBefore": "No",
        #         "factorCompanyName": "",
        #         "receivablesPledgedAsCollateral": "No",
        #         "litigationInvolved": "No",
        #         "bankruptcyFiled": "No",
        #         "bankName": "Bank Name",
        #         "bankBranch": "Bank Branch",
        #         "bankLocation": "Bank Location",
        #         "bankContact": "Bank Contact",
        #         "bankPhoneNumber": "Bank Phone Number",
        #         "bankDuration": "5 years",
        #         "lenderName": "Lender Name",
        #         "lenderAmount": 50000,
        #         "lenderCollateral": "Collateral",
        #         "principal1": {
        #             "name": "Principal 1",
        #             "title": "Title",
        #             "sin": "SIN",
        #             "dob": "01/01/1980",
        #             "homeAddress": "Home Address",
        #             "city": "City",
        #             "state": "State",
        #             "postalCode": "Postal Code",
        #             "country": "Country",
        #             "rentOrOwn": "Own",
        #             "signingAuthority": "Yes",
        #             "percentageOwned": 50
        #         },
        #         "principal2": {
        #             "name": "Principal 2",
        #             "title": "Title",
        #             "sin": "SIN",
        #             "dob": "01/01/1980",
        #             "homeAddress": "Home Address",
        #             "city": "City",
        #             "state": "State",
        #             "postalCode": "Postal Code",
        #             "country": "Country",
        #             "rentOrOwn": "Own",
        #             "signingAuthority": "Yes",
        #             "percentageOwned": 50
        #         },
        #         "criminalOffenseConviction": "No",
        #         "subsidiaries": "Subsidiaries",
        #         "federalBusinessNumber": "Federal Business Number",
        #         "craBusinessNumber": "CRA Business Number",
        #         "workersCompensationNumber": "Workers Compensation Number",
        #         "payrollServiceUsed": "No",
        #         "numberOfEmployees": 10,
        #         "taxStatus": {
        #             "payrollTaxFederal": "Status",
        #             "hst": "Status",
        #             "payrollTaxProvincial": "Status",
        #             "gstPst": "Status",
        #             "corporateIncomeTax": "Status",
        #             "workersCompensation": "Status"
        #         },
        #         "corporateLawyerName": "Corporate Lawyer",
        #         "externalAccountantName": "External Accountant",
        #         "externalAccountantPhone": "Accountant Phone",
        #         "certification": {
        #             "principal1": "Principal 1",
        #             "principal1Initials": "Initials",
        #             "principal2": "Principal 2",
        #             "principal2Initials": "Initials"
        #         }
        #     }
        # }

        driver.get("https://ebf.ca/financing-application/")
        random_sleep(15)

        # Personal Information
        personal_info = data.get("personal", {})
        firstName = personal_info.get("firstName")
        lastName = personal_info.get("lastName")
        dob = personal_info.get("dob")
        date = personal_info.get("date")
        ssn = personal_info.get("ssn")
        homeAddress = personal_info.get("homeAddress")
        city = personal_info.get("city")
        zipcode = personal_info.get("zipcode")
        state = personal_info.get("state")
        email = data.get("email")
        mobileNumber = personal_info.get("mobileNumber")
        grossIncome = personal_info.get("grossIncome")

        # Business Information
        business_info = data.get("business", {})
        companyLegalName = business_info.get("companyLegalName")
        dbaTradeName = business_info.get("dbaTradeName")
        corporateTitle = business_info.get("corporateTitle")
        addressLine1 = business_info.get("addressLine1")
        addressLine2 = business_info.get("addressLine2")
        businessCity = business_info.get("city")
        businessState = business_info.get("state")
        postalCode = business_info.get("postalCode")
        country = business_info.get("country")
        website = business_info.get("website")
        telephone = business_info.get("telephone")
        corporationNumber = business_info.get("corporationNumber")
        dateEstablished = business_info.get("dateEstablished")
        yearsInOwnership = business_info.get("yearsInOwnership")
        facilityAmountRequested = business_info.get("facilityAmountRequested")
        typeOfBusiness = business_info.get("typeOfBusiness")
        industry = business_info.get("industry")
        projectedAnnualSales = business_info.get("projectedAnnualSales")
        previous12MonthSales = business_info.get("previous12MonthSales")
        projectedNetIncome = business_info.get("projectedNetIncome")
        previous12MonthNetIncome = business_info.get("previous12MonthNetIncome")
        intendedUseOfFunds = business_info.get("intendedUseOfFunds")
        factorCompanyName = business_info.get("factorCompanyName")
        litigationInvolved = business_info.get("litigationInvolved")
        bankruptcyFiled = business_info.get("bankruptcyFiled")
        bankName = business_info.get("bankName")
        bankBranch = business_info.get("bankBranch")
        bankLocation = business_info.get("bankLocation")
        bankContact = business_info.get("bankContact")
        bankPhoneNumber = business_info.get("bankPhoneNumber")
        bankDuration = business_info.get("bankDuration")
        lenderName = business_info.get("lenderName")
        lenderAmount = business_info.get("lenderAmount")
        lenderCollateral = business_info.get("lenderCollateral")

        # Principal 1 Information
        principal1 = data.get("business").get("principal1", {})
        principal1Name = principal1.get("name")
        principal1Title = principal1.get("title")
        principal1Sin = principal1.get("sin")
        principal1Dob = principal1.get("dob")
        principal1HomeAddress = principal1.get("homeAddress")
        principal1City = principal1.get("city")
        principal1State = principal1.get("state")
        principal1PostalCode = principal1.get("postalCode")
        principal1Country = principal1.get("country")
        
        # Principal 2 Information
        principal2 = data.get("business").get("principal2", {})
        principal2Name = principal2.get("name")
        principal2Title = principal2.get("title")
        principal2Sin = principal2.get("sin")
        principal2Dob = principal2.get("dob")
        principal2HomeAddress = principal2.get("homeAddress")
        principal2City = principal2.get("city")
        principal2State = principal2.get("state")
        principal2PostalCode = principal2.get("postalCode")
        principal2Country = principal2.get("country")
        
        # Other Information
        federalBusinessNumber = data.get("business").get("federalBusinessNumber")
        craBusinessNumber = data.get("business").get("craBusinessNumber")
        workersCompensationNumber = data.get("business").get("workersCompensationNumber")
        numberOfEmployees = data.get("business").get("numberOfEmployees")
        taxStatus = data.get("business").get("taxStatus", {})
        corporateLawyerName = data.get("business").get("corporateLawyerName")
        externalAccountantName = data.get("business").get("externalAccountantName")
        externalAccountantPhone = data.get("business").get("externalAccountantPhone")
        certification = data.get("business").get("certification", {})

        # Fill out the form
        write_delay(driver, '//*[@id="wpforms-176-field_5"]', date)
        # random_sleep(1)
        send_click(driver, '//*[@id="wpforms-176-field_5"]')
        # random_sleep(1)
        send_click(driver, '//*[@id="wpforms-176-field_5"]')
        # random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-176-field_6"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-lastname"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-email"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="form-field-phone"]', mobileNumber)
        random_sleep(1)
        send_click(driver, '//*[@id="form-field-isFactoring"]')
        random_sleep(1)
        send_click(driver, '//*[@id="form-field-PrivacyConsent"]')
        random_sleep(1)
        send_click(driver, '//*[@id="Apply-Now-Button"]')
        random_sleep(1)
        send_click(driver, '//*[@id="ButtonGroupItem3"]')
        random_sleep(1)
        send_click(driver, '//*[@id="Checkbox1"]')
        random_sleep(1)
        send_click(driver, '//*[@id="b4-Bottom"]/div/div/div[2]/button')
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_Street"]', homeAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_City"]', city)
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_State"]', state)
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_PostalCode"]', zipcode)
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_DOB"]', dob)
        random_sleep(1)
        send_click(driver, '//*[@id="FICO"]')
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_Revenue"]', grossIncome)
        random_sleep(1)
        write_delay(driver, '//*[@id="Input_DateEstablished"]', dateEstablished)
        random_sleep(1)
        send_click(driver, '//*[@id="b4-Bottom"]/div/div/div[2]/button')
        
        
        
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_1"]', companyLegalName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_2"]', dbaTradeName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_4"]', corporateTitle)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6"]', addressLine1)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6-address2"]', addressLine2)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6-city"]', businessCity)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6-state"]', businessState)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6-postal"]', postalCode)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_6-country"]', country)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_126"]', mobileNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_190"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_7"]', website)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_200"]', telephone)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_199"]', corporationNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_12"]', dateEstablished)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_13"]', yearsInOwnership)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_16"]', facilityAmountRequested)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_17"]', typeOfBusiness)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_133"]', industry)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_19"]', projectedAnnualSales)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_20"]', previous12MonthSales)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_21"]', projectedNetIncome)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_22"]', previous12MonthNetIncome)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_134"]', intendedUseOfFunds)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_24"]', factorCompanyName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_138"]', litigationInvolved)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_138"]', bankruptcyFiled)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_27"]', bankName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_28"]', bankBranch)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_29"]', bankLocation)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_30"]', bankContact)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_31"]', bankPhoneNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_34"]', bankDuration)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_37"]', lenderName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_37"]', lenderAmount)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_39"]', lenderCollateral)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_54"]', principal1Name)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_55"]', principal1Title)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_56"]', principal1Sin)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_57"]', principal1Dob)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_58"]', principal1HomeAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_58-city"]', principal1City)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_58-state"]', principal1State)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_58-postal"]', principal1PostalCode)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_58-country"]', principal1Country)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_63"]', principal2Name)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_65"]', principal2Title)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_64"]', principal2Sin)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_66"]', principal2Dob)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_67"]', principal2HomeAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_67-city"]', principal2City)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_67-state"]', principal2State)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_67-postal"]', principal2PostalCode)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_67-country"]', principal2Country)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_78"]', federalBusinessNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_79"]', craBusinessNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_80"]', workersCompensationNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_83"]', numberOfEmployees)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_191"]', taxStatus.get("payrollTaxFederal", ""))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_194"]', taxStatus.get("hst", ""))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_193"]', taxStatus.get("payrollTaxProvincial", ""))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_195"]', taxStatus.get("gstPst", ""))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_192"]', taxStatus.get("corporateIncomeTax", ""))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_196"]', taxStatus.get("workersCompensation", ""))
        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_163"]', corporateLawyerName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_168"]', externalAccountantName)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_164"]', externalAccountantPhone)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_169"]', externalAccountantPhone)
        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_111"]', certification.get("principal1", "")); 
        write_delay(driver, '//*[@id="wpforms-2776-field_184"]', certification.get("principal1Initials", "")); 
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_179"]', certification.get("principal2", "")); 
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-2776-field_185"]', certification.get("principal2Initials", ""))
        random_sleep(1)
        send_click(driver, '//*[@id="wpforms-submit-2776"]')

        random_sleep(20)

        # Fill out the form
        

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Express Business Funding"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "Express Business Funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
