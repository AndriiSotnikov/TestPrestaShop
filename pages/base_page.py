class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    def get_page_title(self):
        return self.title.text

    def get_url(self):
        return self.driver.current_url
