import undetected_chromedriver as webdriver
from Utils.constants import proxylist, DEV_MACHINE_NAME
from random import choice
import socket

def start(page_load_strategy="none"):
    proxy = choice(proxylist)
    chrome_options = webdriver.ChromeOptions()

    # Chrome binary location for Linux/Ubuntu-based systems
    chrome_options.binary_location = "/usr/bin/google-chrome"

    # Add required options
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument("--force-device-scale-factor=1")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    # Set proxy if required
    chrome_options.add_argument(f'--proxy-server={proxy}')

     #Check if the current machine is a development machine
    if socket.gethostname() not in DEV_MACHINE_NAME:
        driver = webdriver.Chrome(options=chrome_options, version_main=131)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    
    return driver
