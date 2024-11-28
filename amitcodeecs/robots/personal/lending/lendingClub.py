from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Lending Club
# -----------------------------------------------------------------

def lendingClub(driver, data, product_id):
    try:
        driver.get("https://www.lendingclub.com/apply/personal/identity/primary-name")
        random_sleep(15)

        email = data.get("email")
        personal = data.get("personal")

        random_sleep(20)

        # ===================
        # Page - 1
        # ===================

        # First Name
        write_delay(driver, '//*[@id="primary-name-firstName"]',
                    personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="primary-name-lastName"]',
                    personal.get("lastName"))
        random_sleep(1)
        
        # Apply Now Button
        send_click(
            driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[4]/form/div[2]/div/button')
        random_sleep(5)

        #  Page - 2
        # Business Email
        write_delay(driver, '//*[@id="email-email"]', email)
        random_sleep(1)
        
        # Checkbox
        send_click(
            driver, '//*[@id="agreements"]')
        random_sleep(1)
        
        send_click(
            driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[2]/div/button[2]')
        random_sleep(5)

        # Password
        write_delay(driver, '/html/body/div[1]/div[1]/form[1]/label[2]/div/input',
                    'personal.get("password")')
        random_sleep(1)

        # Apply Now Button
        send_click(
            driver, '/html/body/div[1]/div[1]/form[1]/div[4]/button[2]')
        random_sleep(15)

        # ===================
        # Page - 2
        # ===================

        # Street Address
        write_delay(driver, '//*[@id="primary-address-streetAddress"]',
                    personal.get("streetAddress"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="primary-address-city"]',
                    personal.get("city"))
        random_sleep(1)

        # State
        write_delay(driver, '//*[@id="primary-address-state"]',
                    personal.get("state"))
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="primary-address-zip"]',
                    personal.get("zip"))
        random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="primary-dob-dob"]',
                    personal.get("dob"))
        random_sleep(1)

        # Mobile
        write_delay(driver, '//*[@id="phoneNumber"]',
                    personal.get("mobile"))
        random_sleep(1)

        # Next Button
        send_click(driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[2]/div/button[2]')
        random_sleep(15)

        # ===================
        # Page - 3
        # ===================

        # Total Annual Income
        write_delay(driver, '//*[@id="primary-income-income"]',
                    personal.get("annualIncome"))
        random_sleep(1)

        # Living Situation
        if personal.get("livingSituation") == "RENT":
            send_click(driver, '//*[@id="homeStatus-RENT"]')
        elif personal.get("livingSituation") == "MORTGAGE":
            send_click(driver, '//*[@id="homeStatus-MORTGAGE"]')
        elif personal.get("livingSituation") == "OWN":
            send_click(driver, '//*[@id="homeStatus-OWN"]')
        random_sleep(1)

        # Monthly Mortgage Payment
        write_delay(driver, '//*[@id="primary-living-homeStatusExpense"]',
                    personal.get("monthlyMortgagePayment"))
        random_sleep(1)

        # Loan Amount
        write_delay(driver, '//*[@id="loan-intent-loanAmount"]',
                    personal.get("loanAmount"))
        random_sleep(1)

        # Loan Purpose
        write_delay(driver, '//*[@id="loanPurpose"]',
                    personal.get("loanPurpose"))
        random_sleep(1)

        # Next Button
        send_click(driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[2]/div/button[2]')
        random_sleep(15)

        # Are you applying with someone else?
        if personal.get("applyingWithSomeoneElse") == "JUST_ME":
            send_click(driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[1]/fieldset/ul/li[1]/label/div[2]/div')
        elif personal.get("applyingWithSomeoneElse") == "TWO_OF_US":
            send_click(driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[1]/fieldset/ul/li[2]/label/div[2]/div')
        random_sleep(1)

        # Get Your Rate Button
        send_click(driver, '//*[@id="pi1-1QAAT"]/div[2]/div[2]/div/div[3]/form/div[2]/div/button[2]')
        random_sleep(1)

        # Screenshot and upload
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Lending Club"
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
        card_name = "Lending Club"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
