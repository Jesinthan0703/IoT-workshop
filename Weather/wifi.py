import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

option= str (input(("You want to connect(1) or disconnect(2) or check connection(3) : ")))

if(option=="1"):
    print("\n")
    name = str(input("Enter the name of the wifi: "))
    passw = str(input("Enter the password: "))

    if (not sta_if.isconnected()):
        sta_if.connect(name, passw)
        print("Connected to WIFI: ", sta_if.config('essid'))
        
        
if(option=="2"):
    print("\n")
    if (sta_if.isconnected()):
        sta_if.disconnect()
        
    if (not sta_if.isconnected()):
        print("Disconnected Successfully!")
        

if(option=="3"):
    print("\n")
    if(sta_if.isconnected()):
        print("Wifi : ", sta_if.config('essid'))
        print("Board's IP : ", sta_if.ifconfig()[0])
        print("Status : ", sta_if.isconnected())
    if(not sta_if.isconnected()):
        print("Wifi: ", sta_if.config('essid'))
        print("Status : ", sta_if.isconnected())
        