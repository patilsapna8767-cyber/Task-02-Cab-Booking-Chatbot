import random

while True:
    print("\n--- KIRAN ACADEMY CAB BOOKING ---")
    print("1. Book Ride")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print("\n1. Auto (12/km)")
        print("2. Sedan (18/km)")
        print("3. SUV (25/km)")
        cab = input("Choose cab: ")

        if cab == '1':
            cab_name = "Auto"
            rate = 12
        elif cab == '2':
            cab_name = "Sedan"
            rate = 18
        elif cab == '3':
            cab_name = "SUV"
            rate = 25
        else:
            print("Invalid cab!")
            continue

        print("\n1. Pune Station to Shivajinagar (5 km)")
        print("2. Swargate to Kothrud (8 km)")
        print("3. Hinjawadi to Wakad (10 km)")
        route = input("Choose route: ")

        if route == '1':
            source = "Pune Station"
            dest = "Shivajinagar"
            distance = 5
        elif route == '2':
            source = "Swargate"
            dest = "Kothrud"
            distance = 8
        elif route == '3':
            source = "Hinjawadi"
            dest = "Wakad"
            distance = 10
        else:
            print("Invalid route!")
            continue

        fare = distance * rate
        print(f"\nRoute: {source} to {dest}")
        print(f"Cab: {cab_name}, Distance: {distance} km, Fare: {fare}")

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")
        confirm = input("Enter: ")

        if confirm == '2':
            print("Ride Cancelled. OTP share nahi jhala.")
            continue
        elif confirm == '1':
            otp = random.randint(1000, 9999)
            print(f"\nBooking Confirmed! OTP: {otp}")
            print("OTP share zalyanantar ride cancel hou shakat nahi.")
            
    elif choice == '2':
        print("Thank you! Bye.")
        break
    else:
        print("Chukicha option!")