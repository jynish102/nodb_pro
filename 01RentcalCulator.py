## Input Feilds
# total hostel/flat rent
# total food cost
# Electricity Units spend
# Charge per unit
#how much person living in room/flat

from tkinter import *
from tkinter import messagebox

# Create window
root = Tk()
root.title("Room Expense Split Calculator")
root.geometry("400x500")
root.config(bg="lightblue")


# Function to calculate bill
def calculate_bill():
    try:
        rent = float(rent_entry.get())
        food = float(food_entry.get())
        electricity_units = float(units_entry.get())
        charge_per_unit = float(charge_entry.get())
        persons = int(persons_entry.get())

        electricity_bill = electricity_units * charge_per_unit
        total_expense = rent + food + electricity_bill
        per_person = total_expense / persons

        result_label.config(
            text=f"""
Electricity Bill : ₹{electricity_bill:.2f}

Total Expense : ₹{total_expense:.2f}

Each Person Pays : ₹{per_person:.2f}
""",
            fg="darkgreen"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")


# Heading
heading = Label(
    root,
    text="Expense Split Calculator",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=10)


# Rent
Label(root, text="Room Rent (₹)", bg="lightblue", font=("Arial", 12)).pack()
rent_entry = Entry(root, width=30)
rent_entry.pack(pady=5)

# Food
Label(root, text="Food Cost (₹)", bg="lightblue", font=("Arial", 12)).pack()
food_entry = Entry(root, width=30)
food_entry.pack(pady=5)

# Electricity Units
Label(root, text="Electricity Units", bg="lightblue", font=("Arial", 12)).pack()
units_entry = Entry(root, width=30)
units_entry.pack(pady=5)

# Charge Per Unit
Label(root, text="Charge Per Unit (₹)", bg="lightblue", font=("Arial", 12)).pack()
charge_entry = Entry(root, width=30)
charge_entry.pack(pady=5)

# Persons
Label(root, text="Number of Persons", bg="lightblue", font=("Arial", 12)).pack()
persons_entry = Entry(root, width=30)
persons_entry.pack(pady=5)

# Calculate Button
calc_button = Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=calculate_bill
)
calc_button.pack(pady=20)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
result_label.pack(pady=10)

# Run app
root.mainloop()
