from selenium import webdriver

# Replace these with your website's login page URL and your login credentials
login_url = "https://example.com/login"
username = "your_username"
password = "your_password"

# Create a new instance of the Chrome web driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find the username and password fields and fill them with your credentials
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Wait for the page to load and confirm login
driver.implicitly_wait(10)
if driver.current_url == "https://example.com/dashboard":
    print("Login successful!")
else:
    print("Login failed.")

# Close the web driver
driver.quit()
