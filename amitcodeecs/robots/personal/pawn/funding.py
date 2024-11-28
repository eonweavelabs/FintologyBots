from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Pawn Funding
# -----------------------------------------------------------------

def pawnFunding(driver, data, product_id):
    try:
        driver.get("https://pawnfunding.com/#aabc23a0-2980-43a8-a0ee-b7ec5e4a76df")
        random_sleep(15)

        personal = data.get("personal")
        businessName = personal.get("businessName")
        contact_number = personal.get("contact_number")
        email = data.get("email")
        credit_score = personal.get("credit_score")
        full_name = personal.get("full_name")
        monthly_revenue = personal.get("monthly_revenue")
        amount_needed = personal.get("amount_needed")

        random_sleep(20)
        
        # Business Information
        write_delay(driver, '//*[@id="input20"]', businessName)
        random_sleep(1)
        write_delay(driver, '//*[@id="input21"]', contact_number)
        random_sleep(1)
        write_delay(driver, '//*[@id="input22"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="input23"]', credit_score)
        random_sleep(1)
        write_delay(driver, '//*[@id="input24"]', full_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="input25"]', monthly_revenue)
        random_sleep(1)
        write_delay(driver, '//*[@id="input26"]', amount_needed)
        random_sleep(1)
        send_click(driver, '//*[@id="aabc23a0-2980-43a8-a0ee-b7ec5e4a76df-bootstrap-container"]/span/div/div/div/form/div[8]/label')  # Sign up for email list
        random_sleep(1)
        send_click(driver, '//*[@id="aabc23a0-2980-43a8-a0ee-b7ec5e4a76df-bootstrap-container"]/span/div/div/div/form/div[9]/div/div/button')  # Submit
        random_sleep(10)
        
        card_name = "Pawn Funding"
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
        card_name = "Pawn Funding"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
