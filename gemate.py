from __future__ import unicode_literals
import os, sys, time

#Clear the console or the command prompt for both platforms
def clear():
    if sys.platform == 'linux':
        os.system("clear")
    elif sys.platform == 'win32':
        os.system("cls")
    else:
        print("\033[1;31mThis program is only compatible with windows and linux for now.")
        exit()
        
#Install packages in linux platform 
def linux():
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           %%%%%%%%%%%%%% L\033[3;32mINU\033[3;31mX\033[3;94m %%%%%%%%%%%%%")
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2.5)
    print("\033[3;31m")
    s = os.system
    s("sudo apt-get update")
    s("sudo apt install python3-pip")
    s("pip3 install youtube-dl")
    s("pip3 install pyperclip")
    s("clear")
    #Restart the program, to fully initiate installations
    os.execv(sys.executable, ['python'] + sys.argv)
    function()

#Install packages in windows platform
def windows():
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           %%%%%%%%%%%% W\033[3;32mINDOW\033[3;31mS\033[3;94m %%%%%%%%%%%")
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2.5)
    s = os.system
    s("pip install youtube-dl")
    s("pip install pyperclip")
    s("cls")
    os.execv(sys.executable, ['python'] + sys.argv)
    function()
    
#The main download and additions
def function():
    clear()
    print("\033[;1;94m(For audio conversion: \033[;2;95mThis program requires ffmpeg, install it for Linux (and other command-line OSes) by running 'apt-get install ffmpeg'. For windows, You can download the package online and convert it manually......)\n")
    print("\033[1;33m*** Copy/Paste to you browser to view a list of youtube-dl supported sites ***\n")
    print(" https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md \n")
    print("Choose 1 or 2")
    print("1. Take the url from the clipboard automatically")
    print("2. Type/paste the url manually\n")
    clip = input("GEMATE==> ")
    if clip == '':
        print("\033[1;31mNo choice, exiting.....")
        time.sleep(1.5)
        clear()
        exit()
    #Extract clipboard contents, (thanks to Al-Swiegart)    
    elif clip == '1':
        print("\n                   [*]Extracting clipboard content........")
        try:
            url = pyperclip.paste()
            if url == '':
                print("Your clipboard doesn't seem to have any contents. ", end = '')
                print("exiting.....")
                time.sleep(1.5)
                clear()
                exit()
            else:
                print("                                 Done")
        #Usually happens in termux (Android based consoles)        
        except pyperclip.PyperclipException:
            print("Your platform doesn't seem to possess any copy/paste mechanism, Do try choosing option 2")
            time.sleep(3.5)
            function()
    #Seeing that you're hardworking, enter the url manually        
    elif clip == '2':
        print("\033[3;32m                         [*]Manual input....")
        time.sleep(0.5)
        url = input("Enter the video url ==> ")
        if url == '':
            print("\nYou didn't provide any url. ",end='')
            print("exiting......")
            time.sleep(2)
            clear()
            exit()
    #Trouble maker        
    else:
        print("\033[1;31mError, please follow the instructions")
        time.sleep(1.5)
        clear()
        exit()
        
    #Audio or video?, make your choice
    print("\nChoose your file Format, 1 or 2")
    print("\n                 [1.] mp3 ('mp3 is audio')")
    print("                 [2.] mp4 ('mp4 is video')")
    form = input("GEMATE==>  ")
    if form == '':
        print("No Choice, Exiting........")
        time.sleep(1.5)
        clear()
        exit()
    elif form == '1':
        print("\033[3;36mPro tip: type (./) if you want to save the audio in the same directory you are right now. Without the brackets of course.",end='')
        print(" Your input should look like this '/home/username/folder/' for linux and 'C:/Users/username/folder/'\n")
        dest = input("\033[3;35mEnter the destination you want to save the audio ==> ")
        print("[*]Retrieving audio format........")
        time.sleep(0.5)
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl':dest+'%(title)s.%(ext)s',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',}],
    }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except youtube_dl.utils.DownloadError:
            pass
        except KeyboardInterrupt:
            print("\nExiting Cleanly....")
            time.sleep(2.5)
            clear()
            exit()
            
    elif form == '2':
        print("Pro tip: type (./) if you want to save the video in the same directory you are right now. Without the brackets of course.",end='')
        print(" Your input should look like this '/home/username/folder/' for linux and 'C:/Users/username/folder/' for windows \n")
        dest = input("Enter the destination you want to save the video ==> ")
        print("\033[3;36m[*]Extracting Video Format.........")
        time.sleep(0.5)
        ydl_opts = {'ext':'mp4',
                    'outtmpl':dest+'%(title)s.%(ext)s',}

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except youtube_dl.utils.DownloadError:
            pass
        except KeyboardInterrupt:
            print("\nExiting Cleanly...")
            time.sleep(2.5)
            clear()
            exit()
        
    else:
        print("Please Follow the instructions and try again later")
        exit()

    print("\033[3;32mDo you want to perform another Download? \nY or N")
    down = input("GEMATE==> ")
    if down == 'y' or down == 'Y':
        print("[*]Continuing........")
        time.sleep(0.5)
        function()
    elif down == 'n' or down == 'N':    
        print("THANKS FOR USING GEMATE.........")
        time.sleep(1.5)
        clear()
        exit()
    else:
        print("\033[1;31mError, Please follow the instructions.")
        time.sleep(1.5)
        clear()
        exit()
    
     
        
        
try:
    clear()
    import youtube_dl
    import pyperclip
except ModuleNotFoundError:
    print("\033[3;91mYou dont have all the required modules.\n")
    print("\033[3;94mWould you like the program to install them automatically?")
    print("                           (Y or N)")
    install = input("GEMATE==> ")
    if install == 'Y' or install == 'y':
        print("[*]Installing Please wait.......")
        time.sleep(1.5)
        print("Checking your platform.......\n")
        if sys.platform == 'linux':
            linux()
        elif sys.platform == 'win32':
            windows()
    elif install == 'N' or install == 'n':
        print("Exiting......")
        time.sleep(1.5)
        clear()
        exit()
    else:
        print("\033[1;31mTrouble maker")
        time.sleep(1.5)
        clear()
        exit()

function()        
