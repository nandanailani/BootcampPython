command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car Stopped")
    elif command == "help":
        print('''
        start - to start the car
        start - to stop the car'''
              )