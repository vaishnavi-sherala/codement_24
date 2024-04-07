import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from PIL import Image, ImageTk
from odd import window_english
from odd1 import window_marathi

bg_photo = None  # Declare bg_photo as a global variable

# Function to translate text using Google Translate API
def translate_text(text, target_language='hi'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Function to open the next page+
def open_next_page():
    global window  # Use the global variable for the main window
    window.destroy()  # Close the current window
    
    next_window = tk.Tk()
    # Create a new top-level window
    next_window.title("Next Page")
    next_window.configure(bg='#0000FF')  # Set the background color to blue
    # Set the title for the new window
    original_text = "Select your choice"
    translated_text = translate_text(original_text, target_language='hi')
    
    tts = gTTS(translated_text, lang='hi')
    tts.save("sakshi.mp3")

    # Create a label with the translated text
    next_label = tk.Label(next_window, text=translated_text, font=("Arial", 18), wraplength=300)
    next_label.pack(pady=20)
    next_window.geometry("600x400+{}+{}".format(int(next_window.winfo_screenwidth() / 2 - 300), int(next_window.winfo_screenheight() / 2 - 200)))
   
    # Schedule the playing of the speech after a short delay (e.g., 100 milliseconds)
    next_window.after(100, lambda: playsound("sakshi.mp3"))
   
    # Function to show the English window
    def show_english():
        next_window.destroy()
        window_english()
        
    # Function to show the Marathi window
    def show_marathi():
        next_window.destroy()
        window_marathi()

    # Create buttons for English and Marathi options
    english_button = tk.Button(next_window, text="English", command=show_english, font=("Arial", 18))
    english_button.place(relx=0.5, rely=0.6, anchor="center")
    english_button.pack(pady=10)
    
    marathi_button = tk.Button(next_window, text="मराठी", command=show_marathi, font=("Arial", 18))
    marathi_button.place(relx=0.5, rely=0.7, anchor="center")
    marathi_button.pack(pady=10)
 
# Create the main window//..
window = tk.Tk()
window.title("Welcome to Our GramSehat")
window.geometry("600x400+{}+{}".format(int(window.winfo_screenwidth() / 2 - 300), int(window.winfo_screenheight() / 2 - 200)))

#Load and display the background image for the main window
bg_image = Image.open("C:\\Users\\Hp\\OneDrive\\Desktop\\codement\\1.jpg")
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to Sehat-Sathi", font=("Arial", 24), fg="blue")
welcome_label.place(relx=0.5, rely=0.4, anchor="center")

# Create a styled start button that opens the next page
start_button_style = ttk.Style()
start_button_style.configure('Start.TButton', foreground='blue', font=('Arial', 18))

start_button = ttk.Button(window, text="Start", command=open_next_page, style='Start.TButton')
start_button.place(relx=0.5, rely=0.6, anchor="center")

# Run the main loop
window.mainloop()
