from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# import time

"""make your requests look more like they are coming from a real human user, 
and less like they are coming from a bot.
techniques you can use to avoid getting your IP address blocked when using 
Selenium:
1. Use a rotating proxy service
2. Use a delay between requests - using the time.sleep() function
3. Use a user-agent switcher
4. Mimic human behavior:- 
    You can mimic human behavior by introducing randomness in your code, such 
    as randomizing the order in which you interact with page elements.
    For example, instead of always clicking on the same button in the same order, you can use Python's random module to
     randomize the order in which you click on buttons. You can also add a random delay between actions to further 
     increase the randomness of your requests.
     # Example:
        buttons = driver.find_elements_by_xpath("//button")

        # shuffle the order of the buttons
        random.shuffle(buttons)

        # click on the buttons in random order
        for button in buttons:
            button.click()
            # add a random delay between clicks
            time.sleep(random.uniform(1, 3))
            
    #  you can make your requests less predictable and more like those of a human user.
     """

# 1.
# a list of IP addresses and ports for the rotating proxy service
# Hides your IP address, Bypass geo-restrictions, Security
proxy_list = ["167.172.226.251:443", "49.0.2.242:8090", "190.61.88.147:8080"]

random.shuffle(proxy_list)
for proxy in proxy_list:
    # Set up the proxy
    PROXY = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy,
        'ftpProxy': proxy,
        'sslProxy': proxy,
        'noProxy': ''
    })

PATH = "C:\ChromeDriver\chromedriver.exe"
service = Service(PATH)

# 3.
# use a user-agent switcher
"""Websites may also detect automated requests based on the user-agent header sent 
by the browser. You can use a user-agent switcher to mimic the user-agent 
of a real browser."""
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

driver = webdriver.Chrome(service=service, options=options,
                          desired_capabilities=webdriver.DesiredCapabilities.CHROME)
# driver.install_addon("path/to/switchyomega.crx") # Optional - if you're using a Chrome extension to manage proxies

driver.get("https://www.ebay.com/sh/research?marketplace=EBAY-US&keywords=pokemon+cards&dayRange=365&endDate=1676256151596&startDate=1644720151596&categoryId=0&offset=0&limit=50&sorting=-datelastsold&tabName=SOLD&tz=Asia%2FSingapore")

print(driver.title)
input("If there is a security measure, You have to fill it manually to continue"
      "Solve the security measure and enter Y in the command terminal  and press enter to continue"
      ""
      "If there is no security measure just simply pres Y and press enter to continue.")

#
# # solve for captcha security check by user
# if "Scurity" in driver.title:
#     captcha_solved = False
#     while not captcha_solved:
#         print("In loop first")
#         try:
#             # Wait for the captcha or security verification check to be visible
#             captcha = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "anchor")))
#             print("In loop middle")
#
#             # Verify that the captcha or security verification check has been solved
#             captcha_solved = True
#
#             # Wait for the user to solve the captcha or security verification check
#             captcha_input = input("Please solve the captcha and press Enter to continue...")
#
#
#         except:
#             print("In loop last")
#             # If the captcha or security verification check is not visible, wait for a short time and try again
#             time.sleep(5)


# 2.
"""
# Navigate to another page:
import time # should be imported above the script.

time.sleep(5)

# Navigate to another page
driver.get('https://www.example.com/page2')

will pause the program for 5 seconds before continuing to make the 
second request.
"""


# ___fill in a login form and log in to a page____

# Wait for the username and password input fields to be visible
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'userid')))

# Fill in the username input field
userid = input("Enter username or email:\n")
username.send_keys(userid)

try:
    # Click on the "continue" button
    continue_button = driver.find_element_by_css_selector('button[type="submit"]')
    continue_button.click()

    print("User id worked!")
except:
    print("User id does not exist in database. Ensure your user id is correct.")

# Wait for the password input field to be visible
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

# Fill in the password input field
Password = input("Enter your password:\n")
password.send_keys(Password)

# Submit the login form
login_form = driver.find_element_by_tag_name('form')
login_form.submit()


input("Press any key to exit.")
driver.quit()
