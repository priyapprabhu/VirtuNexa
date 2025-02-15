import time

def countdown_timer(duration):
    while duration > 0:
        mins, secs = divmod(duration,60)
        print(f"{mins:02d}:{secs:02d}",end="\r")
        time.sleep(1)
        duration -= 1
    print("Time's up!!")

def menu():
    print("Welcome to the timer application!!")
    while True:
        print("Main Menu:")
        print("1. Start countdown timer")
        print("2. Exit")
        ch = int(input("select an option:"))

        if ch == 1:
            duration = int(input("Enter countdown duration in seconds:"))
            countdown_timer(duration)
        elif ch ==2:
            print("exiting application!")
            break
        else:
            print("Invalid option. Please select a valid choice")

menu()