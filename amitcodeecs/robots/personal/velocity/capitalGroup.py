from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Velocity Capital Group
# -----------------------------------------------------

def capitalGroup(driver, data, product_id):
    try:
        driver.get(
            "https://www.velocitycg.com/apply//"
        )
        random_sleep(15)

        # Default data with dummy values
        data = {
            "personal": {
                "firstName": "John",
                "lastName": "Doe",
                "companyName": "Doe Enterprises",
                "creditScore": "700",
                "totalAnnualSales": "1000000",
                "phone": "1234567890",
                "amountRequested": "50000",
                "owner1Name": "John Doe",
                "owner1Email": "john.doe@example.com",
                "owner2Name": "Jane Doe",
                "owner2Email": "jane.doe@example.com",
                "representativeName": "Jim Doe",
                "representativeEmail": "jim.doe@example.com"
            },
            "email": "contact@doeenterprises.com"
        }

        personal = data.get("personal")

        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        companyName = personal.get("companyName")
        creditScore = personal.get("creditScore")
        email = data.get("email")
        totalAnnualSales = personal.get("totalAnnualSales")
        phone = personal.get("phone")
        amountRequested = personal.get("amountRequested")
        owner1Name = personal.get("owner1Name")
        owner1Email = personal.get("owner1Email")
        owner2Name = personal.get("owner2Name")
        owner2Email = personal.get("owner2Email")
        representativeName = personal.get("representativeName")
        representativeEmail = personal.get("representativeEmail")

        # First Name
        write_delay(
            driver,
            '//*[@id="input_comp-lmfaa1s3"]',
            firstName
        )

        # Last Name
        write_delay(
            driver,
            '//*[@id="input_comp-lmfaa3cf"]',
            lastName
        )

        # Company Name
        write_delay(
            driver,
            '//*[@id="input_comp-lmfab207"]',
            companyName
        )

        # Credit Score
        write_delay(
            driver,
            '//*[@id="input_comp-lmfaczh5"]',
            creditScore
        )

        # Email
        write_delay(
            driver,
            '//*[@id="input_comp-lmfa48s8"]',
            email
        )

        # Total Annual Sales
        write_delay(
            driver,
            '//*[@id="input_comp-lmfaglmp"]',
            totalAnnualSales
        )

        # Phone
        write_delay(
            driver,
            '//*[@id="input_comp-lmfabo6y"]',
            phone
        )

        # Amount Requested
        write_delay(
            driver,
            '//*[@id="input_comp-lmfagnoi"]',
            amountRequested
        )

        # Submit Button
        send_click(driver, '//*[@id="comp-lmfa48sl2"]/button')

        random_sleep(1)

        # --------------------------------
        # PowerForm Signer Information = 2
        # --------------------------------
        
        
        # Merchant/Owner_1
        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[1]/input',
            owner1Name
        )

        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[2]/input',
            owner1Email
        )

        # Merchant/Owner_2
        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[3]/input',
            owner2Name
        )

        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[4]/input',
            owner2Email
        )

        # Representative
        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[5]/input',
            representativeName
        )

        write_delay(
            driver,
            '//*[@id="root"]/div/div/div/div/form/div[1]/div/div[6]/input',
            representativeEmail
        )

        # Submit Button
        send_click(driver, '//*[@id="root"]/div/div/div/div/form/div[2]/div/div/button')
        
        # ------------------------------
        # Page - 3
        # ------------------------------
        
        # ----------------------
        # Agree and contunie
        # ----------------------
        send_click(driver, '//*[@id="action-bar-consent-control"]/div/div[2]/div[2]')
        
        # ----------------------
        # Submit Button
        # ----------------------
        send_click(driver, '//*[@id="action-bar-btn-continue"]')
        
        # ------------------------------
        # Page - 4
        # ------------------------------
        
        # ----------------------
        # Finish button
        # ----------------------
        send_click(driver, '//*[@id="action-bar-btn-finish"]')

        
        random_sleep(1)

        full_name = f"{firstName} {lastName}"
        card_name = "Velocity Capital Group"
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
        card_name = "Velocity Capital Group"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
