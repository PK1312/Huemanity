from qhue import Bridge, create_new_username
username = create_new_username("10.0.0.96")
b = Bridge("10.0.0.96", username)

while True:
    command = raw_input("Welcome to Huemanity! Please select a number: 1. Turn lights on and off. 2. Set schedule. 3. Check schedules. Enter quit to quit. ")

    if command == "1" or command == "1.":
        light = raw_input("Which lights are you looking to turn on or off? Valid inputs are Bedroom, Office, Basement, or All. ")

        if light.lower() == "office":
            onoff = raw_input("Are you turning your lights on or off? ")
            if onoff.lower() == "on":
                bright = raw_input("How bright would you like the lights to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[1].state(on = True, bri = int(bright))
                else:
                    print "You must enter a number between 1 and 254."
            elif onoff.lower() == "off":
                b.lights[1].state(on = False)
            else:
                print "You must enter on or off."

        elif light.lower() == "bedroom":
            onoff = raw_input("Are you turning your lights on or off? ")
            if onoff.lower() == "on":
                bright = raw_input("How bright would you like the lights to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[3].state(on = True, bri = int(bright))
                else:
                    print "You must enter a number between 1 and 254."
            elif onoff.lower() == "off":
                b.lights[3].state(on = False)
            else:
                print "You must enter on or off."

        elif light.lower() == "Basement":
            onoff = raw_input("Are you turning your lights on or off? ")
            if onoff.lower() == "on":
                bright == raw_input("How bright would you like the light to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[2].state(on = True, bri = int(bright))
                else:
                    print "You must enter a number between 1 and 254."
            elif onoff.lower() == "off":
                b.lights[2].state(on = False)
            else:
                print "You must enter on or off."

        elif light.lower() == "all":
            onoff = raw_input("Are you turning your lights on or off? ")
            if onoff.lower() == "on":
                bright = raw_input("How bright would you like the office light to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[1].state(on = True, bri = int(bright))
                bright = raw_input("How bright would you like the bedroom light to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[3].state(on = True, bri = int(bright))
                bright = raw_input("How bright would you like the basement light to be, where 1 is the dimmest and 254 is the brightest? ")
                if int(bright) >= 1 and int(bright) <= 254:
                    b.lights[2].state(on = True, bri = int(bright))
            elif onoff.lower() == "off":
                b.lights[1].state(on = False)
                b.lights[2].state(on = False)
                b.lights[3].state(on = False)
            else:
                print "You must enter a number between 1 and 254."
        else:
            print "You must enter a valid light."
    elif command == "2" or command == "2.":
            print "You must select a valid input."
    elif command == "3" or command == "3.":
        print "You must select a valid input."
    elif command.lower() == "quit":
        break
    else:
        print "You must select a valid input."
