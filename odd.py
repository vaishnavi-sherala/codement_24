import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import speech_recognition as sr
import mysql.connector
from profile_english import save_profile

class DBOperation():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="vaishnavi@123",
                database="user_info"
            )
            if self.mydb.is_connected():
                print("Connection successful")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)

    def CreateTables(self):
        cursor = self.mydb.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS info (id INT AUTO_INCREMENT PRIMARY KEY, name_var VARCHAR(30), age_var INT(100), phone_var INT(10))")
        cursor.close()

    def InsertOneTimeData(self, name, age, phone):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO info (name_var, age_var, phone_var) VALUES (%s, %s, %s)"
        values = (name, age, phone)
        cursor.execute(sql, values)
        self.mydb.commit()
        cursor.close()

def window_english():
    
    def recognize_speech():
        # Initialize the recognizer
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio, language='en-US')
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio"
        except sr.RequestError as e:
            return "Error: {0}".format(e)

    def get_voice_input(label_var):
        voice_input = recognize_speech()
        if voice_input:
            label_var.set(voice_input)

    def save_information():
        # Retrieve values from tkinter StringVar variables
        name = name_var.get()
        age = age_var.get()
        phone = phone_var.get()

        # Insert data into the database
        db_operation = DBOperation()
        db_operation.CreateTables()
        db_operation.InsertOneTimeData(name, age, phone)

        # Show a message box confirming that the information is saved
        message = f"Information saved:\nName: {name}\nAge: {age}\nPhone: {phone}"
        messagebox.showinfo("Information Saved", message)
        def save_profile1():
            window1.destroy()
            save_profile(name_var,age_var,phone_var)
        save_profile1()

    # Create the main window
    window1 = tk.Tk()
    window1.title("Voice Input for Information")

    # Center the window on the screen
    window_width = 600
    window_height = 400
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window1.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window1.configure(bg='#0000FF')  # Set the background color to blue

    # Title label
    title_label = tk.Label(window1, text="Voice Input for Information", font=("Helvetica", 18), bg='#0000FF', fg='white')
    title_label.grid(row=0, column=0, columnspan=3, pady=20)

    # Create labels and entry fields for name, age, and phone number
    tk.Label(window1, text="Name:", font=("Helvetica", 12), bg='#0000FF', fg='white').grid(row=1, column=0, sticky='w', padx=10, pady=10)
    name_var = tk.StringVar()
    tk.Entry(window1, textvariable=name_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

    tk.Label(window1, text="Age:", font=("Helvetica", 12), bg='#0000FF', fg='white').grid(row=2, column=0, sticky='w', padx=10, pady=10)
    age_var = tk.StringVar()
    tk.Entry(window1, textvariable=age_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(window1, text="Phone Number:", font=("Helvetica", 12), bg='#0000FF', fg='white').grid(row=3, column=0, sticky='w', padx=10, pady=10)
    phone_var = tk.StringVar()
    tk.Entry(window1, textvariable=phone_var, font=("Helvetica", 12)).grid(row=3, column=1, padx=10, pady=10)

    # Create buttons to trigger voice input for each field
    tk.Button(window1, text="Speak Name", command=lambda: get_voice_input(name_var), font=("Helvetica", 10)).grid(row=1, column=2, padx=10, pady=10)
    tk.Button(window1, text="Speak Age", command=lambda: get_voice_input(age_var), font=("Helvetica", 10)).grid(row=2, column=2, padx=10, pady=10)
    tk.Button(window1, text="Speak Phone Number", command=lambda: get_voice_input(phone_var), font=("Helvetica", 10)).grid(row=3, column=2, padx=10, pady=10)
    # Create a button to save the information
    start_button_style = ttk.Style()
    start_button_style.configure('Start.TButton', foreground='blue', font=('Arial', 18))

    start_button = ttk.Button(window1, text="Save Information", command=save_information, style='Start.TButton')
    start_button.place(relx=0.3, rely=0.3)
    start_button.grid(row=5, column=1, pady=40,padx=10)


    # Add space below the button
    

    # Run the application
    
