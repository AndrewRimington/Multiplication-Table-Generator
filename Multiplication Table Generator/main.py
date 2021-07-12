from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Multiplication Table Generator")
window.iconbitmap(r"cancel (5).ico")
window.state("zoomed")

original_text = """
Multiplication Table:
 1 x 0 = 0
 1 x 1 = 1
 1 x 2 = 2
 1 x 3 = 3
 1 x 4 = 4
 1 x 5 = 5
 1 x 6 = 6
 1 x 7 = 7
 1 x 8 = 8
 1 x 9 = 9
 1 x 10 = 10"""

def clear():
    expression = ""
    results_screen.config(text=expression)

def generate(text_box_input):
    number = int(text_box_input.get("1.0",END))
    x ="Multiplication Table: \n\n"
    result = []
    for count in range (11): 
        product = count * number
        result.append("{} x {} = {}".format(number,count,product))
    final_result= x + "\n".join(result)
    results_screen.config(text=final_result)

frame = Frame(window)
frame.place(anchor=N)
frame.pack(pady=15)

Label1 = tk.Label(frame, text="Generate the multiplication table for ", font="Times, 18")
Label1.pack(side=LEFT)
text_box = tk.Text(frame,height =1,width=2, font="Times, 18")
text_box.pack(side=LEFT)
text_box.insert(tk.INSERT, "1")
Label2 = tk.Label(frame, text=" up to x 10:", font="Times, 18")
Label2.pack(side=LEFT)
results_screen = tk.Label(window, text=str(original_text), font="Times, 18", relief="solid", bg="peach puff",justify=LEFT, width=80, height=15)
results_screen.pack(pady=20)

button_frame = Frame(window)
button_frame.pack()

clear_button = Button(button_frame, text="Clear", font="Times, 15", bg="navajo white", command= clear, width=10)
clear_button.grid(row=0, column=0, pady=25)

generate_button = Button(button_frame, text="Generate", font="Times, 15", bg="navajo white", command=lambda: generate(text_box), width=10)
generate_button.grid(row=0, column=1, pady=25, padx=30)


icon_credit = Label(window, text="Credits to Freepik for the icon.", font="Times, 10")
icon_credit.place(anchor=S)
icon_credit.pack()











print("The icon was made by Freepik.")
window.mainloop()