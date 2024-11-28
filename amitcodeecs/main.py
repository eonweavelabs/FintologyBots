from Utils.spawn_driver import start
from Utils.select_card import select_card
from Utils.proxy_auth import create_ip_auth, delete_ip_auth
import os
import socket, pyvirtualdisplay
import logging
import sys, json
import traceback
from Utils.constants import DEV_MACHINE_NAME
from Utils.database_queries import fetch_user_json
from Utils.pre_process_user import pre_process_user
from Utils.data_extraction import UserManager

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def controller(application_id=None, product_id=None, card_name=None):
    try:
        # Start virtual display if not on the development machine
        if socket.gethostname() not in DEV_MACHINE_NAME:
            display = pyvirtualdisplay.Display(visible=0, size=(1920, 1080))
            display.start()

        logger.info("Task start.")
        # Fetch environment variables if arguments are not provided
        if application_id is None:
            product_id = os.getenv("product_id")
            application_id = os.getenv("application_id")
            card_name = os.getenv("card_name")

        logger.info(f"application_id is {application_id}")
        logger.info(f"product_id is {product_id}")
        logger.info(f"card_name is {card_name}")

        # Fetch user JSON
        user = fetch_user_json(application_id)
        if user is None:
            logger.error("Failed to fetch user JSON. Task Aborted.")
            return

        # Pre-process user data
        try:
            user = pre_process_user(user)
            UserManager.set_user_data(user)
        except Exception as e:
            logger.error(f"Error during user pre-processing: {e}", exc_info=True)
            return

        # Create IP authentication and start the driver
        id = create_ip_auth()
        driver = start()

        # Select the card
        res = select_card(driver, user, product_id, card_name)

        # Clean up the IP auth and driver
        delete_ip_auth(id)
        driver.quit()

        if res is True:
            logger.info("Card selection was successful.")

        logger.info("Task Finished")

    except Exception as e:
        logger.error(f"Task Aborted. Error: {e}", exc_info=True)

        # Ensure IP auth and driver are cleaned up in case of an error
        try:
            delete_ip_auth(id)
        except Exception as cleanup_error:
            logger.warning(f"Error during IP auth cleanup: {cleanup_error}", exc_info=True)

if __name__ == "__main__":
    controller()
