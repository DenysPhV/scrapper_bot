import time
from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://go.seated.com/tour-events/331bafd0-68de-450c-ba3e-90f11d3114fc"
driver.get(url)

time.sleep(6)

driver.click('a[href="/event-reminders/bd3cd050-bda1-4b4f-9ef4-c65dd632b1c1"]')

time.sleep(3)

driver.type('input[data-test-first-name]', "Ваше имя")
driver.type('input[data-test-last-name]', "Ваша фамилия")
driver.type('input[data-test-email]', "example@example.com")

driver.click('button[type="submit"]')


driver.quit()

