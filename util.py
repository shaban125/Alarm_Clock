# utils.py

import time
from datetime import datetime
from tkinter import messagebox
import threading

# Function to continuously update and display the current time
def get_current_time(label):
    def update_time():
        current_time = datetime.now().strftime("%I:%M:%S %p")  # Fetch current time in 12-hour format
        label.config(text=current_time)  # Update the label with the current time
        label.after(1000, update_time)  # Refresh every 1 second
    update_time()

# Function to play alarm sound (placeholder function)
def play_alarm_sound():
    # Replace this with code to play an actual sound file if needed
    messagebox.showinfo("Alarm!", "Wake up! It's time!")  # Show notification when alarm goes off

# Function to check if the current time matches the alarm time
def check_alarm(set_time, period, alarm_label):
    def alarm_thread():
        while True:
            current_time = datetime.now().strftime("%I:%M %p")  # Get current time in hours and minutes
            if current_time == f"{set_time} {period}":  # Compare with the set alarm time
                play_alarm_sound()  # Play sound if alarm time matches
                break
            time.sleep(1)  # Check every second

    # Start a new thread for the alarm check
    alarm_threading = threading.Thread(target=alarm_thread)
    alarm_threading.start()
    alarm_label.config(text=f"Alarm set for: {set_time} {period}")  # Display the set alarm time
