from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Everest Business Funding
# -----------------------------------------------------------------

def everestBusinessFunding(driver, data, product_id):
    try:
        driver.get("https://everestbusinessfunding.com/business-funding/")
        random_sleep(15)

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")

        random_sleep(20)
        
        # Personal Information
        write_delay(driver, '//*[@id="nf-field-47"]', personal.get("firstName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-51"]', personal.get("lastName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-49"]', business.get("legalName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-48"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-52"]', business.get("phoneNumber"))
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-53"]', business.get("monthlySpend"))
        random_sleep(1)
        write_delay(driver, '//*[@id="nf-field-50"]', business.get("annualRevenue"))  # Assuming this is the amount needed
        random_sleep(1)
        # send_click(driver, '//*[@id="nf-field-54"]')  # Assuming this is a dropdown or similar
        random_sleep(1)
        send_click(driver, '//*[@id="nf-label-field-55"]')  # Agree to terms
        random_sleep(1)
        send_click(driver, '//*[@id="nf-field-56"]')  # Submit
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Everest Business Funding"
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
        full_name = data.get("personal").get("firstName") + " " + data.get("personal").get("lastName")
        card_name = "Everest Business Funding"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
