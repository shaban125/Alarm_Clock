import tkinter as tk
from datetime import datetime
import time
import threading
from playsound import playsound  # Import the playsound library

# Function to get the current time
def get_current_time():
    return datetime.now().strftime("%I:%M %p")  # Returns time in HH:MM AM/PM format

# Function to play the alarm sound
def play_alarm_sound():
    playsound('hen_sound.mp3')  # Replace with your sound file name

# Function to compare the current time with the set alarm time
def check_alarm(alarm_time, alarm_label):
    def alarm_thread():
        while True:
            current_time = get_current_time()
            alarm_label.config(text=f"Current Time: {current_time}")
            if current_time == alarm_time:
                play_alarm_sound()  # Play the alarm sound when the time matches
                break
            time.sleep(1)  # Check every second

    # Start the alarm checking in a separate thread
    threading.Thread(target=alarm_thread).start()

# Function to set the alarm
def set_alarm(alarm_time_entry, alarm_label):
    alarm_time = alarm_time_entry.get()  # Get the alarm time from the input field
    alarm_label.config(text=f"Alarm set for: {alarm_time}")
    check_alarm(alarm_time, alarm_label)  # Start checking the alarm

# Function to create the GUI window
def create_gui():
    window = tk.Tk()
    window.title("Simple Alarm Clock")
    window.geometry("300x200")

    # Label and Entry for setting the alarm time
    tk.Label(window, text="Set Alarm Time (HH:MM AM/PM):").pack(pady=10)
    alarm_time_entry = tk.Entry(window, width=20)
    alarm_time_entry.pack(pady=5)

    # Label to display the current time and alarm status
    alarm_label = tk.Label(window, text="", font=("Helvetica", 10))
    alarm_label.pack(pady=10)

    # Button to set the alarm
    set_button = tk.Button(window, text="Set Alarm", command=lambda: set_alarm(alarm_time_entry, alarm_label))
    set_button.pack(pady=5)

    # Run the main loop
    window.mainloop()

# Main function to run the GUI
if __name__ == "__main__":
    create_gui()
