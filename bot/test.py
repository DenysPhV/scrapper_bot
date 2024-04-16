import time
from seleniumbase import BaseCase

class TestsCase(BaseCase):
    def test_open_page(self):
         self.get_current_url("https://go.seated.com/tour-events/ee8effe7-d205-403c-a39f-007a83ac9629")

         self.assert_title("Twenty One Pilots Tickets - Orlando, FL - Kia Center - Wed, Sep 11 2024 | Seated | a Sofar artist service")
  
