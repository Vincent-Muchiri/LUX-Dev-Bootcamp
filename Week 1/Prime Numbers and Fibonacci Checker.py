# -------------------------------------------PACKAGES AND MODULES----------------------------------------------------
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

# --------------------------------------------CONSTANTS AND VARIABLES-----------------------------------------------
fib_list = [0, 1]


# ----------------------------------------------FUNCTIONS----------------------------------------------------------
# TODO Create a function to check whether the number is in the Fibonacci sequence and return 'response'
def fib_checker(digit):
    response = ""

    # TODO Check whether 0 is in the sequence
    if digit == 0:
        response = f"{digit} is in the Fibonacci sequence"
    else:
        continue_checking = True

        while continue_checking:
            # TODO Create a fibonacci number and add it into the list
            fib = fib_list[-1] + fib_list[-2]
            fib_list.append(fib)

            # TODO Check whether the digit is in the list of Fibonacci numbers
            if fib <= digit:
                if fib == digit:
                    response = f"{digit} is in the Fibonacci sequence."
                    continue_checking = False
            else:
                response = f"{digit} is not in the fibonacci sequence."
                continue_checking = False
    return response

# A number is prime of its is divisible only by 1 and itself
# A number is not prime if it is divisible by any other number other than 1 and itself

# TODO Create a function to check whether the number enter is a prime number
def prime_checker(digit, response):
    if digit == 0:
        response += " but is not a prime number."
        messagebox.showinfo(message=response)
    elif digit == 1:
        response += "\nIt is also not a prime number."
        messagebox.showinfo(message=response)
    elif digit == 2:
        response += "\nIt's also a prime number."
        messagebox.showinfo(message=response)
    else:
        for num in range(2, digit):
            if digit % num == 0:
                response += "\nIt is not a prime number."
                messagebox.showinfo(message=response)
                break
            if num == digit - 1:
                response += "\nIt is a prime number."
                messagebox.showinfo(message=response)


def check():
    try:
        digit = int(num_entry.get())
    except ValueError:
        num_entry.state(["invalid"])
        messagebox.showerror(title="Value missing", message="Please enter an integer.")
    else:
        # TODO Check whether the number is in the Fibonacci sequence
        response = fib_checker(digit)

        # TODO Check whether the number entered is a prime number
        prime_checker(digit, response)

# TODO Delete the entry and place the cursor in the entry
    num_entry.delete(0, END)
    num_entry.focus()


# -----------------------------------------------------GUI------------------------------------------------------------
# TODO Create window
window = Tk()
window.title("Prime Number and Fibonacci Checker")
window.config(padx=20, pady=20)
window.minsize(width=300, height=100)


# TODO Add styling
style = ttk.Style(window)
window.tk.call('source', './_packages/Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground="white")

# TODO Create prime number label
num_label = Label(text="Enter number:")
num_label.config(padx=20, pady=20)
num_label.grid(row=0, column=0)

# TODO Create prime number entry
num_entry = ttk.Entry()
num_entry.focus()
# num_entry.insert(0, 0)
num_entry.grid(row=0, column=1)

# TODO Create check button
check_btn = ttk.Button(text="Check", style="Accentbutton", command=check)
check_btn.config(width=37)
check_btn.grid(row=1, column=0, columnspan=2)

window.mainloop()
