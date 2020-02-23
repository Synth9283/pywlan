import subprocess, platform, sys


if platform.system() == 'Windows':
    while True:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for n, i in enumerate(profiles):
            print(f"#{n+1}: {i}")

        option = input('Option: ')
        try:
            option = int(option)
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profiles[option-1], 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(profiles[option-1], results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(profiles[option-1], ""))
        except:
            print('Option must be an integer!')
        redo = input("Again? (Y/N): ")
        if redo == 'Y' or redo == 'y':
            pass
        else:
            sys.exit()
        option = input('Option: ')
else:
    print('Not supported yet')
