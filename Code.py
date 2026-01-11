from selenium import webdriver

# Initialize Chrome browser
driver = webdriver.Chrome()
driver.get("https://example.com")
print(f"Page Title: {driver.title}")

# Close the browser
driver.quit()
