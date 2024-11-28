from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Silverline Funding
# -----------------------------------------------------------------

def silverlineFunding(driver, data, product_id):
    try:
        driver.get("https://silverlinefunding.com/#contact_sec")
        random_sleep(15)

        personal = data.get("personal")
        business = data.get("business")
        email = data.get("email")

        random_sleep(20)
        
        # Personal Information
        write_delay(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[1]/span/input', personal.get("firstName") + " " + personal.get("lastName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[2]/span/input', business.get("legalName"))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[3]/span/input', business.get("phoneNumber"))
        random_sleep(1)
        write_delay(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[4]/span/input', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[5]/span/textarea', business.get("message"))
        random_sleep(1)
        send_click(driver, '//*[@id="wpcf7-f21-p7-o1"]/form/div[2]/div[6]/input')  # Submit
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Silverline Funding"
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
        card_name = "Silverline Funding"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
