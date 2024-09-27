# # ui.py

# import tkinter as tk
# from tkinter import messagebox

# # Function to initialize the GUI window
# def create_gui():
#     # Create the main window
#     window = tk.Tk()
#     window.title("Alarm Clock")
#     window.geometry("400x300")  # Set window size
#     window.config(bg="#2C3E50")  # Set background color for an attractive look

#     # Heading Label
#     title_label = tk.Label(window, text="Alarm Clock", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
#     title_label.pack(pady=10)

#     # Frame for time input
#     time_frame = tk.Frame(window, bg="#2C3E50")
#     time_frame.pack(pady=20)

#     # Hour input field
#     hour_label = tk.Label(time_frame, text="Hour:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
#     hour_label.grid(row=0, column=0, padx=5)
#     hour_entry = tk.Entry(time_frame, width=5, font=("Helvetica", 12))
#     hour_entry.grid(row=0, column=1, padx=5)

#     # Minute input field
#     minute_label = tk.Label(time_frame, text="Minute:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
#     minute_label.grid(row=0, column=2, padx=5)
#     minute_entry = tk.Entry(time_frame, width=5, font=("Helvetica", 12))
#     minute_entry.grid(row=0, column=3, padx=5)

#     # AM/PM dropdown
#     period_label = tk.Label(time_frame, text="AM/PM:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
#     period_label.grid(row=0, column=4, padx=5)
#     period_var = tk.StringVar(value="AM")
#     period_option = tk.OptionMenu(time_frame, period_var, "AM", "PM")
#     period_option.config(width=4, font=("Helvetica", 10))
#     period_option.grid(row=0, column=5, padx=5)

#     # Function placeholder for setting the alarm (to be implemented later)
#     def set_alarm():
#         messagebox.showinfo("Alarm Set", "Alarm has been set!")

#     # Set Alarm Button
#     set_button = tk.Button(window, text="Set Alarm", font=("Helvetica", 12), bg="#27AE60", fg="white", command=set_alarm)
#     set_button.pack(pady=10)

#     # Exit Button
#     exit_button = tk.Button(window, text="Exit", font=("Helvetica", 12), bg="#E74C3C", fg="white", command=window.quit)
#     exit_button.pack(pady=10)

#     # Run the main loop
#     window.mainloop()
# ui.py

import tkinter as tk
from tkinter import messagebox
from util import get_current_time, check_alarm  # Import functions from utils.py

# Function to initialize the GUI window
def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Alarm Clock")
    window.geometry("600x800")  # Set window size
    window.config(bg="#2C3E50")  # Set background color for an attractive look

    # Heading Label
    title_label = tk.Label(window, text="Alarm Clock", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
    title_label.pack(pady=10)

    # Current Time Display
    current_time_label = tk.Label(window, font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
    current_time_label.pack(pady=10)

    # Display the current time continuously
    get_current_time(current_time_label)

    # Frame for time input
    time_frame = tk.Frame(window, bg="#2C3E50")
    time_frame.pack(pady=20)

    # Hour input field
    hour_label = tk.Label(time_frame, text="Hour:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
    hour_label.grid(row=0, column=0, padx=5)
    hour_entry = tk.Entry(time_frame, width=5, font=("Helvetica", 12))
    hour_entry.grid(row=0, column=1, padx=5)

    # Minute input field
    minute_label = tk.Label(time_frame, text="Minute:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
    minute_label.grid(row=0, column=2, padx=5)
    minute_entry = tk.Entry(time_frame, width=5, font=("Helvetica", 12))
    minute_entry.grid(row=0, column=3, padx=5)

    # AM/PM dropdown
    period_label = tk.Label(time_frame, text="AM/PM:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
    period_label.grid(row=0, column=4, padx=5)
    period_var = tk.StringVar(value="AM")
    period_option = tk.OptionMenu(time_frame, period_var, "AM", "PM")
    period_option.config(width=4, font=("Helvetica", 10))
    period_option.grid(row=0, column=5, padx=5)

    # Alarm Label to Display Set Time
    alarm_set_label = tk.Label(window, font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
    alarm_set_label.pack(pady=10)

    # Function to set the alarm
    def set_alarm():
        hour = hour_entry.get()
        minute = minute_entry.get()
        period = period_var.get()

        # Check if input fields are not empty
        if hour.isdigit() and minute.isdigit():
            alarm_time = f"{int(hour):02}:{int(minute):02}"  # Format the time to HH:MM
            check_alarm(alarm_time, period, alarm_set_label)  # Call function to check the alarm
        else:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for hours and minutes.")

    # Set Alarm Button
    set_button = tk.Button(window, text="Set Alarm", font=("Helvetica", 12), bg="#27AE60", fg="white", command=set_alarm)
    set_button.pack(pady=10)

    # Exit Button
    exit_button = tk.Button(window, text="Exit", font=("Helvetica", 12), bg="#E74C3C", fg="white", command=window.quit)
    exit_button.pack(pady=10)

    # Run the main loop
    window.mainloop()

