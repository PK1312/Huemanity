from qhue import Bridge, create_new_username

username = create_new_username("<Your bridge IP")
b = Bridge("<Your bridge IP", "username")

def turnon(lightname):
    bright = raw_input("How bright would you like the light(s) to be, where 1 is the dimmest and 254 is the brightest? ")
    if int(bright) >= 1 and int(bright) <= 254:
        b.lights[lightlist[lightname]].state(on = True, bri = int(bright))
    else:
        print "You must enter a number between 1 and 254. "

def turnoff(lightname):
        b.lights[lightlist[lightname]].state(on = False)

lightlist = {
"office" : 1,
"basement" : 2,
"bedroom" : 3,
}

commands = {
"on" : turnon,
"off" : turnoff,
}

while True:

    allLights = lightlist.keys()
    allLights.append("all")
    light = raw_input("What lights are you looking to turn on or off? Valid inputs are "+", ".join(allLights)+". You can also type 'quit' to end the application. ")


    if light in allLights:
        command = raw_input("Are you looking to turn your lights on or off? ").lower()
        if command in commands:
            commandFunction = commands[command]
            if light == "all":
                for bulb in lightlist:
                    commandFunction(bulb)
            else:
                commandFunction(light)
        else:
            print "You must enter either on, off, or quit. "

    elif light == "quit":
        break
    else:
        print "You must enter a valid command. "
