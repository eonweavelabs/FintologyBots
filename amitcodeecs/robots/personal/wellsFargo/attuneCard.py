from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ---------------------------------------------------------------
# Wells Fargo Attune Card
# ---------------------------------------------------------------

def AttuneCard(driver,data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "citizenship": "Indiam",
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "membership": 456836297456,
        #         "housingStatus": "own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "employmentType": "full-time",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://creditcards.wellsfargo.com/attune-credit-card/?sub_channel=SEO&vendor_code=G"
        )
        random_sleep(1)
        send_click(
            driver, 
            '//*[@id="main-content"]/section[1]/div/div/div[2]/p[4]/a'
        )
        random_sleep(15)

        citizenship = data.get("personal").get("citizenship")
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        bonvoyNumber = data.get("personal").get("bonvoyNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        grossIncome = data.get("personal").get("householdIncome")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMPLOYED",
            "part-time": "EMPLOYED",
            "freelance": "EMPLOYED",
            "internship": "EMPLOYED",
        }
        
        random_sleep(20)
        
        # First Name
        write_delay(
            driver,
            '//*[@id="restrictedFirstName"]',
            firstName
        )

        random_sleep(1)

        # Middle name
        if len(middleName):
            write_delay(
                driver,
                '//*[@id="middleInitial"]',
                middleName
            )
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")

        # Last name
        write_delay(
            driver,
            '//*[@id="restrictedLastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)

        # Date of birth
        write_delay(
            driver,
            '//*[@id="birthDate"]',
            dob
        )
        random_sleep(1)
        random_sleep(1)

        # Mother name
        write_delay(
            driver,
            '//*[@id="securityWord"]',
            motherMaidenName
        )
        random_sleep(1)

        # SSN Number
        write_delay(
            driver,
            '//*[@id="tin"]',
            ssn
        )

        random_sleep(1)

        # Home address
        write_delay(
            driver,
            '//*[@id="restrictedAddressLine1"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="zipCode"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="restrictedCity"]',
            city,
            clear=True
        )

        random_sleep(1)

        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="yourInfoCommand"]/div[2]/fieldset/div[2]/div[2]/div/div/div[1]/div/div'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="PBXKPEZJ"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="yourInfoCommand"]/div[2]/fieldset/div[2]/div[2]/div/div/div/div/input'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, state)

                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Citizenship
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="yourInfoCommand"]/div[2]/fieldset/div[3]/div[2]/div/div/div/div/div[1]/div/div[1]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="YKJZONUG"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="yourInfoCommand"]/div[2]/fieldset/div[3]/div[2]/div/div/div/div/div[1]/div/input'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, 'US')
                # select = Select(select_element)
                # select.select_by_value(citizenship)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)

        # Email
        write_delay(
            driver,
            '//*[@id="restrictedEmail"]',
            email
        )

        random_sleep(1)
        random_sleep(1)

        # Phone number
        write_delay(
            driver,
            '//*[@id="phoneNumber"]',
            mobileNumber
        )

        random_sleep(1)

        # Checkbox One
        # send_click(
        #     driver,
        #     '//*[@id="yourInfoCommand"]/div[3]/fieldset/div[4]/div/fieldset/div/div/div/div/div/div',
        # )
        random_sleep(1)

        # Marriott Bonvoy number
        # write_delay(
        #     driver,
        #     '//*[@id="marriottBonvoyId-text-validate-input-field"]',
        #     bonvoyNumber
        # )

        random_sleep(1)

        # Type of residense
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="yourInfoCommand"]/div[3]/fieldset/div[1]/div[1]/div/div/div/div'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="WTPDKAZQ"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="yourInfoCommand"]/div[3]/fieldset/div[1]/div[1]/div/div/div/div/input'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])", select_element, housingStatusDict.get(housingStatus))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        # Employment status
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="yourInfoCommand"]/div[3]/fieldset/div[2]/div[1]/div/div/div/div/div[1]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="AWIZGHOW"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="yourInfoCommand"]/div[3]/fieldset/div[2]/div[1]/div/div/div/div/input'
                )
                driver.execute_script(
                    "arguments[0].setAttribute('value',arguments[1])",
                    select_element,
                    employmentTypeDict.get(employmentType)
                )
                break
            except:
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)

        # Gross annual income
        write_delay(
            driver,
            '//*[@id="incomeAmount"]',
            grossIncome
        )

        random_sleep(1)

        random_sleep(1)
        
        # Checkbox One
        send_click(
            driver,
            '//*[@id="ecbsv-consent-container"]/div[2]/div/div/div/div[1]/div',
        )
        random_sleep(1)

        # I Agree
        try:
            send_click(
                driver, '//*[@id="yourInfoCommand"]/div[8]/div[6]/div/div/div/div/div')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Wells Fargo Attune Card.png"
            )
        random_sleep(1)

        # Submit button
        send_click(driver, '//*[@id="ROVZPAMX"]')
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]'
                )
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Popup Confirm
        # send_click(
        #     driver,
        #     '//*[@id="pav-save"]',
        # )
        random_sleep(10)
        random_sleep(1)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Wells Fargo Attune Card"
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
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Wells Fargo Attune Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

