class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://example.com/login")

    def login(self, username, password):
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "login").click()

    def is_logged_in(self):
        return "dashboard" in self.driver.current_url
