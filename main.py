import classes.deliveryRobot
import classes.guardRobot


Dora = classes.deliveryRobot.DeliveryRobot("Dora", [0,0])
Gideon = classes.guardRobot.GuardRobot("Gideon")

while True:
    choose = input("\nEnter a command: \n 1- SAY ready \n 2- MOVE 3 2 \n 3- WHERE \n 4- SAY done \n 5- EXIT\n")
    match choose:
        case "1":
            Dora.speak("ready")
            Gideon.speak("ready")
        case "2":
            Dora.move(3,2)
            print(f"{Gideon.name} unsupported command MOVE")
        case "3":
            print(f"{Dora.name} is in place {Dora.localisation}")
            print(f"{Gideon.name} unsupported command WHERE")
        case "4":
            Dora.speak("done")
            Gideon.speak("done")
        case "5":
            break

