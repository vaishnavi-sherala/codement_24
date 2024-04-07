import tkinter as tk
from tkinter import messagebox, ttk
import speech_recognition as sr
from gtts import gTTS
import os
from arogya_english import fun
from video1 import vedo
from chatbot import fun1
#from arogya import predict_disease

def vido():
    profile_window1.destroy()

    vedo()

def fun3():
    profile_window1.destroy()
    fun1()


profile_window1 = None

def open_arogya():
    global profile_window1  # Referencing the global profile_window
    profile_window1.destroy()  # Close the profile window
    fun()

def save_profile(name_var, age_var, phone_var):
    global profile_window1  # Declare global profile_window1 to modify it within the function
    profile_window1 = tk.Tk()
    profile_window1.title("Profile")

    profile_window1.geometry("600x400+{}+{}".format(int(profile_window1.winfo_screenwidth() / 2 - 300), int(profile_window1.winfo_screenheight() / 2 - 200)))

    # Set background color and font
    profile_window1.configure(bg="#0000FF")
    label_font = ("Arial", 12, "bold")

    # Create sections with different background colors
    personal_info_frame = tk.Frame(profile_window1, bg="#0000FF", padx=20, pady=10)
     
    personal_info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Personal Information Section
    tk.Label(personal_info_frame, text="Profile", font=("Arial", 18, "bold"), bg="#e6e6e6").pack(pady=5)

    tk.Label(personal_info_frame, text=f"Name: {name_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)
    tk.Label(personal_info_frame, text=f"Age: {age_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)
    tk.Label(personal_info_frame, text=f"Phone No: {phone_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)

    tk.Button(personal_info_frame, text="Arogya kendra",command=open_arogya ,font=label_font, bg="#80ff80", width=14, height=10).pack(side=tk.RIGHT, padx=5)
    tk.Button(personal_info_frame, text="Chatbot", font=label_font,command=fun3, bg="#ff8080", width=14, height=10).pack(side=tk.RIGHT, padx=5)
    tk.Button(personal_info_frame, text="Video Chat",command=vido, font=label_font, bg="#8080ff", width=14, height=10).pack(side=tk.RIGHT, padx=5)

    #profile_window1.mainloop()

# Example usage:
# root = tk.Tk()
# name_var = tk.StringVar()
# age_var = tk.StringVar()
# phone_var = tk.StringVar()
# save_profile(name_var, age_var, phone_var)
