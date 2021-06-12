# -*- coding: utf-8 -*-

#python3
#
# main script
#
# 2021/06/11
# author
# hirokazu niimoto

#PIPinstallを動的にする
#参考：https://qiita.com/fumitoh/items/f6a4577e263c3791c868
import pip, site, importlib

def install_packege():
    print(  "  install some necessaly package plese wait...")
    package = ["colorama","tqdm","webdriver-manager",'msedge-selenium-tools']
    for i in range(len(package)):
        pip.main(['install','--user', package[i]])  # pip install --user modelx を実行
        importlib.reload(site)

def regist_github():
    print("  Please set up your github acount")
    github_user_name = input("  user_name:")
    github_user_password = input("  password:")

    github_user = "user_name = '" + github_user_name + "' \n" + "user_password = '" + github_user_password + "'"
    with open('conf.py', 'w', encoding='utf-8') as f:
        f.write(github_user)

    print("  OK")




if __name__ == '__main__':
    while 1:
        setup_type = input('  Select setup type "install and setup"(f) (You need to do first)  or "install only" (i) or "setup only" (s). And typing "q" is stop this program:')
        if setup_type == "install and setup" or setup_type == "f":
            regist_github()
            install_packege()
            exit()
        elif setup_type == "install only" or setup_type == "i":
            install_packege()
            exit()

        elif setup_type == "setup only" or setup_type == "s":
            regist_github()
            exit()
        elif setup_type == "q":
            exit()
        else:
            print("  ! Please input correct type")
            print("\n")
