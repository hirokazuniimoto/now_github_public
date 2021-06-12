# -*- coding: utf-8 -*-

#python3
#
# main script
#
# 2021/06/11
# author
# hirokazu niimoto

#seleniumは同じディレクトリから（ログを非表示にするため)
#参考：https://yuki.world/windows-selenium-headlesschrome-log-hide/
from selenium import webdriver
import time
#import pyautogui as pgui
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
import os
#色付けライブラリ（Windows初期化）
from colorama import init
init()
#色付けライブラリ
from colorama import Fore, Back, Style
#Progress Bar
import tqdm
from tqdm import tqdm

#ドライバーを自動更新
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


#プログラムライブラリ
from lib import login_github
from lib import windowsPATH_to_linux
from lib import aa_print
#import setting
import conf

user_name = conf.user_name
user_password = conf.user_password

rep_names = {}
rep_name = ""
dir_names = {}
file_names = []
dir_name = ""
file_name = ""

branch = "master"
dir = ""

# Chrome Optionsの設定
options = Options()
options.add_argument('--headless')                 # headlessモードを使用する
options.add_argument('--disable-gpu')              # headlessモードで暫定的に必要なフラグ(そのうち不要になる)
options.add_argument('--disable-extensions')       # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument('--proxy-server="direct://"') # Proxy経由ではなく直接接続する
options.add_argument('--proxy-bypass-list=*')      # すべてのホスト名
options.add_argument('--start-maximized')

#Chromeを指定
#executable_path="C:/Users/kazum/Desktop/chromedriver_win32 (1)/chromedriver.exe"
driver_flag = 1

try:
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
except Exception as e:
    driver_flag = 0

if driver_flag == 0:
    #Edge headless
    from msedge.selenium_tools import Edge, EdgeOptions
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('--headless')
    options.add_argument("disable-gpu")
    try:
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),options=options)
    except Exception as e:
        driver_flag = 1

if driver_flag == 1:
    #Firefox headless
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.headless = True

    try:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
    except Exception as e:
        driver_flag = 2

if driver_flag == 2:
    #Edge headless
    from msedge.selenium_tools import Edge, EdgeOptions
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('--headless')
    options.add_argument("disable-gpu")
    try:
        driver = webdriver.Chrome(EdgeChromiumDriverManager().install(),options=options)
    except Exception as e:
        driver_flag = 4


try:
    driver
except NameError:
    # なかった場合の処理
    print("  webドライバーに問題があります。")
    exit()


driver.implicitly_wait(10) # 秒


def get_repositories():
    #指定したURLに遷移する
    driver.get("https://github.com/" + user_name + "?tab=repositories")
    #time.sleep(2)
    repositories = driver.find_elements_by_class_name('wb-break-all')
    #print(fruits[3].text)
    i=0
    for repository in repositories:
        i+=1
        rep_name = user_name + "/" + repository.text
        rep_name = rep_name.replace('Private','')
        rep_name = rep_name.replace('Public','')
        rep_name = rep_name.rstrip(' ')
        print("  " + Fore.RED + str(i) + " " + Fore.GREEN  + rep_name +  Style.RESET_ALL)
        #rep_names.append(rep_name)
        rep_names[i] = rep_name



def select_repositories():

    #リポジトリの一覧を表示
    #core.get_repositories(driver,user_name)
    get_repositories()

    #最初のループ
    threads = [] #生成したスレッドオブジェクトを格納するためのリスト
    while 1:
        #print('  Please select repository number :'  )
        print("\n")
        flag = input('  Please select repository number. And typing "0" is stop this program:')
        print("\n")

        # TODO: 例外処理
        try:
            if int(flag) in rep_names:

                global rep_name
                rep_name = rep_names[int(flag)]

                global branch
                branch = input('  Please choose branch. And if you did not write any name, branch is default branch "main":')
                if branch.strip() == "":
                    branch = "main"
                #dir_names = core.get_dirs_first(driver,int(flag) , "master")
                #dir_names = get_dirs_first(int(flag) , "master")

                #指定したURLに遷移する
                driver.get("https://github.com/" + rep_names[int(flag)] + "/find/" + branch)
                #time.sleep(2)

                break
            elif int(flag) == 0:
                print("  OK, see you again!")
                exit()
            else:
                #print("\n")
                print(Fore.RED + "  Your input number is not exist. Please try again." + Style.RESET_ALL)
        except Exception as e:
            #print("\n")
            print(Fore.RED + "  Your input number is not exist. Please try again." + Style.RESET_ALL)


def select_and_get_file():

    while 1:
        #print('  Please select repository number :'  )
        #print("\n")
        memo = '  Please write file_name. If you choose more than one, use a space (ex:"script.py dir/index.html"). And typing "q" is stop this program:'
        flag_3 = list(map(str,input(memo).split()))
        #flag_3 = input('  Please write file_name. If you type more than one, please use a space (ex:"script.py index.html"). And typing "q" is stop this program:')
        print("\n")

        if flag_3[0] == "q":
            print("  OK, see you again!")
            exit()
        else:
            try:
                for i in range(len(flag_3)):
                    #指定したURLに遷移する
                    driver.get("https://github.com/" + rep_name +"/blob/" + branch + "/" + flag_3[i])
                    # 3秒待ちます
                    #time.sleep(3)
                    for t in tqdm(range(10)):
                        time.sleep(0.3)

                    element = driver.find_element_by_xpath('//*[@id="raw-url"]')
                    #リンクをクリック
                    element.click()


                    linux_path_create = windowsPATH_to_linux.WindowPATH_to_linux(flag_3[i])
                    flag_3[i] = linux_path_create.windowsPATH_to_linux()

                    if "/" in flag_3[i]:
                        pos = flag_3[i].find('/')
                        dir_name = flag_3[i][:pos]
                        file_name = flag_3[i][pos:]
                        print('NEW_WORK!/'+dir_name)
                        os.makedirs('NEW_WORK!/'+dir_name, exist_ok=True)
                        dir_name = "NEW_WORK!/"+dir_name + file_name
                    else:
                        dir_name = "NEW_WORK!/" + flag_3[i]

                    html_body = driver.find_element_by_tag_name("body").text

                    with open(dir_name, 'w', encoding='utf-8') as f:
                        f.write(html_body)
                        print('  saved ' + Fore.YELLOW + dir_name + Style.RESET_ALL)
                        print('\n')
                break

            except Exception as e:
                print(Fore.RED + "  Your input file name is not exist. Please try again." + Style.RESET_ALL)


if __name__ == '__main__':
    welcome = aa_print.AA_PRINT()
    welcome.AA_print()

    login = login_github.Login_to_github()
    login.login(driver,user_name,user_password)

    select_repositories()
    select_and_get_file()

    print("\n")
    print(Fore.CYAN + '  Success! Thank you for use.' + Style.RESET_ALL)
