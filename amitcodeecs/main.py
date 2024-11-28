import os
import sys
import socket
import logging
import traceback
import pyvirtualdisplay
from Utils.spawn_driver import start
from Utils.select_card import select_card
from Utils.proxy_auth import create_ip_auth, delete_ip_auth
from Utils.constants import DEV_MACHINE_NAME
from Utils.database_queries import fetch_user_json
from Utils.pre_process_user import pre_process_user
from Utils.data_extraction import UserManager

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("main")

def controller(application_id=None, product_id=None, card_name=None):
    try:
        if socket.gethostname() not in DEV_MACHINE_NAME:
            display = pyvirtualdisplay.Display(visible=0, size=(1920, 1080))
            display.start()

        logger.info("Task start.")
        application_id = application_id or os.getenv("application_id")
        product_id = product_id or os.getenv("product_id")
        card_name = card_name or os.getenv("card_name")

        logger.info(f"application_id is {application_id}")
        logger.info(f"product_id is {product_id}")
        logger.info(f"card_name is {card_name}")

        user = fetch_user_json(application_id)
        if not user:
            raise ValueError(f"Application with id {application_id} not found.")
        user = pre_process_user(user)
        UserManager.set_user_data(user)

        id = create_ip_auth()
        driver = start()
        result = select_card(driver, user, product_id, card_name)
        delete_ip_auth(id)
        driver.quit()

        if result:
            logger.info("Task completed successfully.")
        else:
            logger.warning("Task failed.")
    except Exception as e:
        logger.error(f"Error in task: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    controller()
