from qhue import Bridge, create_new_username
username = create_new_username("10.0.0.96")
b = Bridge("10.0.0.96", username)

light = raw_input("Which lights are you looking to turn on? Valid inputs are Bedroom, Office, or All.")

command = raw_input("Are you turning your lights on or off? ")


if light.lower() == "office":
    if command.lower() == "on":
        bright = raw_input("How bright would you like the lights to be, where 1 is the dimmest and 254 is the brightest? ")
        if int(bright) >= 1 and int(bright) <= 254:
            b.lights[1].state(on = True, bri = int(bright))
    elif command.lower() == "off":
        b.lights[1].state(on = False)
    else:
        print "You must enter a number between 1 and 254."

elif light.lower() == "bedroom":
    if command.lower() == "on":
        bright = raw_input("How bright would you like the lights to be, where 1 is the dimmest and 254 is the brightest? ")
        if int(bright) >= 1 and int(bright) <= 254:
            b.lights[2].state(on = True, bri = int(bright))
    elif command.lower() == "off":
        b.lights[2].state(on = False)
    else:
        print "You must enter a number between 1 and 254."

elif light.lower() == "all":
    if command.lower() == "on":
        bright = raw_input("How bright would you like the office light to be, where 1 is the dimmest and 254 is the brightest? ")
        if int(bright) >= 1 and int(bright) <= 254:
            b.lights[1].state(on = True, bri = int(bright))
        bright = raw_input("How bright would you like the office light to be, where 1 is the dimmest and 254 is the brightest? ")
        if int(bright) >= 1 and int(bright) <= 254:
            b.lights[2].state(on = True, bri = int(bright))
    elif command.lower() == "off":
        b.lights[1,2].state(on = False)
    else:
        print "You must enter a number between 1 and 254."



else:
    print "You must select a valid input."
