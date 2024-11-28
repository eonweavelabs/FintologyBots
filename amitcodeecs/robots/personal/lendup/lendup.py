from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Lendup
# ------------------------------------------------------

def lendup(driver, data, product_id):
    try:
        #data = {
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
        #         "loanAmount": 5000,
        #         "loanPurpose": "personal",
        #         "timeAtResidence": 24,
        #         "timeEmployed": 36,
        #         "nextPaydate": "01/15/2023",
        #         "employerName": "ABC Corp",
        #         "jobTitle": "Software Engineer",
        #         "workPhone": 1234567890,
        #         "payFrequency": "bi-weekly",
        #         "directDeposit": "yes",
        #         "routingNumber": "123456789",
        #         "bankName": "XYZ Bank",
        #         "accountType": "checking",
        #         "monthsAtBank": 12,
        #         "bankPhone": 9876543210,
        #         "bankAccountNumber": "123456789012",
        #         "driversLicenseNumber": "D1234567",
        #         "issuingState": "AK",
        #         "creditScore": 700,
        #     }
        # }
        driver.get("https://www.lendup.com/apply")
        random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)

        # Loan Amount
        # write_delay(driver, '//*[@id="id_field_requested_amount"]', personal.get("loanAmount"))
        random_sleep(1)

        # Loan Purpose
        write_delay(driver, '//*[@id="id_field_loan_purpose"]', 'OTHER')
        random_sleep(1)

        # Email
        random_sleep(1)
        random_sleep(1)
        driver.execute_script('document.querySelector("#pr-lead-form-v3").shadowRoot.querySelector("#pr-lead-form-v3_inner").click()' )
        write_delay(driver, '//*[@id="id_field_email"]', email)


        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="id_field_email"]'
                )
                driver.execute_script('#id_field_email',select_element, email)
                # select = Select(select_element)
                # select.select_by_value(personal.get("state"))
                 # driver.execute_script(
        #         #     "arguments[0].setAttribute('value',arguments[1])", 
        #         #     select_element, 
        #         #     state
        #         # )
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Phone number
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[5]/label', personal.get("mobileNumber"))
        random_sleep(1)

        # Last 4 digits of SSN
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[6]/label', str(personal.get("ssn"))[-4:])
        random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[7]/label', personal.get("firstName"))
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[8]/label', personal.get("lastName"))
        random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[9]/label', personal.get("dob"))
        random_sleep(1)

        # ZIP Code
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[10]/label', personal.get("zipcode"))
        random_sleep(1)

        # Street Address
        write_delay(driver, '//*[@id="id_page_three-step-1"]/div[1]/div[11]/label', personal.get("homeAddress"))
        random_sleep(1)

        # Would you also consider a lower amount?
        send_click(driver, '//*[@id="id_field_switch_vertical_1"]')
        random_sleep(1)

        # NEXT STEP
        send_click(driver, '//*[@id="id_button_next_step"]')
        random_sleep(1)

        # State
        write_delay(driver, '//*[@id="id_field_state"]', personal.get("state"))
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="id_page_three-step-2"]/div[1]/div[2]/label', personal.get("city"))
        random_sleep(1)

        # Time at residence
        write_delay(driver, '//*[@id="id_field_address_length_months"]', personal.get("timeAtResidence"))
        random_sleep(1)

        # Do you own or rent?
        send_click(driver, '//[@id="id_field_own_home_1"]' if personal.get("housingStatus") == "own" else '//[@id="id_field_own_home_0"]')
        random_sleep(1)

        # Source of income
        write_delay(driver, '//*[@id="id_field_income_type"]', personal.get("employmentType"))
        random_sleep(1)

        # Time employed
        write_delay(driver, '//*[@id="id_field_employed_months"]', personal.get("timeEmployed"))
        random_sleep(1)

        # Monthly gross income
        write_delay(driver, '//*[@id="id_field_monthly_income"]', personal.get("grossIncome"))
        random_sleep(1)

        # Next Paydate
        write_delay(driver, '//*[@id="id_page_three-step-2"]/div[1]/div[8]/div', personal.get("nextPaydate"))
        random_sleep(1)

        # Employer name
        write_delay(driver, '//*[@id="id_page_three-step-2"]/div[1]/div[9]/span', personal.get("employerName"))
        random_sleep(1)

        # Job title
        write_delay(driver, '//*[@id="id_page_three-step-2"]/div[1]/div[10]/label', personal.get("jobTitle"))
        random_sleep(1)

        # Work phone
        write_delay(driver, '//*[@id="id_page_three-step-2"]/div[1]/div[11]/label', personal.get("workPhone"))
        random_sleep(1)

        # How often are you paid?
        write_delay(driver, '//*[@id="id_field_pay_frequency"]', personal.get("payFrequency"))
        random_sleep(1)

        # How is your paycheck received?
        write_delay(driver, '//*[@id="id_field_direct_deposit"]', personal.get("directDeposit"))
        random_sleep(1)

        # NEXT STEP
        send_click(driver, '//*[@id="id_button_next_step"]')
        random_sleep(1)

        # ABA/routing number
        write_delay(driver, '//*[@id="id_page_three-step-3"]/div[1]/div[1]/label', personal.get("routingNumber"))
        random_sleep(1)

        # Bank Name
        write_delay(driver, '//*[@id="id_page_three-step-3"]/div[1]/div[2]/label', personal.get("bankName"))
        random_sleep(1)

        # Account type
        write_delay(driver, '//*[@id="id_field_bank_account_type"]', personal.get("accountType"))
        random_sleep(1)

        # Months at bank
        write_delay(driver, '//*[@id="id_field_bank_account_length_months"]', personal.get("monthsAtBank"))
        random_sleep(1)

        # Bank Phone
        write_delay(driver, '//*[@id="id_page_three-step-3"]/div[1]/div[5]/label', personal.get("bankPhone"))
        random_sleep(1)

        # Bank Account Number
        write_delay(driver, '//*[@id="id_page_three-step-3"]/div[1]/div[6]/label', personal.get("bankAccountNumber"))
        random_sleep(1)

        # Driver's license or state id
        write_delay(driver, '//*[@id="id_field_drivers_license_number"]', personal.get("driversLicenseNumber"))
        random_sleep(1)

        # Issuing State
        write_delay(driver, '//*[@id="id_field_drivers_license_state"]', personal.get("issuingState"))
        random_sleep(1)

        # Credit Score
        write_delay(driver, '//*[@id="id_field_credit_score"]', personal.get("creditScore"))
        random_sleep(1)

        # Social Security Number
        write_delay(driver, '//*[@id="id_page_three-step-3"]/div[1]/div[10]/label', personal.get("ssn"))
        random_sleep(1)

        # Request cash
        send_click(driver, '//*[@id="id_button_submit"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Lendup"
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
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Lendup"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

