import os
from time import sleep, time
import random


#################################################


## Colours
red = '\033[91m'
green = '\033[92m'
yellow = '\033[33m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
black = '\033[30m'
dgrey = '\033[1;30m'
red2 = '\033[0;31m'
red3 = '\033[1;33m'
green2 = '\033[0;32m'
green3 = '\033[1;32m'
brownorange = '\033[0;33m'
yellow2 = '\033[1;33m'
blue2 = '\033[0;34m'
blue3 = '\033[1;34m'
purple2 = '\033[0;35m'
purple3 = '\033[1;35m'
cyan2 = '\033[0;36m'
cyan3 = '\033[1;36m'
grey2 = '\033[0;37m'
white2 = '\033[1;37m'
rm = '\033[0m'


#################################################


def banner():
    print("\033[1;31m")
    logoList = ["lion", "skull", "lion", "lion"]
    logo = random.choice(logoList)

    if logo=='lion':
        os.system('bash banner/img2text.sh banner/lion.jpg')
    elif logo=='skull':
        os.system('bash banner/img2text.sh banner/skull.jpg')

    os.system('bash banner/banner.sh')

    print("\033[0;37;40m")


#################################################


def custom_main():
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0

printf '\033[1;32m'

echo -n "{CU570M CMD"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO CUSTOM COMMAND MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')
    print(f"{red3}   |__»» [*] 1. {green3}Back to Custom Commands {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 2. {green3}Main Menu               {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 3. {green3}Exit                    {rm}\033[0;31m)")
    print(f"{red3} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '1':
            custom_cmd()
            break
        elif choice == '2':
            main()
            break
        elif choice == '3':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def custom_cmd():
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0

printf '\033[1;32m'

echo -n "{CU570M CMD"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO CUSTOM COMMAND MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')
    print(f"{red3}   |__»» [*] 1. {green3}apt update           {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 2. {green3}apt upgrade          {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 3. {green3}apt install          {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 4. {green3}cd $PREFIX           {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 5. {green3}cd $HOME             {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 6. {green3}apt show             {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*]                                         {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 9. {green3}Main Menu            {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 0. {green3}Exit                 {rm}\033[0;31m)")
    print(f"{red3} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '1':
            print(f"{red3}   |__»» [×] {green3}Custom name for *apt update* Ex = apu {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>      {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : ap u ->> apu  {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/apt-update ')
            os.system(f'mv helper/apt-update helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '2':
            print(f"{red3}   |__»» [×] {green3}Custom name for *apt upgrade* Ex = apug {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>        {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : ap ug ->> apug  {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/apt-upgrade ')
            os.system(f'mv helper/apt-upgrade helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '3':
            print(f"{red3}   |__»» [×] {green3}Custom name for *apt install* Ex = apin {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>        {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : ap in ->> apin  {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/apt-install ')
            os.system(f'mv helper/apt-install helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '4':
            print(f"{red3}   |__»» [×] {green3}Custom name for *cd $PREFIX* Ex = usr-ja {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>            {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : usr- ja ->> usr-ja  {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/cd-root ')
            os.system(f'mv helper/cd-root helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '5':
            print(f"{red3}   |__»» [×] {green3}Custom name for *cd $HOME* Ex = home-ja {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>               {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : home -ja ->> home-ja   {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/cd-home ')
            os.system(f'mv helper/cd-home helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '6':
            print(f"{red3}   |__»» [×] {green3}Custom name for *apt show* Ex = apsh {rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM NAME: ")
            if " " in cmd_input:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>        {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : ap sh ->> apsh  {rm}\033[0;31m)")
                cmd_input = cmd_input.replace(" ", "")
            os.system('chmod +x helper/apt-show ')
            os.system(f'mv helper/apt-show helper/{cmd_input}')
            os.system(f'cp helper/{cmd_input} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {cmd_input} ->>{rm}\033[0;31m)\n\n")
            custom_main()
            break

        elif choice == '9':
            main()
            break
        elif choice == '0':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def user_custom_main():
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0

printf '\033[1;32m'

echo -n "{CU570M CMD"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO CUSTOM COMMAND CREATION MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')
    print(f"{red3}   |__»» [*] 1. {green3}Back to Custom Commands Creation {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 2. {green3}Main Menu                        {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 3. {green3}Exit                             {rm}\033[0;31m)")
    print(f"{red3} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '1':
            user_custom_cmd()
            break
        elif choice == '2':
            main()
            break
        elif choice == '3':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def user_custom_cmd():
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0

printf '\033[1;32m'

echo -n "{CU570M CMD"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO CUSTOM COMMAND CREATION MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')
    print(f"{red3}   |__»» [*] 1. {green3}Create Custom CMD/HANDLER{rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 2. {green3}Main Menu                {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 3. {green3}Exit                     {rm}\033[0;31m)")
    print(f"{red3} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '1':

            print(f"{red3}   |__»» [×] {green3}Type Custom Command Ex = apt update   {rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}NOTE <-> PLEASE TYPE COMMAND CAREFULLY{rm}\033[0;31m)")
            cmd_input = input("\033[0;37m   |_»»  ENTER YOUR CMD: ")
            print(f"{red3}   |__»» [×] {green3}OK PROCESSING...   ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Type Custom Command Ex = aptup        {rm}\033[0;31m)")
            custom_cmd = input("\033[0;37m   |_»»  ENTER YOUR CUSTOM CMD: ")

            if " " in custom_cmd:
                print(f"{red3}   |__»» [×] {green3}SPACES ARE NOT ALLOWED ->>          {rm}\033[0;31m)")
                print(f"{red3}   |__»» [×] {green3}REMOVING SPACES : apt up ->> aptup  {rm}\033[0;31m)")
                custom_cmd = custom_cmd.replace(" ", "")

            os.system(f"touch helper/{custom_cmd}")

            content = f'''
#!/bin/bash
echo -e "{green3}Performing {red3}<< {cmd_input} >>{rm}"
{cmd_input}
'''
            with open(f'helper/{custom_cmd}', 'w') as cmd_file:
                cmd_file.write(content)

            os.system(f'chmod +x helper/{custom_cmd}')
            os.system(f'cp helper/{custom_cmd} $PREFIX/bin')
            print(f"{red3}   |__»» [×] {green3}DONE ->>{rm}\033[0;31m)")
            print(f"{red3}   |__»» [×] {green3}Test Uses:$ {custom_cmd} ->> $ {cmd_input} {rm}\033[0;31m)\n\n")
            user_custom_main()
            break
        elif choice == '2':
            main()
            break
        elif choice == '3':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def help():
    banner()
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{H31P"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO TOOL HELP MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')

    print("\033[1;32;40m", end="")
    print('''\033[91m   |\033[0;37;40m
\033[91m   |~==>> \033[0;36mWELCOME TO MY SCRIPT SHIFT TOOL
\033[91m   |      \033[0;36mAUTHOR = HR~MAFIA
\033[91m   |      \033[0;36mTELEGRAM = t.me/hr_mafia
\033[91m   |      \033[0;36mTHE AUTOMATION SCRIPT TO MAKE CUSTOMISED SHELL COMMANDS
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mScript Shift, your go-to tool for customizing shell commands with
\033[91m   |      \033[0;36mease and flair. Transform your command line experience by creating
\033[91m   |      \033[0;36mmemorable, short aliases for your most-used commands.
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mGETTING STARTED !!
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mInstallation:
\033[91m   |      \033[0;36m- Ensure Script Shift is properly installed in your system. If not,
\033[91m   |      \033[0;36mfollow the installation guide provided with the tool.
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mCreating Custom Commands:
\033[91m   |      \033[0;36m- Script Shift allows you to create custom cmd's, which will serve
\033[91m   |      \033[0;36mas your new, Just go to the CUSTOM COMMAND MENU and create your own
\033[91m   |      \033[0;36mcustom commands (e.g., `aptup` for `apt update`).
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mCreating Your Own Custom Commands:
\033[91m   |      \033[0;36m- Script Shift allows you to create your custom cmd's for your custom
\033[91m   |      \033[0;36mcustom shell command, which will serve as your new, Just go to the
\033[91m   |      \033[0;36mYOUR CUSTOM COMMAND MENU and create your own custom commands with
\033[91m   |      \033[0;36mcustom shell command. (e.g., `aptup` for `apt update`).
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mNOW HOW THE SCRIPT WORKS !!
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mHow you can do this task manually:
\033[91m   |      \033[0;36m— The Steps that the tool run automatically in the backend is ~
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mCreating Custom Command Files:
\033[91m   |      \033[0;36mFirst you have to create a file without any extention, you can use
\033[91m   |      \033[0;36mthis cmd ->> \033[0;31m[× touch "command_name" ×] [× Ex -> touch aptin ×]
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mGiving Executable Permissions:
\033[91m   |      \033[0;36m- After creating your custom command files, you'll need to grant
\033[91m   |      \033[0;36mthem executable permissions. You can do this by running:
\033[91m   |      \033[0;36m\033[0;31m[× chmod +x /path/to/your/custom_command ×] [× Ex -> chmod +x aptin ×]
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mWriting Main Content to the Custom Command File:
\033[91m   |      \033[0;36mYou have to specify the content of the custom command file, so it can
\033[91m   |      \033[0;36mruns your command with custom name:
\033[91m   |      \033[0;36mWrite the content like this:
\033[91m   |      \033[0;36mSample : File name = custom_name
\033[91m   |      \033[0;36m\033[0;31m[× #!/bin/bash/                              ×]
\033[91m   |      \033[0;36m\033[0;31m[× "at this line you can type your command"  ×]
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36mExample : File name = aptin (custome cmd name)
\033[91m   |      \033[0;36m\033[0;31m[× #!/bin/bash/                              ×]
\033[91m   |      \033[0;36m\033[0;31m[× apt install                               ×]
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36mThen save the file Content +
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mMoving Commands to the /bin/ Directory:
\033[91m   |      \033[0;36m- To make your custom commands globally accessible, move them to the
\033[91m   |      \033[0;36m/bin/ directory: /033[0;31m[× mv custom_command $PREFIX/bin/ ×]
\033[91m   |      \033[0;36m\033[0;31m[× Ex - mv aptin $PREFIX/bin/ ×]
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36m\033[1;37m<<-- DONE -- THE CUSTOM COMMAND IS SUCCESSFULLY SETTED -->>
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mUsage:
\033[91m   |      \033[0;36m- To use your custom commands, simply type the name of your newly
\033[91m   |      \033[0;36mcreated command in the terminal. For example, \033[0;31m[× aptin ×] to
\033[91m   |      \033[0;36mrun \033[0;31m[× apt install ×]
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36mExample: [× \033[0;31maptin git -y ×]
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mSupport:
\033[91m   |      \033[0;36m- For additional help or to report issues, please contact our support
\033[91m   |      \033[0;36mteam or visit our GitHub repository.
\033[91m   |\033[0;37;40m''')

    print("\033[91m   |\033[0;37;40m")
    print(f"{red}   |__»» [*] 0. {green}MAIN MENU                   {rm}\033[0;31m)")
    print(f"{red}   |__»» [*] 1. {green}Exit                        {rm}\033[0;31m)")
    print(f"{red} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '0':
            main()
            break
        elif choice == '1':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def aboutMe():
    banner()
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{A80U7"
sleep 0.1

echo -n " M3}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO ABOUT US MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')

    print("\033[1;32;40m", end="")
    print('''\033[91m   |\033[0;37;40m
\033[91m   |~==>> \033[0;36mWELCOME TO MY ABOUT US
\033[91m   |      \033[0;36mAUTHOR = HITESH / HR MAFIA >>=-=>> THE OWNER OF THIS TOOL
\033[91m   |      \033[0;36mTELEGRAM = t.me/hr_mafia && t.me/Hiteshbro
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mOUR COMMUNITY == SUDO WORLD <<=+=>> A Group of Ethical Hackers
\033[91m   |~==>> \033[0;36mJOIN US NOW:
\033[91m   |      \033[0;36mTELEGRAM CHAMNEL = t.me/sudo_world_channel
\033[91m   |      \033[0;36mTELEGRAM CHATGROUP = t.me/sudo_world
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36msudo WORLD is a community of Hackers, where we teach CyberSecurity and
\033[91m   |      \033[0;36mEthical Hacking for free.
\033[91m   |      \033[0;36mWe are a team of cybersecurity/ethical hacking experts with knowledge
\033[91m   |      \033[0;36min many fields.
\033[91m   |      \033[0;36m
\033[91m   |      \033[0;36m[×] ETHICAL HACKING                              ]
\033[91m   |      \033[0;36m[×] CYBERSECURITY DETAILS			   ]
\033[91m   |      \033[0;36m[×] WEB PENTESTING				   ]
\033[91m   |      \033[0;36m[×] ANDROID PENTESTING			   ]
\033[91m   |      \033[0;36m[×] PYTHON DEVELOPERS			   	   ]
\033[91m   |      \033[0;36m[×] AI ENGINEERS				   ]
\033[91m   |      \033[0;36m[×] AI MANIPULATION				   ]
\033[91m   |      \033[0;36m[×] CHATBOT BUILDING			   	   ]
\033[91m   |      \033[0;36m[×] TELEGRAM BOT BUILDING			   ]
\033[91m   |      \033[0;36m[×] WHATSAPP BOT BUILDING			   ]
\033[91m   |      \033[0;36m[×] AI BOTS					   ]
\033[91m   |      \033[0;36m[×] PROMPT ENGINEERING/MANIPULATION TECHNIQUES   ]
\033[91m   |      \033[0;36m[×] MANY MORE +++++++			       	   ]
\033[91m   |      \033[0;36m
\033[91m   |~==>> \033[0;36mSupport:
\033[91m   |      \033[0;36m- For additional help or to report issues, please contact our support
\033[91m   |      \033[0;36mteam or visit our GitHub repository.
\033[91m   |\033[0;37;40m''')

    print("\033[91m   |\033[0;37;40m")
    print(f"{red}   |__»» [*] 0. {green}MAIN MENU                   {rm}\033[0;31m)")
    print(f"{red}   |__»» [*] 1. {green}Exit                        {rm}\033[0;31m)")
    print(f"{red} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '0':
            main()
            break
        elif choice == '1':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


def main():
    os.system('clear')
    banner()
    print(blue2)
    os.system('''
echo -n "~↑--→"
sleep 0

printf "\033[1;33m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0

printf '\033[1;32m'

echo -n "{TOOL"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n "~|___»»"
sleep 0.1

echo "\033[0;37m WELCOME TO INTERACTIVE MENU !!"
sleep 0.1

echo "\033[0;91m |-↓"
sleep 1
''')
    print(f"{red3}   |__»» [*] 1. {green3}Custom Commands      {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 2. {green3}Your Custom Command  {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 3. {green3}Help Menu            {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 4. {green3}About Me             {rm}\033[0;31m)")
    print(f"{red3}   |__»» [*] 5. {green3}Exit                 {rm}\033[0;31m)")
    print(f"{red3} |-↓", end="")
    sleep(1)
    print("\033[0;37;40m")

    while True:
        os.system('''

printf '\033[1;34m'

echo -n " ↑--→"
sleep 0.1

printf "\033[033m"

echo -n "HITESH"
sleep 0.2

echo -n "×"
sleep 0.2

echo -n "GURU"
sleep 0.1

printf '\033[0;34m'

echo -n "--"
sleep 0.1

printf '\033[1;32m'

echo -n "{CH01C3"
sleep 0.1

echo -n " M3NU}\n"
sleep 0.1

printf '\033[0;34m'

echo -n " |___»»"
sleep 0.1
''')

        choice = input("\033[0;37m ENTER YOUR CHOICE: ")

        if choice == '1':
            banner()
            custom_cmd()
            break
        elif choice == '2':
            banner()
            user_custom_cmd()
            break
        elif choice== '3':
            help()
            break
        elif choice == '4':
            aboutMe()
            break
        elif choice == '5':
            print("\n\033[1;91m>>×××××××××××××××--Good Bye, we meet again fast Baby.--×××××××××××××××××<<\n")
            break
        else:
            print("\n\033[1;91m>>×××××××××××××××--Invalid choice. Please try again.--×××××××××××××××××<<\n")


#################################################


if __name__ == "__main__":
    main()
