from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Ascentium Capital
# ------------------------------------------------------

def ascentiumCapital(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "ssn": 124365888,
        #         "mobileNumber": 7349303040,
        #         "homeAddress": "123 street",
        #         "city": "Jaipur",
        #         "state": "AK",
        #         "zipcode": 85445,
        #     },
        #     "business": {
        #         "legalName": "Business Legal Name",
        #         "dbaName": "DBA(if applicable)",
        #         "streetAddress": "Business street address",
        #         "zipCode": "ZIP Code",
        #         "city": "City",
        #         "state": "State",
        #         "phoneNumber": "Phone number",
        #         "email": "Email",
        #         "website": "Website",
        #         "legalStructure": "Legal structure",
        #         "taxId": "Federal Tax ID",
        #         "formationState": "state of inc./formation",
        #         "annualRevenue": "gross annual revenue in prior fiscal year",
        #         "numEmployees": "of workers",
        #         "dateOfOwnership": "Date business started under current ownership",
        #         "industryType": "Industry type",
        #         "requestAmount": "Request amount",
        #         "businessPurpose": "Business purpose",
        #         "bankName": "Bank Name",
        #         "account": "Account",
        #         "balance": "Average daily balance",
        #         "bankPhone": "phone",
        #         "contactFirstName": "contact first name",
        #         "contactLastName": "contact last name",
        #     }
        # }
        driver.get("https://myascentium.com/ApplyNow/CommCredit?_gl=1*1ondxzi*_gcl_au*ODYzMjUzNzU2LjE3Mjc0NDMwMjY.*rollup_ga*NjM1MTE1Nzg5LjE3Mjc0NDMwMjY.*rollup_ga_HGL8EBD5R8*MTcyNzQ0MzAyNi4xLjAuMTcyNzQ0MzAyNy41OS4wLjA.*_ga*NjM1MTE1Nzg5LjE3Mjc0NDMwMjY.*_ga_KDGRTTC9MX*MTcyNzQ0MzAyNi4xLjAuMTcyNzQ0MzAyNy41OS4wLjA.")
        random_sleep(15)

        # Personal Information
        firstName = data["personal"]["firstName"]
        lastName = data["personal"]["lastName"]
        dob = data["personal"]["dob"]
        ssn = data["personal"]["ssn"]
        homeAddress = data["personal"]["homeAddress"]
        city = data["personal"]["city"]
        zipcode = data["personal"]["zipcode"]
        state = data["personal"]["state"]
        email = data["email"]
        mobileNumber = data["personal"]["mobileNumber"]

        # Business Information
        legalName = data["business"]["legalName"]
        dbaName = data["business"]["dbaName"]
        streetAddress = data["business"]["streetAddress"]
        businessZipCode = data["business"]["zipCode"]
        businessCity = data["business"]["city"]
        businessState = data["business"]["state"]
        businessPhoneNumber = data["business"]["phoneNumber"]
        businessEmail = data["business"]["email"]
        website = data["business"]["website"]
        legalStructure = data["business"]["legalStructure"]
        taxId = data["business"]["taxId"]
        formationState = data["business"]["formationState"]
        annualRevenue = data["business"]["annualRevenue"]
        numEmployees = data["business"]["numEmployees"]
        dateOfOwnership = data["business"]["dateOfOwnership"]
        industryType = data["business"]["industryType"]
        requestAmount = data["business"]["requestAmount"]
        businessPurpose = data["business"]["businessPurpose"]
        bankName = data["business"]["bankName"]
        account = data["business"]["account"]
        balance = data["business"]["balance"]
        bankPhone = data["business"]["bankPhone"]
        contactFirstName = data["business"]["contactFirstName"]
        contactLastName = data["business"]["contactLastName"]

        random_sleep(20)

        # Fill in the form
        write_delay(driver, '//*[@id="LegalName"]', legalName)
        random_sleep(1)
        write_delay(driver, '//*[@id="DbaName"]', dbaName)
        random_sleep(1)
        write_delay(driver, '//*[@id="Address"]', streetAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="Zip"]', businessZipCode)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="City"]', businessCity)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="State"]', businessState)
        random_sleep(1)
        write_delay(driver, '//*[@id="Phone"]', businessPhoneNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="BizEmail"]', businessEmail)
        random_sleep(1)
        write_delay(driver, '//*[@id="WebSite"]', website)
        random_sleep(1)
        # write_delay(driver, '', legalStructure)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="LegalStructureId"]'
                )
                select = Select(select_element)
                select.select_by_value('20032')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        # write_delay(driver, '//*[@id="TaxId"]', taxId)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="FormationState"]', formationState)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="FormationState"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        write_delay(driver, '//*[@id="AnnualRevenue"]', annualRevenue)
        random_sleep(1)
        # write_delay(driver, '//*[@id="NumEmployees"]', numEmployees)
        random_sleep(1)
        write_delay(driver, '//*[@id="DateOfOwnership"]', '01/01/2002')
        random_sleep(1)
        # write_delay(driver, '//*[@id="Naics"]', industryType)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="Naics"]'
                )
                select = Select(select_element)
                select.select_by_value('424490')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1
        random_sleep(1)
        
        random_sleep(1)
        write_delay(driver, '//*[@id="RequestAmt"]', requestAmount)
        random_sleep(1)
        # write_delay(driver, '//*[@id="Equipments_0__Description"]', businessPurpose)
        random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__ReferenceName"]', bankName)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__AcctNum"]', account)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__Balance"]', balance)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__Phone"]', bankPhone)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__ContactFirstName"]', contactFirstName)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="References_0__ContactLastName"]', contactLastName)
        # random_sleep(1)

        # Clear and Next Step
        # send_click(driver/, '//*[@id="clear"]')
        random_sleep(1)
        send_click(driver, '//*[@id="next"]')
        random_sleep(1)

        # Page 2
        write_delay(driver, '//*[@id="Contacts_4127aefa-f781-46c0-b862-f39ae3ada5f5__FirstName"]', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="Contacts_4127aefa-f781-46c0-b862-f39ae3ada5f5__LastName"]', lastName)
        random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__Generation"]', "")
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__Title"]', "")
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__EmailAddress"]', email)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__MainPhone"]', mobileNumber)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__PctOwnership"]', "")
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__SsnTaxId"]', ssn)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__Address"]', homeAddress)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__Zip"]', zipcode)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__City"]', city)
        # random_sleep(1)
        # write_delay(driver, '//*[@id="Contacts_db57f5d7-8a28-4671-ae93-0dd5824e548b__State"]', state)
        # random_sleep(1)

        # Agree to Terms
        send_click(driver, '//*[@id="cbAgree"]')
        random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="submit-button"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Ascentium Capital"
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
        card_name = "Ascentium Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
