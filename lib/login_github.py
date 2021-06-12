#python3
#
# user login for github
#
# 2021/06/11
# author
# hirokazu niimoto

class Login_to_github(object):

    def login(self,driver,user_name,user_password):
        #指定したURLに遷移する
        driver.get("https://github.com/login?")

        #time.sleep(5)
        element_email_input = driver.find_element_by_xpath('//*[@id="login_field"]')
        element_pass_input = driver.find_element_by_xpath('//*[@id="password"]')


        element_email_input.send_keys(user_name)
        element_pass_input.send_keys(user_password)

        element_login = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]')
        element_login.click()
