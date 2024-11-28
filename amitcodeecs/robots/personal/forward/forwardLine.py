from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Forward Line
# -----------------------------------------------------------------


def forwardLine(driver, data, product_id):
    try:
        driver.get("https://apply.britecap.com/")
        random_sleep(15)

        email = data.get("email")
        personal = data.get("personal")
        business = data.get("personal")

        random_sleep(20)

        # ===================
        # Page - 1
        # ===================

        # First Name
        write_delay(driver, '//*[@id="ownerFirstname"]',
                    personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="ownerLastname"]',
                    personal.get("lastName"))
        random_sleep(1)

        # Business Email
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Business Phone
        write_delay(driver, '//*[@id="businessPhone"]',
                    business.get("businessMobileNumber"))
        random_sleep(1)

        # Apply Now Button
        send_click(
            driver, '//*[@id="root"]/div/div/div/div[1]/div/div[2]/form/div[2]/div[4]/button/span[1]')
        random_sleep(15)

        # ===================
        # Page - 2
        # ===================

        # Funding Amount Requested
        write_delay(driver, '//*[@id="amountRequested"]',
                    business.get("estimatedMonthly"))
        random_sleep(1)

        # Continue Button
        send_click(driver, '//*[@id="verify-info-button"]/span[1]')
        random_sleep(15)

        # ===================
        # Page - 3
        # ===================

        # Date of birth
        write_delay(driver, '//*[@id="dateOfBirth"]', business.get("dob"))
        random_sleep(1)

        # Owner ship
        write_delay(driver, '//*[@id="percentOwnership"]',business.get("ownership"))
        random_sleep(1)

        # SSN
        write_delay(driver, '//*[@id="ssn"]', business.get("ssn"))
        random_sleep(1)

        # Legal structure
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(driver, '//*[@id="mui-component-select-legalStructure"]')
                random_sleep(1)
                send_click(driver, '//*[@id="menu-legalStructure"]/div[3]/ul/li[5]')
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="outlined-age-simple"]'
                )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, business.get('structure'))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Business Name
        # write_delay(driver, '//*[@id="businessName"]', business.get("legalBusinessName"))
        random_sleep(1)

        # Submit
        send_click(driver, '//*[@id="activate-get-results-button"]')
        random_sleep(1)

        # Business Street Address
        # write_delay(driver, '//*[@id="businessAddress"]', business.get("businessAddress"))
        random_sleep(1)

        # ZIP Code
        # write_delay(driver, '//*[@id="businessZip"]', business.get("businessZip"))
        random_sleep(1)

        # City
        # write_delay(driver, '//*[@id="city"]', business.get("city"))
        random_sleep(1)

        # State
        # send_click(driver, '//*[@id="mui-52908"]')
        random_sleep(1)

        # Is your business address the same as your home address?
        # send_click(driver, '//*[@id="mui-component-select-businessAddressIsHome"]')
        random_sleep(1)

        # Industry
        # send_click(driver, '//*[@id="mui-37259"]')
        random_sleep(1)

        # Time in Business
        # write_delay(driver, '//*[@id="timeInBusiness"]', business.get("yearInBusiness"))
        random_sleep(1)

        # Gross Annual Sales
        # write_delay(driver, '//*[@id="grossAnnualSales"]', business.get("grossBusiness"))
        random_sleep(1)

        # Screenshot and upload
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Forward Line"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Forward Line"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
