from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback
from selenium.webdriver.support.ui import Select

# -----------------------------------------------------------------
# Fenix Capital
# -----------------------------------------------------------------

def fenixCapital(driver, data, product_id):
    try:
        driver.get("https://www.fenixcapitalfunding.com/apply-now/")
        random_sleep(15)
        
        personal = data.get("personal")
        business_name = personal.get("business_name")
        years_in_operation = personal.get("years_in_operation")
        credit_score = personal.get("credit_score")
        capital_seeking = personal.get("capital_seeking")
        first_name = personal.get("first_name")
        last_name = personal.get("last_name")
        email = personal.get("email")
        phone = personal.get("phone")
        monthly_sales = personal.get("monthly_sales")

        random_sleep(20)
        
        # Business Information
        driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="wpforms-205-field_1"]', business_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-205-field_3"]', years_in_operation)
        random_sleep(1)
        
        # Select credit score
        send_click(driver, '//*[@id="wpforms-205-field_4"]/li[7]/label')
        random_sleep(1)
        
        write_delay(driver, '//*[@id="wpforms-205-field_5"]', capital_seeking)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-205-field_6"]', first_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-205-field_6-last"]', last_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-205-field_7"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="wpforms-205-field_8"]', phone)
        random_sleep(1)
        
        # Select monthly sales
        send_click(driver, '//*[@id="wpforms-205-field_9"]/li[7]/label')
        random_sleep(1)
        
        send_click(driver, '//*[@id="wpforms-submit-205"]')  # SUBMIT
        random_sleep(10)
        
        card_name = "Fenix Capital"
        filepath = f"FinalScreenshots/business/{first_name} {last_name} - {card_name}.png"
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
        card_name = "Fenix Capital"
        filepath = f"FinalScreenshots/business/{first_name} {last_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
