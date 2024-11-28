from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# ------------------------------------------------------
# Revup Capital
# ------------------------------------------------------

def revupCapital(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "companyName": "Example Company",
        #     "companyWebsite": "https://example.com",
        #     "headquarters": "Example City",
        #     "fullNameTitle": "Neha LastName, CEO",
        #     "aboutCompany": "We are a tech startup.",
        #     "revenueModel": "Subscription-based",
        #     "previousRevenue": 1000000,
        #     "revenueGoals": 2000000,
        #     "linkedinProfiles": "https://linkedin.com/in/example",
        #     "additionalMaterials": "https://example.com/pitch",
        #     "referralSource": "LinkedIn",
        #     "otherInfo": "Looking forward to working with you."
        # }
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe3LjCpDBUnVtd2IgNvZvV_uRC8mZJ0sioFCN2ZfFiLeGpvjQ/viewform")
        random_sleep(15)

        email = data.get("email")
        companyName = data.get("companyName")
        companyWebsite = data.get("companyWebsite")
        headquarters = data.get("headquarters")
        fullNameTitle = data.get("fullNameTitle")
        aboutCompany = data.get("aboutCompany")
        revenueModel = data.get("revenueModel")
        previousRevenue = data.get("previousRevenue")
        revenueGoals = data.get("revenueGoals")
        linkedinProfiles = data.get("linkedinProfiles")
        additionalMaterials = data.get("additionalMaterials")
        referralSource = data.get("referralSource")
        otherInfo = data.get("otherInfo")

        # Fill the form fields
        # write_delay(driver, '//*[@id="wSDd7b"]', email)
        # random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', companyName)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', companyWebsite)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', headquarters)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', fullNameTitle)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', aboutCompany)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea', revenueModel)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input', previousRevenue)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input', revenueGoals)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input', linkedinProfiles)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea', additionalMaterials)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input', referralSource)
        random_sleep(1)
        write_delay(driver, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[2]/textarea', otherInfo)
        random_sleep(1)

        # Submit the form
        send_click(driver, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        random_sleep(1)

        # Screenshot and upload
        full_name = fullNameTitle.split(",")[0]
        card_name = "Revup Capital"
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
        full_name = data.get("fullNameTitle").split(",")[0]
        card_name = "Revup Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
