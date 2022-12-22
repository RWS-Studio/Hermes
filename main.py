from time import sleep
import sys
import os
from random import randint
from pyfiglet import Figlet

def main():
    toolbar_width = 100
    time = 0
    nb = 0
    listpath = "./path/yourlist.txt" # change this with your email list

    with open("./temp/active.txt", 'w') as active:
        active.write("False")
    with open("./logs/reportmailrestart.txt", 'w') as restartmaillog:
        restartmaillog.write("False")
    with open("./temp/overflow.txt", 'w') as overflow:
        overflow.write("False")
    with open(listpath, 'r') as f:
        for line in f:
            if line == '':
                print("Empty list. . .")
                sys.exit()
            nb += 1
    
    lastindex = 0
    with open("./temp/log.txt", 'r') as log:
        for i in log:
            pass
            lastline = i                            
            lastindex = int(lastline[lastline.find(":")+1::])+1

    emailsleft = nb - lastindex
    minutesleft = round((15*emailsleft)/(60))
    if minutesleft > 60:
        minutesleft = (minutesleft//60, minutesleft - ((minutesleft//60)*60))
    with open("./temp/liste.txt", 'w') as logliste:
        logliste.write(listpath)

    with open(listpath, 'r') as f:   
        custom_fig = Figlet(font='larry3d')
        print(custom_fig.renderText('Hermes'))       
        print(f"\n{emailsleft} emails left ~= {minutesleft[0]} hours {minutesleft[1]} minutes.")
        print("\nProgress bar :")
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
        for email in f:
            with open("./temp/active.txt", 'r') as active:
                send = active.readline()
                while send == "True":
                    send = active.readline()
            if send == "False":
                with open("./logs/reportmailrestart.txt", 'r') as restartmaillog:
                    bug = restartmaillog.readline()
                if bug == "False":
                    with open("./temp/overflow.txt", 'r') as overflow:
                        overflowline = overflow.readline()
                    if overflowline == 'False':
                        if time == emailsleft/toolbar_width:
                            sys.stdout.write('■')
                            sys.stdout.flush()
                            time = 0
                        time += (emailsleft/toolbar_width)/(emailsleft/toolbar_width)
                        os.system("start cmd /c python ./sender.py")
                        sleep(randint(10, 20))
                    else:
                        print("\nDaily limit")
                        sys.exit()
                else:
                    sleep(300)
                    with open("./logs/reportmailrestart.txt", 'w') as restartmaillog:
                        restartmaillog.write("False")

        print("Finish !")

main()
