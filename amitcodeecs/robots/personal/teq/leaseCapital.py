from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Teq Lease Capital
# ------------------------------------------------------

def teqLeaseCapital(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
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
        #     "equipmentRequest": {
        #         "description": "Equipment Description",
        #         "amount": "50000",
        #         "condition": "new",
        #         "intendedUse": "business",
        #         "vendorName": "Vendor Name",
        #         "vendorContactName": "Vendor Contact Name",
        #         "vendorPhoneNumber": "1234567890",
        #         "businessName": "Business Name",
        #         "businessStreetAddress": "Business Street Address",
        #         "businessSuiteNumber": "Suite 100",
        #         "businessCity": "Business City",
        #         "businessState": "AL",
        #         "businessZipCode": "12345",
        #         "businessPhoneNumber": "0987654321",
        #         "legalStructure": "LLC",
        #         "businessSince": "01/01/2010",
        #         "ownerFirstName": "Owner First Name",
        #         "ownerLastName": "Owner Last Name",
        #         "ownerStreetAddress": "Owner Street Address",
        #         "ownerUnit": "Unit 1",
        #         "ownerCity": "Owner City",
        #         "ownerState": "AL",
        #         "ownerZipCode": "54321",
        #         "ownerDob": "01/01/1980",
        #         "ownerEmail": "owner@example.com",
        #         "ownershipPercentage": "50",
        #         "ownerPhoneNumber": "1122334455",
        #         "ownerSsn": "123-45-6789"
        #     }
        # }
        driver.get("https://www.teqlease.com/credit-application/")
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

        # Equipment Request Information
        equipmentRequest = data["equipmentRequest"]
        description = equipmentRequest["description"]
        amount = equipmentRequest["amount"]
        condition = equipmentRequest["condition"]
        intendedUse = equipmentRequest["intendedUse"]
        vendorName = equipmentRequest["vendorName"]
        vendorContactName = equipmentRequest["vendorContactName"]
        vendorPhoneNumber = equipmentRequest["vendorPhoneNumber"]
        businessName = equipmentRequest["businessName"]
        businessStreetAddress = equipmentRequest["businessStreetAddress"]
        businessSuiteNumber = equipmentRequest["businessSuiteNumber"]
        businessCity = equipmentRequest["businessCity"]
        businessState = equipmentRequest["businessState"]
        businessZipCode = equipmentRequest["businessZipCode"]
        businessPhoneNumber = equipmentRequest["businessPhoneNumber"]
        legalStructure = equipmentRequest["legalStructure"]
        businessSince = equipmentRequest["businessSince"]
        ownerFirstName = equipmentRequest["ownerFirstName"]
        ownerLastName = equipmentRequest["ownerLastName"]
        ownerStreetAddress = equipmentRequest["ownerStreetAddress"]
        ownerUnit = equipmentRequest["ownerUnit"]
        ownerCity = equipmentRequest["ownerCity"]
        ownerState = equipmentRequest["ownerState"]
        ownerZipCode = equipmentRequest["ownerZipCode"]
        ownerDob = equipmentRequest["ownerDob"]
        ownerEmail = equipmentRequest["ownerEmail"]
        ownershipPercentage = equipmentRequest["ownershipPercentage"]
        ownerPhoneNumber = equipmentRequest["ownerPhoneNumber"]
        ownerSsn = equipmentRequest["ownerSsn"]

        random_sleep(20)

        # Fill out the form
        write_delay(driver, '//*[@id="form-field-firstname"]', firstName)
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

        # Equipment Request
        write_delay(driver, '//*[@id="nextreview"]/div[2]/div[1]/input', description)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[2]/div[2]/div/input', amount)
        random_sleep(1)
        # Select(driver.find_element(By.XPATH, '//*[@id="nextreview"]/div[3]/div[1]/select')).select_by_visible_text(condition)
        # random_sleep(1)
        # Select(driver.find_element(By.XPATH, '//*[@id="nextreview"]/div[3]/div[2]/select')).select_by_visible_text(intendedUse)
        # random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[4]/div[2]/div[1]/input', vendorName)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[4]/div[2]/div[2]/input', vendorContactName)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[4]/div[3]/div/input', vendorPhoneNumber)
        random_sleep(1)

        # Your Contact Information
        write_delay(driver, '//*[@id="nextreview"]/div[5]/div[2]/div[1]/input', firstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[5]/div[2]/div[2]/input', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[5]/div[3]/div[1]/input', mobileNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[5]/div[3]/div[2]/input', email)
        random_sleep(1)

        # Your Business
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[2]/div[1]/input', businessName)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[2]/div[2]/input', businessStreetAddress)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[3]/div[1]/input', businessSuiteNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[3]/div[2]/input', businessCity)
        random_sleep(1)
        # Select(driver.find_element(By.XPATH, '//*[@id="nextreview"]/div[6]/div[4]/div[1]/select')).select_by_visible_text(businessState)
        # random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[4]/div[2]/input', businessZipCode)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[5]/div[1]/input', businessPhoneNumber)
        random_sleep(1)
        # Select(driver.find_element(By.XPATH, '//*[@id="nextreview"]/div[6]/div[5]/div[2]/select')).select_by_visible_text(legalStructure)
        # random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[6]/div[6]/div/input[1]', businessSince)
        random_sleep(1)

        # Business Owners
        write_delay(driver, '//*[@id="skip_section"]/div[2]/div[1]/input', ownerFirstName)
        random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[2]/div[2]/input', ownerLastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[3]/div[1]/input', ownerStreetAddress)
        random_sleep(1)
        # write_delay(driver, '//*[@id="skip_section"]/div[3]/div[2]/input', ownerUnit)
        random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[4]/div[1]/input', ownerCity)
        random_sleep(1)
        # Select(driver.find_element(By.XPATH, '//*[@id="skip_section"]/div[4]/div[2]/select')).select_by_visible_text(ownerState)
        # random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[5]/div[1]/input', ownerZipCode)
        random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[5]/div[2]/input', ownerDob)
        random_sleep(1)
        write_delay(driver, '//*[@id="skip_section"]/div[6]/div/input', ownerEmail)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[7]/div[2]/div[1]/input', 100)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[7]/div[2]/div[2]/input', ownerPhoneNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[7]/div[3]/div/input[1]', ownerSsn.split('-')[0])
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[7]/div[3]/div/input[2]', ownerSsn.split('-')[1])
        random_sleep(1)
        write_delay(driver, '//*[@id="nextreview"]/div[7]/div[3]/div/input[3]', ownerSsn.split('-')[2])
        random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="nextreview"]/div[8]/input[2]')
        random_sleep(15)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Teq Lease Capital"
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
        card_name = "Teq Lease Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
