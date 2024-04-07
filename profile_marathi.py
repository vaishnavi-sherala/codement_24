import tkinter as tk
from tkinter import messagebox, ttk
import speech_recognition as sr
from gtts import gTTS
import os
from arogya import pre
from chatbot_marathi import fun
from video2 import vedo
#from arogya import predict_disease

def vido():
    profile_window.destroy()

    vedo()
profile_window = None


  # Define profile_window globally


def open_arogya():
    global profile_window  # Referencing the global profile_window
    profile_window.destroy()  # Close the profile window
    pre()  # Open the arogya window


def save_profile(name_var, age_var, phone_var):
    global profile_window  # Referencing the global profile_window
    profile_window = tk.Tk()
    profile_window.title("प्रोफाइल")

    profile_window.geometry("600x400+{}+{}".format(int(profile_window.winfo_screenwidth() / 2 - 300), int(profile_window.winfo_screenheight() / 2 - 200)))

    # Set background color and font
    profile_window.configure(bg="#0000FF")
    label_font = ("Arial", 12, "bold")

    # Create sections with different background colors
    personal_info_frame = tk.Frame(profile_window, bg="#0000FF", padx=20, pady=10)

    personal_info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Personal Information Section
    tk.Label(personal_info_frame, text="प्रोफाइल", font=("Arial", 18, "bold"), bg="#e6e6e6").pack(pady=5)

    tk.Label(personal_info_frame, text=f"नाव: {name_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)
    tk.Label(personal_info_frame, text=f"वय: {age_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)
    tk.Label(personal_info_frame, text=f"फोन नंबर: {phone_var.get()}", font=label_font, bg="#e6e6e6").pack(anchor=tk.W)

    tk.Button(personal_info_frame, text="आरोग्य केंद्र", command=open_arogya, font=label_font, bg="#80ff80", width=14, height=10).pack(side=tk.RIGHT, padx=5)
    tk.Button(personal_info_frame, text="चॅटबॉट",command=fun, font=label_font, bg="#ff8080", width=14, height=10).pack(side=tk.RIGHT, padx=5)
    tk.Button(personal_info_frame, text="व्हिडिओ चॅट",command=vido, font=label_font, bg="#8080ff", width=14, height=10).pack(side=tk.RIGHT, padx=5)


