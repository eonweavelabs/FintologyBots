from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Oakmont Capital Services
# -----------------------------------------------------

def capitalServices(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Krishan Pratap",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "mobileNumber": 7349303040,
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #         "businessName": "My Business Name",
        #         "dba": "My DBA",
        #         "businessPhone": 1234567890,
        #         "federalId": "12-3456789",
        #         "annualRevenue": 546843,
        #         "businessStartDate": "01/01/2010",
        #         "stateOfIncorporation": "NY",
        #         "yearsInBusiness": 10,
        #         "natureOfBusiness": "Retail",
        #         "businessMailingAddress": "456 Business Rd., Suite 100, New York",
        #         "businessCity": "New York",
        #         "businessState": "NY",
        #         "businessZip": 10001,
        #         "businessCountry": "USA",
        #         "equipmentLocation": "789 Equipment St., New York",
        #         "equipmentCity": "New York",
        #         "equipmentState": "NY",
        #         "equipmentZip": 10002,
        #         "insuranceAgentName": "Agent Name",
        #         "insurancePhone": 9876543210,
        #         "guarantorFirstName": "Guarantor First",
        #         "guarantorLastName": "Guarantor Last",
        #         "guarantorTitle": "Owner",
        #         "percentageOwned": 100,
        #         "guarantorDob": "01/01/1980",
        #         "guarantorSsn": 123456789,
        #         "guarantorCitizenship": "USA",
        #         "residenceStatus": "Resident",
        #         "guarantorAddress": "123 Guarantor St., New York",
        #         "guarantorCity": "New York",
        #         "guarantorState": "NY",
        #         "guarantorZip": 10003,
        #         "guarantorEmail": "guarantor@example.com",
        #         "guarantorCell": 1231231234,
        #         "guarantorHomePhone": 3213214321,
        #         "dischargeDate": "01/01/2020",
        #         "additionalOwners": 0,
        #         "vendorName": "Vendor Name",
        #         "vendorContact": "Vendor Contact",
        #         "vendorPhone": 5555555555,
        #         "equipmentType": "Type of Equipment",
        #         "equipmentPrice": 10000,
        #         "equipmentYear": 2022,
        #         "howDidYouHear": "Internet"
        #     }
        # }
        
        personal = data.get("personal")
        email = data.get("email")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        dob = personal.get("dob")
        ssn = personal.get("ssn")
        mobileNumber = personal.get("mobileNumber")
        homeAddress = personal.get("homeAddress")
        motherMaidenName = personal.get("motherMaidenName")
        businessName = personal.get("businessName")
        dba = personal.get("dba")
        businessPhone = personal.get("businessPhone")
        federalId = personal.get("federalId")
        annualRevenue = personal.get("annualRevenue")
        businessStartDate = personal.get("businessStartDate")
        stateOfIncorporation = personal.get("stateOfIncorporation")
        yearsInBusiness = personal.get("yearsInBusiness")
        natureOfBusiness = personal.get("natureOfBusiness")
        businessMailingAddress = personal.get("businessMailingAddress")
        businessCity = personal.get("businessCity")
        businessState = personal.get("businessState")
        businessZip = personal.get("businessZip")
        businessCountry = personal.get("businessCountry")
        equipmentLocation = personal.get("equipmentLocation")
        equipmentCity = personal.get("equipmentCity")
        equipmentState = personal.get("equipmentState")
        equipmentZip = personal.get("equipmentZip")
        insuranceAgentName = personal.get("insuranceAgentName")
        insurancePhone = personal.get("insurancePhone")
        guarantorFirstName = personal.get("guarantorFirstName")
        guarantorLastName = personal.get("guarantorLastName")
        guarantorTitle = personal.get("guarantorTitle")
        percentageOwned = personal.get("percentageOwned")
        guarantorDob = personal.get("guarantorDob")
        guarantorSsn = personal.get("guarantorSsn")
        guarantorCitizenship = personal.get("guarantorCitizenship")
        residenceStatus = personal.get("residenceStatus")
        guarantorAddress = personal.get("guarantorAddress")
        guarantorCity = personal.get("guarantorCity")
        guarantorState = personal.get("guarantorState")
        guarantorZip = personal.get("guarantorZip")
        guarantorEmail = personal.get("guarantorEmail")
        guarantorCell = personal.get("guarantorCell")
        guarantorHomePhone = personal.get("guarantorHomePhone")
        dischargeDate = personal.get("dischargeDate")
        additionalOwners = personal.get("additionalOwners")
        vendorName = personal.get("vendorName")
        vendorContact = personal.get("vendorContact")
        vendorPhone = personal.get("vendorPhone")
        equipmentType = personal.get("equipmentType")
        equipmentPrice = personal.get("equipmentPrice")
        equipmentYear = personal.get("equipmentYear")
        howDidYouHear = personal.get("howDidYouHear")

        driver.get(
            "https://oakmontfinance.com/oakmont-capital-online-application/"
        )
        random_sleep(20)
        # driver.switch_to.frame(0)
        
        # Legal Business Name
        write_delay(
            driver,
            '//*[@id="field_businessname4"]',
            businessName
        )
        random_sleep(2)

        # D.B.A.
        write_delay(
            driver,
            '//*[@id="field_dba4"]',
            dba
        )
        random_sleep(2)
        
        send_click(driver, '//*[@id="frm_radio_1514-1510-0"]/label')
        random_sleep(2)
        # Business Phone
        write_delay(
            driver,
            '//*[@id="field_businessphone4"]',
            businessPhone
        )
        random_sleep(2)

        # Federal ID
        write_delay(
            driver,
            '//*[@id="field_federalid4"]',
            federalId
        )
        random_sleep(2)

        # Annual Revenue
        write_delay(
            driver,
            '//*[@id="field_annualrev4"]',
            annualRevenue
        )
        random_sleep(2)

        # Business Start Date
        write_delay(
            driver,
            '//*[@id="field_businessstart4"]',
            businessStartDate
        )
        random_sleep(2)

        # State of Incorporation
        write_delay(
            driver,
            '//*[@id="field_stateofincrop4"]',
            stateOfIncorporation
        )
        random_sleep(2)

        # Years in Business
        write_delay(
            driver,
            '//*[@id="field_businessyears4"]',
            yearsInBusiness
        )
        random_sleep(2)

        # Nature of Business
        write_delay(
            driver,
            '//*[@id="field_businessnature4"]',
            natureOfBusiness
        )
        random_sleep(2)

        # Business Mailing Address
        write_delay(
            driver,
            '//*[@id="field_businessaddress4"]',
            businessMailingAddress
        )
        random_sleep(2)

        # Business City
        write_delay(
            driver,
            '//*[@id="field_businesscity4"]',
            businessCity
        )
        random_sleep(2)

        # Business State
        write_delay(
            driver,
            '//*[@id="field_businesstate4"]',
            businessState
        )
        random_sleep(2)

        # Business ZIP Code
        write_delay(
            driver,
            '//*[@id="field_businesszip4"]',
            businessZip
        )
        random_sleep(2)

        # Business Country
        write_delay(
            driver,
            '//*[@id="field_businesscounty4"]',
            businessCountry
        )
        random_sleep(2)
        
        random_sleep(2)
        send_click(driver, '//*[@id="frm_radio_1525-1510-1"]/label')
        
        random_sleep(2)
        send_click(driver, '//*[@id="frm_radio_1530-1510-1"]/label')
        random_sleep(2)
        random_sleep(2)
        send_click(driver, '//*[@id="frm_checkbox_3136-1510-0"]/label')
        random_sleep(2)
        
        
        
        # NEXT Button
        send_click(driver, '//*[@id="form_oakmontapp"]/div/fieldset/div/div[4]/button')
        random_sleep(2)

        # Guarantor First Name
        write_delay(
            driver,
            '//*[@id="field_guarantorfirstname4"]',
            guarantorFirstName
        )
        random_sleep(2)

        # Guarantor Last Name
        write_delay(
            driver,
            '//*[@id="field_guarantorlastname4"]',
            guarantorLastName
        )
        random_sleep(2)

        # Guarantor Title
        write_delay(
            driver,
            '//*[@id="field_guarantortitle4"]',
            guarantorTitle
        )
        random_sleep(2)

        # Percentage Owned
        write_delay(
            driver,
            '//*[@id="field_guarantorpercentage4"]',
            percentageOwned
        )
        random_sleep(2)

        # Guarantor Date of Birth
        write_delay(
            driver,
            '//*[@id="field_guarantordob4"]',
            guarantorDob
        )
        random_sleep(2)

        # Guarantor Social Security Number
        write_delay(
            driver,
            '//*[@id="field_guarantorsocsec4"]',
            guarantorSsn
        )
        random_sleep(2)

        # Guarantor Country of Citizenship
        write_delay(
            driver,
            '//*[@id="field_guarantorcitizenship4"]',
            guarantorCitizenship
        )
        random_sleep(2)

        # Residence Status
        # write_delay(
        #     driver,
        #     '//*[@id="field_gurantor1resstatus4"]',
        #     residenceStatus
        # )
        # random_sleep(2)

        # Guarantor Home Address
        write_delay(
            driver,
            '//*[@id="field_guarantoraddress4"]',
            guarantorAddress
        )
        random_sleep(2)

        # Guarantor City
        write_delay(
            driver,
            '//*[@id="field_guarantorcity4"]',
            guarantorCity
        )
        random_sleep(2)

        # Guarantor State
        write_delay(
            driver,
            '//*[@id="field_guarantorstate4"]',
            guarantorState
        )
        random_sleep(2)

        # Guarantor ZIP Code
        write_delay(
            driver,
            '//*[@id="field_guarantorzip4"]',
            guarantorZip
        )
        random_sleep(2)

        # Guarantor Email
        write_delay(
            driver,
            '//*[@id="field_guarantoremail4"]',
            guarantorEmail
        )
        random_sleep(2)

        # Guarantor Cell Phone
        write_delay(
            driver,
            '//*[@id="field_guarantorcell4"]',
            guarantorCell
        )
        random_sleep(2)

        # Guarantor Home Phone
        write_delay(
            driver,
            '//*[@id="field_guarantorphone4"]',
            guarantorHomePhone
        )
        random_sleep(2)
        
        send_click(driver, '//*[@id="frm_radio_1551-1536-0"]/label')
        random_sleep(2)
        
        send_click(driver, '//*[@id="frm_radio_1552-1536-1"]/label')
        random_sleep(2)


        # Number of Additional Owners
        write_delay(
            driver,
            '//*[@id="field_additionalapplicants"]',
            0
        )

        # NEXT Button
        send_click(driver, '//*[@id="form_oakmontapp"]/div/fieldset/div/div[8]/button[2]')
        random_sleep(2)

        # Vendor Name
        write_delay(
            driver,
            '//*[@id="field_vendorname4"]',
            vendorName
        )

        # Vendor Contact Full Name
        write_delay(
            driver,
            '//*[@id="field_vendorcontact4"]',
            vendorContact
        )

        # Vendor Phone Number
        write_delay(
            driver,
            '//*[@id="field_vendorphone4"]',
            vendorPhone
        )

        # Type of Equipment
        write_delay(
            driver,
            '//*[@id="field_equipmentmodel4"]',
            equipmentType
        )

        # Equipment's Sale Price
        write_delay(
            driver,
            '//*[@id="field_equipmentprice4"]',
            equipmentPrice
        )

        # Equipment Year
        write_delay(
            driver,
            '//*[@id="field_equipmentyear4"]',
            equipmentYear
        )

        # NEXT Button
        send_click(driver, '//*[@id="form_oakmontapp"]/div/fieldset/div/div[4]/button[2]')
        random_sleep(2)

        # Agreement Checkbox
        send_click(driver, '//*[@id="field_applicantagreement4-0"]')

        # Guarantor's Full Name
        write_delay(
            driver,
            '//*[@id="field_gurantorauthorization4"]',
            f"{guarantorFirstName} {guarantorLastName}"
        )

        # Guarantor Signature (Assuming it's a canvas element)
        # You might need to use a different method to handle the signature
        # For now, we'll just scroll to it
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '//*[@id="sigPad1591"]/div/canvas'))
        random_sleep(2)

        # How did you hear about OCS?
        write_delay(
            driver,
            '//*[@id="field_ql1e"]',
            howDidYouHear
        )

        # Submit Button
        send_click(driver, '//*[@id="form_oakmontapp"]/div/fieldset/div/div[5]/button[2]')
        random_sleep(2)

        full_name = f"{firstName} {lastName}"
        card_name = "Oakmont Capital Services"
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
        full_name = f"{firstName} {lastName}"
        card_name = "Oakmont Capital Services"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
