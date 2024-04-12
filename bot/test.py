from seleniumbase import Driver

driver = Driver(uc=True)
try:
    driver.get("https://go.seated.com/tour-events/ee8effe7-d205-403c-a39f-007a83ac9629")
    driver.sleep(4)
finally:
    driver.quit()