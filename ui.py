import customtkinter
from PIL import Image, ImageTk
import os
import sys
import main
from CTkToolTip import *

#Setup
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Generator")
icon = ImageTk.PhotoImage(Image.open(resource_path("logo.png")))
app.iconbitmap()
app.iconphoto(False, icon)

#App Grid Configuration
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(6, weight=1)

#Functions
def generatePassword():
    length = int(lengthSlider.get())
    useUppercase = upperCase.get()
    useNumbers = numbers.get()
    useSymbols = symbols.get()
    main.generateRandomPassword(length, useUppercase, useNumbers, useSymbols, output)

def updateLabel(val):
    lengthSliderLabel.configure(text=f"Password Length: {int(val)}")
    
def sliderCommand(val):
    generatePassword()
    updateLabel(lengthSlider.get())
    
def select_all(event):
    event.widget.after_idle(lambda: event.widget.tag_add("sel", "1.0", "end"))
    event.widget.after_idle(lambda: app.clipboard_clear())
    event.widget.after_idle(lambda: app.clipboard_append(event.widget.get("1.0", "end")))

#Widgets
title = customtkinter.CTkLabel(app,
                               text="Aegis Core",
                               font=("Product Sans", 50),
                               )
title.grid(row=0, column=0, columnspan=3, pady=10)
titleToolTip = CTkToolTip(title,
                          font=("Product Sans", 10),
                          message="Made by Matthew Raymundo")

output = customtkinter.CTkTextbox(app,
                                width=500,
                                height=70,
                                font=("Product Sans", 20),
                                )
output.grid(row=1, column=0, columnspan=3, pady=10)
output.bind('<FocusIn>', select_all)
output.bind('<Button-1>', select_all)

#Generate Button
generate = customtkinter.CTkButton(app,
                                    width=150,
                                    height=40,
                                    corner_radius=20,
                                    text="Generate",
                                    font=("Product Sans", 15, "bold"),
                                    command=generatePassword,
                                    )
generate.grid(row=2, column=0, columnspan=3, pady=(10, 0))

#Frame
frame = customtkinter.CTkFrame(app)
frame.grid(sticky="nsew", row=3, column=0, columnspan=3, rowspan=3, padx=20, pady=20)

#Frame Grid Configuration
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)

#Length Slider
lengthSlider = customtkinter.CTkSlider(frame,
                                       width=400,
                                       from_=5,
                                       to=64,
                                       number_of_steps=59,
                                       command=sliderCommand,
                                       )
lengthSlider.grid(row=1, column=0, columnspan=3, pady=(0, 30))
lengthSlider.set(8)

lengthSliderLabel = customtkinter.CTkLabel(frame,
                                            text=("Password Length: 8"),
                                            font=("Product Sans", 15, "bold"),
                                            )
lengthSliderLabel.grid(row=0, column=0, columnspan=3, pady=(20, 10))

#Uppercase
upperCaseLabel = customtkinter.CTkLabel(frame,
                                        width=240,
                                        text="Uppercase Letters",
                                        font=("Product Sans", 15, "bold"),
                                        wraplength=200,
                                        )
upperCaseLabel.grid(sticky="nsew", row=2, column=0, pady=(0, 30))

upperCase = customtkinter.CTkSwitch(frame,
                                    text="",
                                    width=20,
                                    height=20,
                                    command=generatePassword
                                    )
upperCase.grid(row=3, column=0, padx=(10, 0), pady=(0, 40))

#Numbers
numbersLabel = customtkinter.CTkLabel(frame,
                                      width=240,
                                      text="Numbers",
                                      font=("Product Sans", 15, "bold"),
                                      wraplength=200,
                                      )
numbersLabel.grid(sticky="nsew", row=2, column=1, pady=(0, 30))

numbers = customtkinter.CTkSwitch(frame,
                                  text="",
                                  width=20,
                                  height=20,
                                  command=generatePassword
                                  )
numbers.grid(row=3, column=1, padx=(10, 0), pady=(0, 40))

#Symbols
symbolsLabel = customtkinter.CTkLabel(frame,
                                      width=240,
                                      justify="center",
                                      text="Symbols",
                                      font=("Product Sans", 15, "bold"),
                                      wraplength=200,
                                      )
symbolsLabel.grid(sticky="nsew", row=2, column=2, pady=(0, 30))

symbols = customtkinter.CTkSwitch(frame,
                                  text="",
                                  width=20,
                                  height=20,
                                  command=generatePassword
                                  )
symbols.grid(row=3, column=2, padx=(10, 0), pady=(0, 40))
    
#Loop
app.mainloop()