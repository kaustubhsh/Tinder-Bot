from selenium import webdriver
from time import sleep
from details import username,password

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):

        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except Exception:
                return None
            return element
        self.driver.get('https://tinder.com/')
        sleep(10)
        cookie_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookie_accept.click()
        #click on more options
        try:
            more_op = check_exists_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
            more_op.click()
        finally:
            # FB_click
            # fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
            fb_btn= self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
            fb_btn.click()
        # self.driver.refresh()
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.window_handles[1]
        self.driver.switch_to_window(popup_window)
        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()


    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Like"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Nope"]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_tinder_plus()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    def close_tinder_plus(self):
        tinder_plus_popup =  self.driver.find_element_by_xpath('//span[text()="No Thanks"]')
        tinder_plus_popup.click()
        self.driver.quit()
        exit(0)


bot = Tinderbot()
bot.login()
bot.auto_swipe()