import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Meet Doctor")
root.geometry("600x400")

# Load doctor images
doctor_images = ["1.jpg","2.jpg","3.jpg"]
for i in range(1, 4):
    image_path = f"doctor{i}.jpg"  # Replace with actual image paths
    doctor_image = Image.open(image_path)
    doctor_image = doctor_image.resize((200, 200), Image.ANTIALIAS)
    doctor_images.append(ImageTk.PhotoImage(doctor_image))

# Function to handle button clicks
def meet_doctor(doctor_num):
    print(f"Meeting Doctor {doctor_num}")

# Create labels for doctor images
labels = []
for i, image in enumerate(doctor_images):
    label = tk.Label(root, image=image)
    label.pack(pady=10)
    labels.append(label)

# Create buttons for each doctor
buttons = []
for i in range(3):
    button = tk.Button(root, text=f"Meet Doctor {i+1}", command=lambda num=i+1: meet_doctor(num))
    button.pack(pady=5)
    buttons.append(button)

# Run the application
root.mainloop()
