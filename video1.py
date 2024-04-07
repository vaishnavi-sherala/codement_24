# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from datetime import datetime
# import webbrowser
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def vedo():
#     # Create the main window
#     root = tk.Tk()
#     root.title("Meet Doctor")
#     root.geometry("800x300")

#     # Define doctor data (images, names, meeting times, and button text)
#     doctors_data = [
#         {"image": "11.jpeg", "name": "Dr. Subhash Bhange", "meeting_time": "6:00 AM to 9:00 AM", "website": "http://example.com"},
#         {"image": "2.jpeg", "name": "Dr.  Mukund Ray", "meeting_time": "3:00 PM to 6:00 PM", "website": "http://example.com"},
#         {"image": "3.jpeg", "name": "Dr. Abhijit Sonawane", "meeting_time": "6:00 AM to 2:00 PM", "website": "http://example.com"}
#     ]

#     # Load doctor images, names, and meeting times
#     doctor_images = []
#     doctor_names = []
#     meeting_times = []
#     doctor_websites = ["https://chat.openai.com/"]  # Store doctor websites
#     for doctor in doctors_data:
#         image_path = doctor["image"]
#         doctor_image = Image.open(image_path)
#     #    doctor_image = doctor_image.resize((200, 200), Image.ANTIALIAS)  # Resize image
#         photo_image = ImageTk.PhotoImage(doctor_image)
#         doctor_images.append(photo_image)
#         doctor_names.append(doctor["name"])
#         meeting_times.append(doctor["meeting_time"])
#         doctor_websites.append(doctor["website"])

#     def meet_doctor(doctor_num):
#         doctor_name = doctors_data[doctor_num]['name']
#         current_time = datetime.now().strftime("%I:%M %p")  # Get current time in HH:MM AM/PM format
#         meeting_time_range = doctors_data[doctor_num]["meeting_time"]
#         start_time_str, end_time_str = meeting_time_range.split(" to ")

#         start_time = datetime.strptime(start_time_str, "%I:%M %p").strftime("%I:%M %p")  # Convert start time to HH:MM AM/PM format
#         end_time = datetime.strptime(end_time_str, "%I:%M %p").strftime("%I:%M %p")  # Convert end time to HH:MM AM/PM format

#         if start_time <= current_time <= end_time:
#             messagebox.showinfo("Doctor is available", f"Meeting with Dr. {doctors_data[doctor_num]['name']} . ")
#             webbrowser.open('http://127.0.0.1:8000/meeting/?roomID=123')
#             send_email(doctor_name)
#         else:
#             messagebox.showerror("Doctor Not Available", f"Doctor {doctors_data[doctor_num]['name']} is not available.")
#             send_email(doctor_name)

#     def send_email(doctor_name):
#         # Email configuration
#         sender_email = "shrutikale5531@gmail.com"
#         receiver_email = "sheralavaishnavi766@gmail.com"
#         password = "qxuiahjzmsjxurag"

#         # Create message object
#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = receiver_email
#         msg['Subject'] = f"Meeting Request from Patient"

#         # Email body
#         body = f"Dear Dr. {doctor_name},\n\nI would like to schedule a meeting with you. Please let me know your availability.\n\nmeet id: http://127.0.0.1:8000/meeting/?roomID=123"
#         msg.attach(MIMEText(body, 'plain'))

#         # Send email using SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender_email, password)
#             server.send_message(msg)   

#     # Create labels for doctor images, names, meeting times, and buttons horizontally
#     for i in range(3):
#         frame = tk.Frame(root)
#         frame.pack(side="left", padx=10)
        
#         label = tk.Label(frame, image=doctor_images[i])
#         label.image = doctor_images[i]  # Keep a reference to the image object
#         label.pack()
        
#         name_label = tk.Label(frame, text=doctor_names[i])
#         name_label.pack()

#         time_label = tk.Label(frame, text=meeting_times[i])  # Add label for meeting time
#         time_label.pack()
        
#         button = tk.Button(frame, text=f"Meet {doctor_names[i]}", command=lambda num=i: meet_doctor(num))
#         button.pack()


