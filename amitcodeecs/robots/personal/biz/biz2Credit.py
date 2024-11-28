from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Biz 2 Credit
# -----------------------------------------------------

def biz2Credit(driver, data, product_id):
    try:
        driver.get(
            "https://www.biz2credit.com/apply-for-business-financing"
        )
        random_sleep(15)

        # Default data with dummy values
        # data = {
        #     "personal": {
        #         "firstName": "John",
        #         "lastName": "Doe",
        #         "phone": "1234567890",
        #         "email": "john.doe@example.com",
        #         "businessNeed": "50000",
        #         "fundsPurpose": "Expansion",
        #         "fundsDuration": "12 months",
        #         "businessRevenue": "100000",
        #         "businessDuration": "5 years",
        #         "creditScore": "700",
        #         "maxAmount": "50000",
        #         "role": "Owner",
        #         "businessName": "John's Business",
        #         "dbaName": "",
        #         "businessAddress": "123 Business St",
        #         "city": "Business City",
        #         "state": "NY",
        #         "zipCode": "12345",
        #         "businessPhone": "1234567890",
        #         "ein": "123456789",
        #         "itinSsn": "123456789",
        #         "industry": "Retail",
        #         "subIndustry": "Clothing",
        #         "businessStartDate": "01/01/2000",
        #         "stateOfIncorporation": "NY",
        #         "revenue": "100000",
        #         "expenses": "50000",
        #         "lenderName": "Bank",
        #         "remainingBalance": "10000",
        #         "ownerFirstName": "John",
        #         "ownerLastName": "Doe",
        #         "ownerDob": "01/01/1980",
        #         "ssn": "1234",
        #         "jobTitle": "Owner",
        #         "ownership": "100",
        #         "mobileNumber": "1234567890",
        #         "ownerAddress": "123 Home St",
        #         "ownerCity": "Home City",
        #         "ownerState": "NY",
        #         "ownerZipCode": "12345"
        #     }
        # }

        personal = data.get("personal")

        # Aomunt
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="loanAmount"]'
                )
                select = Select(select_element)
                select.select_by_value('20000')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[1]/div/div/div[2]/div[1]/div/div', personal.get("businessNeed"))
        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[1]/div/div/div[2]/div[2]/div/div', personal.get("fundsPurpose"))
        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[1]/div/div/div[2]/div[3]/div/div', personal.get("fundsDuration"))
        send_click(driver, '//*[@id="business_chk"]')
        send_click(driver, '//*[@id="step1"]')

        # Next Page
        write_delay(driver, '//*[@id="fname"]', personal.get("firstName"))
        write_delay(driver, '//*[@id="lname"]', personal.get("lastName"))
        write_delay(driver, '//*[@id="email"]', personal.get("email"))
        write_delay(driver, '//*[@id="phoneno"]', personal.get("phone"))
        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div', personal.get("businessRevenue"))
        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div', personal.get("businessDuration"))
        write_delay(driver, '//*[@id="frm_stps"]/div[1]/div/div[2]/div/div/div[2]/div[3]/div/div', personal.get("creditScore"))
        send_click(driver, '//*[@id="step2"]')

        # Continue filling out the form with the remaining fields...
        write_delay(driver, '//*[@id="maxAmount"]', personal.get("maxAmount"))
        write_delay(driver, '//*[@id="role"]', personal.get("role"))
        write_delay(driver, '//*[@id="businessName"]', personal.get("businessName"))
        write_delay(driver, '//*[@id="dbaName"]', personal.get("dbaName"))
        write_delay(driver, '//*[@id="businessAddress"]', personal.get("businessAddress"))
        write_delay(driver, '//*[@id="city"]', personal.get("city"))
        write_delay(driver, '//*[@id="state"]', personal.get("state"))
        write_delay(driver, '//*[@id="zipCode"]', personal.get("zipCode"))
        write_delay(driver, '//*[@id="businessPhone"]', personal.get("businessPhone"))
        write_delay(driver, '//*[@id="ein"]', personal.get("ein"))
        write_delay(driver, '//*[@id="itinSsn"]', personal.get("itinSsn"))
        write_delay(driver, '//*[@id="industry"]', personal.get("industry"))
        write_delay(driver, '//*[@id="subIndustry"]', personal.get("subIndustry"))
        write_delay(driver, '//*[@id="businessStartDate"]', personal.get("businessStartDate"))
        write_delay(driver, '//*[@id="stateOfIncorporation"]', personal.get("stateOfIncorporation"))
        write_delay(driver, '//*[@id="revenue"]', personal.get("revenue"))
        write_delay(driver, '//*[@id="expenses"]', personal.get("expenses"))
        write_delay(driver, '//*[@id="lenderName"]', personal.get("lenderName"))
        write_delay(driver, '//*[@id="remainingBalance"]', personal.get("remainingBalance"))
        write_delay(driver, '//*[@id="ownerFirstName"]', personal.get("ownerFirstName"))
        write_delay(driver, '//*[@id="ownerLastName"]', personal.get("ownerLastName"))
        write_delay(driver, '//*[@id="ownerDob"]', personal.get("ownerDob"))
        write_delay(driver, '//*[@id="ssn"]', personal.get("ssn"))
        write_delay(driver, '//*[@id="jobTitle"]', personal.get("jobTitle"))
        write_delay(driver, '//*[@id="ownership"]', personal.get("ownership"))
        write_delay(driver, '//*[@id="mobileNumber"]', personal.get("mobileNumber"))
        write_delay(driver, '//*[@id="ownerAddress"]', personal.get("ownerAddress"))
        write_delay(driver, '//*[@id="ownerCity"]', personal.get("ownerCity"))
        write_delay(driver, '//*[@id="ownerState"]', personal.get("ownerState"))
        write_delay(driver, '//*[@id="ownerZipCode"]', personal.get("ownerZipCode"))

        # Save screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Biz 2 Credit"
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
        card_name = "Biz 2 Credit"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
