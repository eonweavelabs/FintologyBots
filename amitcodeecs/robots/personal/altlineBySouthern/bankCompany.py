from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Altline By Southern Bank Company
# ------------------------------------------------------

def altlineBySouthernBankCompany(driver, data, product_id):
    try:
        driver.get("https://altline.sobanco.com/apply/")
        random_sleep(15)

        personal = data.get("personal")
        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        email = data.get("email")
        company = personal.get("company")
        mobileNumber = personal.get("mobileNumber")


        random_sleep(20)

        # Fill out the form
        driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="983861_196117pi_983861_196117"]', firstName )
        random_sleep(1)
        write_delay(driver, '//*[@id="983861_196120pi_983861_196120"]', lastName)
        random_sleep(1)
        write_delay(driver, '//*[@id="983861_196123pi_983861_196123"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="983861_196126pi_983861_196126"]', mobileNumber)
        random_sleep(1)
        write_delay(driver, '//*[@id="983861_196129pi_983861_196129"]', company )
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="983861_196132pi_983861_196132"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('2727649')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="983861_261260pi_983861_261260"]'
                )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                select = Select(select_element)
                select.select_by_value('3666650')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        random_sleep(1)
        send_click(driver, '//*[@id="pardot-form"]/p[3]/input')  # Submit Loan Application
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Altline By Southern Bank Company"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), 'product_id', flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "Altline By Southern Bank Company"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