# # Call the function to start the application
 

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def vedo():
    # Create the main window
    root = tk.Tk()
    root.title("Meet Doctor")
    root.geometry("600x400")

    # Label for displaying "Available Doctors"
    label_available_doctors = tk.Label(root, text="Available Doctors", font=("Arial", 18, "bold"), bg="#e6e6e6")
    label_available_doctors.pack(pady=5)

    # Define doctor data (images, names, meeting times, and button text)
    doctors_data = [
        {"image": "11.jpeg", "name": "Dr. Subhash Bhange", "meeting_time": "6:00 AM to 9:00 AM", "website": "http://example.com"},
        {"image": "2.jpeg", "name": "Dr.  Mukund Ray", "meeting_time": "3:00 PM to 6:00 PM", "website": "http://example.com"},
        {"image": "3.jpeg", "name": "Dr. Abhijit Sonawane", "meeting_time": "6:00 AM to 2:00 PM", "website": "http://example.com"}
    ]

    # Load doctor images, names, and meeting times
    doctor_images = []
    doctor_names = []
    meeting_times = []
    doctor_websites = ["https://chat.openai.com/"]  # Store doctor websites
    for doctor in doctors_data:
        image_path = doctor["image"]
        doctor_image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(doctor_image)
        doctor_images.append(photo_image)
        doctor_names.append(doctor["name"])
        meeting_times.append(doctor["meeting_time"])
        doctor_websites.append(doctor["website"])

    def meet_doctor(doctor_num):
        doctor_name = doctors_data[doctor_num]['name']
        current_time = datetime.now().strftime("%I:%M %p")  # Get current time in HH:MM AM/PM format
        meeting_time_range = doctors_data[doctor_num]["meeting_time"]
        start_time_str, end_time_str = meeting_time_range.split(" to ")

        start_time = datetime.strptime(start_time_str, "%I:%M %p").strftime("%I:%M %p")  # Convert start time to HH:MM AM/PM format
        end_time = datetime.strptime(end_time_str, "%I:%M %p").strftime("%I:%M %p")  # Convert end time to HH:MM AM/PM format

        if start_time <= current_time <= end_time:
            messagebox.showinfo("Doctor is available", f"Meeting with Dr. {doctors_data[doctor_num]['name']} . ")
            webbrowser.open('http://127.0.0.1:8000/meeting/?roomID=123')
            send_email(doctor_name)
        else:
            messagebox.showerror("Doctor Not Available", f"Doctor {doctors_data[doctor_num]['name']} is not available.")
            send_email(doctor_name)

    def send_email(doctor_name):
        # Email configuration
        sender_email = "shrutikale5531@gmail.com"
        receiver_email = "sheralavaishnavi766@gmail.com"
        password = "qxuiahjzmsjxurag"

        # Create message object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Meeting Request from Patient"

        # Email body
        body = f"Dear Dr. {doctor_name},\n\nI would like to schedule a meeting with you. Please let me know your availability.\n\nmeet id: http://127.0.0.1:8000/meeting/?roomID=123"
        msg.attach(MIMEText(body, 'plain'))

        # Send email using SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)   

    # Calculate position for placing images in the middle
    frame_width = 200  # Width of each frame
    total_width = frame_width * len(doctors_data)  # Total width of all frames
    start_x = (800 - total_width) // 2  # Starting x-coordinate to center frames

    # Create frames for doctor images, names, and buttons
    for i, doctor in enumerate(doctors_data):
        frame = tk.Frame(root)
        frame.place(x=start_x + i * frame_width, y=200, anchor=tk.CENTER)

        label = tk.Label(frame, image=doctor_images[i])
        label.image = doctor_images[i]
        label.pack()

        name_label = tk.Label(frame, text=doctor_names[i])
        name_label.pack()

        time_label = tk.Label(frame, text=meeting_times[i])
        time_label.pack()

        button = tk.Button(frame, text=f"Meet {doctor_names[i]}", command=lambda num=i: meet_doctor(num))
        button.pack()




   

   


   