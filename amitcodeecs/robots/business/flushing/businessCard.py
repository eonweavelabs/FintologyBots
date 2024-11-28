from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from selenium.webdriver.support.select import Select

from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
from Utils.data_extraction import UserManager

def flushingBusinessCard(driver, data, product_id):
    try:
        driver.get(
            "https://creditcardlearnmore.com/11t3/202208/business-platinum?ecdma-lc=22994&ecid=OTHE_25940"
        )
        random_sleep(1)
        driver.get(
            "https://online1.elancard.com/oad/begin?locationCode=22994&offerId=6H7R5G41WM&preparerType=customer"
        )
        random_sleep(1)
        random_sleep(10)
        entityDict = {"llc": "llc", "corporation": "corporation"}
        titleDict = {
            "ceo": "chief-executive-officer",
            "member": "managing-member",
            "owner": "owner",
        }
        businessCategoryDict = {
            "business-consulting": "Professional, Scientific, and Technical Services",
            "marketing": "Professional, Scientific, and Technical Services",
            "education-support-services": "Educational Services",
            "administration": "Public Administration",
            "software-saas": "Professional, Scientific, and Technical Services",
            "construction-or-real-estate": "Real Estate and Rental and Leasing"
        }

        businessTypeDict = {
            "business-consulting": "Management, Scientific, and Technical Consulting Services",
            "marketing": "Management, Scientific, and Technical Consulting Services",
            "education-support-services": "Educational Support Services",
            "administration": "Administration of Human Resource Programs",
            "software-saas": "Management, Scientific, and Technical Consulting Services",
            "construction-or-real-estate": "Lessors of Real Estate"
        }

        businessSubTypeDict = {
            "business-consulting": "Administrative Management and General Management Consulting Services ",
            "marketing": "Marketing Consulting Services ",
            "education-support-services": "Educational Support Services",
            "administration": "Administration of Human Resource Programs (except Education, Public Health, and Veterans' Affairs Programs)",
            "software-saas": "Other Scientific and Technical Consulting Services ",
            "construction-or-real-estate": "Lessors of Other Real Estate Property "
        }

        # if not firstName or not lastName or not dob or not motherMaidenName or not ssn or not homeAddress or not city or not zipcode or not state or not email or not mobileNumber or not residencyStatus or not grossIncome or not occupation or not employer or not income or not business_legal_name or not numberOfEmployees or not business_grossSales or not einNumber or not businessAddress or not businessZipcode or not businessEmail or not businessCity or not businessState or not businessPhone:
        #     raise Exception("Missing personal data.")
        random_sleep(15)

        write_delay(driver, "#businessName", UserManager.business_name().replace(",",""))
        write_delay(driver, "#businessTaxId", UserManager.ein_number())
        write_delay(driver, "#businessAddressLine1", UserManager.business_address())

        write_delay(driver, "#businessYearTheBusinessBegan", UserManager.year_business_started())
        random_sleep(1)
        write_delay(driver, "#businessAddressCity", UserManager.business_city())
        write_delay(driver, "#businessAddressZipCode", UserManager.business_zipcode())
        send_click(driver, '//select[@id="businessAddressState"]')
        send_click(driver, f'//option[@value="{UserManager.business_state()}"]')
        send_click(driver, "#businessAddressLine2")
        if len(UserManager.business_suite_no()):
            write_delay(driver, '//input[@id="businessAddressLine2"]', UserManager.business_suite_no())
        random_sleep(4)
        send_click(driver, "#businessAddressLine1")
        random_sleep(1)
        write_delay(driver, "#businessPhoneNumber", UserManager.business_phone())
        write_delay(driver, "#businessGrossAnnualSales", UserManager.gross_sales())
        send_click(driver, '//select[@id="businessLegalStructure"]')
        send_click(driver, f'//option[@value="{entityDict.get(UserManager.business_entity())}"]')
        random_sleep(1)
        driver.execute_script("window.scrollBy(0,300)")
        print("Business Industry Type")
        send_click(driver, '//select[@id="businessIndustryType"]')
        random_sleep(1)
        driver.find_element(
            by=By.XPATH, value='//select[@id="businessIndustryType"]'
        ).find_element(
            by=By.XPATH,
            value=f'//option[text()="{businessCategoryDict.get(UserManager.industry_type())}"]',
        ).click()
        send_click(driver, '//select[@id="businessIndustryGroup"]')
        random_sleep(1)
        driver.find_element(
            by=By.XPATH, value='//select[@id="businessIndustryGroup"]'
        ).find_element(
            by=By.XPATH,
            value=f'//option[text()="{businessTypeDict.get(UserManager.industry_type())}"]',
        ).click()
        send_click(driver, '//select[@id="businessIndustrySubGroup"]')
        random_sleep(1)
        driver.find_element(
            by=By.XPATH, value='//select[@id="businessIndustrySubGroup"]'
        ).find_element(
            by=By.XPATH,
            value=f'.//option[text()="{businessSubTypeDict.get(UserManager.industry_type())}"]',
        ).click()
        random_sleep(1)
        Select(
            driver.find_element(By.CSS_SELECTOR, "#businessCountryOfFormation")
        ).select_by_index(1)
        send_click(driver, "#business\.cashAccessChoice1")
        send_click(driver, '//select[@id="businessOwnerTitle"]')
        driver.find_element(
            by=By.XPATH, value='//select[@id="businessOwnerTitle"]'
        ).find_element(
            by=By.XPATH, value=f'.//option[@value="{titleDict.get(UserManager.business_title())}"]'
        ).click()
        write_delay(driver, "#businessOwnerFirstName", UserManager.first_name())
        print("Business Owner First Name")
        if len(UserManager.middle_name()):
            write_delay(driver, "#businessOwnerMiddleName", UserManager.middle_name())
        write_delay(driver, "#businessOwnerLastName", UserManager.last_name())
        write_delay(driver, "#input_businessOwner\.birthDate", UserManager.dob())
        write_delay(driver, "#businessOwnerSocialSecurityNumber", UserManager.ssn())
        write_delay(driver, "#businessOwnerEmailAddress", UserManager.email())
        write_delay(driver, "#businessOwnerPrimaryPhoneNumber", UserManager.phone())
        print("business Owner Primary PhoneNumber")
        random_sleep(1)
        if UserManager.business_address() != UserManager.home_address():
            driver.find_element(
                by=By.XPATH,
                value='//label[@for="businessOwnerAddrDiffToBusinessAddressQuestionAnswer"]',
            ).click()
            random_sleep(1)
            write_delay(driver, "#businessOwnerAddressLine1", UserManager.home_address())
            send_click(driver, '//input[@id="businessOwnerAddressLine2"]')
            if UserManager.suite_no() and len(UserManager.suite_no()):
                write_delay(driver, '//input[@id="businessOwnerAddressLine2"]', UserManager.suite_no())
            send_click(driver, '//input[@id="businessOwnerAddressLine1"]')
            write_delay(driver, "#businessOwnerAddressCity", UserManager.city())
            send_click(driver, '//select[@id="businessOwnerAddressState"]')
            driver.find_element(
                by=By.XPATH, value='//select[@id="businessOwnerAddressState"]'
            ).find_element(by=By.XPATH, value=f'.//option[@value="{UserManager.state()}"]').click()
            write_delay(driver, "#businessOwnerAddressZipCode", UserManager.zipcode())
            send_click(driver, "#businessOwnerAddressLine1")
        print("Business Owner address")
        write_delay(driver, "#businessOwnerTotalAnnualIncome", UserManager.household_income())
        write_delay(
            driver,
            "#businessOwnerPercentageOfBusinessYouOwn",
            data.get("business").get("businessPercent"),
        )
        send_click(driver, "#businessOwnerPercentageOfBusinessYouOwn")
        write_delay(driver, "#assetsUnderCareUuninvestedAssets", "150000")
        write_delay(driver, "#assetsUnderCareInvestedAssets", "150000")
        random_sleep(2)
        print("assetsUnderCareInvestedAssets")
        try:
            send_click(
                driver, "//select[@id='assetsUnderCareYearsWithPartnerNameAccount']"
            )
            driver.find_element(
                by=By.XPATH,
                value="//select[@id='assetsUnderCareYearsWithPartnerNameAccount']",
            ).find_elements(by=By.TAG_NAME, value="option")[1].click()
            send_click(
                driver, "//select[@id='assetsUnderCareMonthsWithPartnerNameAccount']"
            )
            driver.find_element(
                by=By.XPATH,
                value="//select[@id='assetsUnderCareMonthsWithPartnerNameAccount']",
            ).find_elements(by=By.TAG_NAME, value="option")[1].click()
        except:
            pass
        random_sleep(5)
        try:
            driver.find_element(
                By.XPATH,
                value='//input[@id="business.beneficialOwnerAnyoneElseOwnTwentyFivePercentOrMoreChoice2"]',
            ).click()
        except:
            pass

        send_click(driver, "#button\.submitButton")
        print("Screenshot Time123")
        random_sleep(10)

        try:
            driver.find_element(
                by=By.XPATH, value='//*[@id="formElementID"]/button'
            ).click()
        except:
            pass
        # send_click(driver, '//*[@id="formElementID"]/button')
        random_sleep(1)
        retry_counter = 0
        while retry_counter < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value="//*[contains(text(),'Thank you for applying.')]"
                )
                break
            except:
                retry_counter += 1
                random_sleep(0.1)
        print("Screenshot Time")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Flushing Business Card"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except:
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Flushing Business Card"

        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
