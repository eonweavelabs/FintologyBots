from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback
from selenium.webdriver.support.ui import Select

# -----------------------------------------------------------------
# Lendini
# -----------------------------------------------------------------

def lendini(driver, data, product_id):
    try:
        driver.get("https://fundingmetrics.my.salesforce-sites.com/MerchantPortal/Application")
        random_sleep(15)
        
        personal = data.get("personal")
        first_name = personal.get("first_name")
        last_name = personal.get("last_name")
        phone = personal.get("phone")
        email = personal.get("email")
        company = personal.get("company")
        industry = personal.get("industry")
        company_address = personal.get("company_address")
        company_city = personal.get("company_city")
        company_state = personal.get("company_state")
        company_zip_code = personal.get("company_zip_code")
        gross_annual_sales = personal.get("gross_annual_sales")
        amount_requested = personal.get("amount_requested")

        random_sleep(20)
        
        # Business Information
        driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="j_id0:form:j_id41"]', first_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id43"]', last_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id45"]', phone)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id47"]', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id49"]', company)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id51"]', industry)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id53"]', company_address)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id55"]', company_city)
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="j_id0:form"]/div[5]/div[1]/div/div/select'
                )
                select = Select(select_element)
                select.select_by_value(company_state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:j_id110"]', company_zip_code)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:Gross_Annual_Sales__c"]', gross_annual_sales)
        random_sleep(1)
        write_delay(driver, '//*[@id="j_id0:form:Amount_Requested__c"]', amount_requested)
        random_sleep(1)
        send_click(driver, '//*[@id="j_id0:form"]/div[7]/center/input')  # APPLY NOW
        random_sleep(10)
        
        card_name = "Lendini"
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
        card_name = "Lendini"
        filepath = f"FinalScreenshots/business/{first_name} {last_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
