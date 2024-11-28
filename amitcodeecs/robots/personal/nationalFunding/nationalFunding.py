from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# National Funding
# -----------------------------------------------------

def NationalFunding(driver, data, product_id):
    try:
        driver.get(
            "https://www.nationalfunding.com/application/apply-now/"
        )
        random_sleep(15)

        # Default data with dummy values
        data = {
            "personal": {
                "firstName": "John",
                "lastName": "Doe",
                "phone": "1234567890",
                "isAuthorizedRepresentative": "Yes",
                "isMajorityOwnerForeign": "No",
                "hasForeignOperations": "No",
                "businessEstablished": "01/01/2000",
                "cardNumber": "",
                "zip": ""
            },
            "email": "john.doe@example.com",
        }

        personal = data.get("personal")

        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        email = data.get("email")
        phone = personal.get("phone")
        cardNumber = personal.get("cardNumber")
        zipCode = personal.get("zip")
        businessEstablished = personal.get("businessEstablished")
        
        # First Name
        write_delay(
            driver,
            '//*[@id="form-full-dlp"]/div[2]/div[1]/input',
            firstName
        )

        # Last Name
        write_delay(
            driver,
            '//*[@id="form-full-dlp"]/div[2]/div[2]/input',
            lastName
        )

        # Email Address
        write_delay(
            driver,
            '//*[@id="form-full-dlp"]/div[3]/div[1]/input',
            email
        )

        # Phone
        write_delay(
            driver,
            '//*[@id="form-full-dlp"]/div[3]/div[2]/input',
            phone
        )

        # Card Number (Optional)
        # write_delay(
        #     driver,
        #     '//*[@id="form-full-dlp"]/div[4]/div[2]/div/div[2]/input',
        #     cardNumber
        # )

        # ZIP (Optional)
        # write_delay(
        #     driver,
        #     '//*[@id="form-full-dlp"]/div[4]/div[2]/div/div[3]/input',
        #     zipCode
        # )

        # When was your business established?
        # write_delay(
        #     driver,
        #     '//*[@id="form-full-dlp"]/div[2]/div[3]/div/div/div[1]/input',
        #     businessEstablished
        # )

        # Not yet started
        send_click(driver, '//*[@id="tier2a"]')

        # Agree to Privacy Policy, Terms and Conditions
        send_click(driver, '//*[@id="ccpa-input-dlp"]')

        # Get Started
        send_click(driver, '//*[@id="appSubmit"]')

        random_sleep(15)

        full_name = f"{firstName} {lastName}"
        card_name = "National Funding"
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
        card_name = "National Funding"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
