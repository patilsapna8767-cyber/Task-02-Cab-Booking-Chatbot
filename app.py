import tkinter as tk
from tkinter import messagebox
import random

def calculate():
    cab = var_cab.get()
    route = var_route.get()
    
    rates = {"Auto": 15, "Sedan": 18, "SUV": 22}
    distances = {"Baner to Hinjewadi": 5, "Kothrud to Hadapsar": 8, "Pune Station to Airport": 10}
    
    fare = rates[cab] * distances[route]
    otp = random.randint(1000, 9999)
    
    messagebox.showinfo("Booking Confirmed", f"Cab: {cab}\nRoute: {route}\nFare: Rs {fare}\nOTP: {otp}\n\nOTP share zalyavar cancel nahi honar!")

root = tk.Tk()
root.title("Cab Booking App")
root.geometry("300x300")

var_cab = tk.StringVar(value="Auto")
var_route = tk.StringVar(value="Baner to Hinjewadi")

tk.Label(root, text="Sapna's Cab Booking", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Cab Type").pack()
tk.OptionMenu(root, var_cab, "Auto", "Sedan", "SUV").pack()
tk.Label(root, text="Route").pack(pady=5)
tk.OptionMenu(root, var_route, "Baner to Hinjewadi", "Kothrud to Hadapsar", "Pune Station to Airport").pack()
tk.Button(root, text="Book Now", command=calculate, bg="green", fg="white", width=15).pack(pady=20)

root.mainloop()
