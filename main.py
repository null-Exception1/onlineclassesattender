from fetch.assignments import *
from fetch.announcements import *
from fetch.material import *
from record.recorder import *
from meet.get_meets import *
import webbrowser
import time
import os
import json
f = open('userdata.json',)
userdata = json.load(f)
f.close()
if userdata['email'] == "*":
    print("You haven't put your details in userdata.json!")
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    f = open('userdata.json','w')
    f.write("{\"email\": \"" + email + ",\"password\" : \""+password+"\"}")
    f.close()

    f = open('userdata.json',)
    userdata = json.load(f)
    f.close()
print("Found email in userdata.json : ",userdata['email'])
print("Found password in userdata.json : ",len(userdata['password'])*"*")
try:
    import keyboard

except ModuleNotFoundError:
    print("Keyboard module was not found on this computer. Starting a pip install")
    retina = os.system("pip install keyboard")
    if retina != 0:
        print("Keyboard module could not be installed, we recommend you install it manually. Till it is found, any feature that requires keyboard module will not be used")
    else:
        print("Successful install!")
"""

It is recommended to keep this program opened during the entire day session of classes, if you want to use the auto-class meet opening feature

"""
def menu():
    print("""
------------Menu---------------
1 - Open all the assignments
2 - Open all the announcements
3 - Open class links as you recieve them (listener, exit by holding down E)
4 - Open all the material 
5 - Record Session (exit by holding down E)
6 - Exit
-------------------------------
    """)
links = []
while True :   
    menu()
    ans = int(input("Enter number : "))
    if ans == 1:
        print("Fetching all assignments...")
        a = get_assignments(userdata)
        for url in a[0]:
            print("Found an assignment! : " + url+",","Subject :",a[1][a[0].index(url)],"\n")
            
            webbrowser.open("https://classroom.google.com/u/2/"+url[29:],new=2)
    if ans == 2:
        print("Fetching all announcements...")
        a = get_announcements(userdata)
        for url in a[0]:
            print("Found an announcement! : " + url + ",","Subject :",a[1][a[0].index(url)],"\n")
            
            webbrowser.open("https://classroom.google.com/u/2/"+url[29:],new=2)
    if ans == 3:
        print("Hold down E to exit listening for class meet links")
        while True:
            print("Fetching ...")
            urls = get_meet(userdata)
            if len(urls) == 0:
                print("No meet link found, will check again in 10 seconds")
            if len(urls) > 0:
                g = False
                for i in urls:
                    if not i in links:
                        g = True
                if g == False:
                    print("No meet link found, will check again in 10 seconds")
                for i in urls:
                    if i in links:
                        break
                    else:
                        links.append(i)
                    print("Recieved a meet link : " + i,"\n")
                    webbrowser.open(urls[0],new=2)
            for i in range(5):
                time.sleep(2)
                if keyboard.is_pressed('e'):
                    break
    if ans == 4:
        print("Fetching all material...")
        a = get_material(userdata)
        for url in a[0]:
            print("Found material! : " + url + ",","Subject :",a[1],"\n")
            
            webbrowser.open("https://classroom.google.com/u/2/"+url[29:],new=2)
    if ans == 5:
        print("We expect you may be ONE of these devices to hear audio from the class")
        for i in get_devices():
            print(i[0]+",","ID :",i[1])
        id_ = input("Pick the recording device which is currently being used as a speaker. Click on the speaker icon on your computer to know what speaker you are currently using : ")

        select_device(int(id_))

        print("Recording")
        record()
        print("Stopped")
    os.system('cls')
