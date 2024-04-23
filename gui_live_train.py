import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

def fetch_train_status():
    # Get the train number from the entry field
    train_number = entry_train_number.get()

    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    # API endpoint for fetching live train status
    api_endpoint = f"https://api.railwayapi.com/v2/live/train/{train_number}/date/{current_date}/apikey/your_api_key/"

    try:
        response = requests.get(api_endpoint)
        data = response.json()

        # Extract relevant information from the API response
        current_status = data['position']
        station = data['station']['name']
        station_code = data['station']['code']
        schedule_arrival = data['status']

        # Update the label with the train status
        status_label.config(text=f"Current Status: {current_status}\n"
                                  f"Station: {station} ({station_code})\n"
                                  f"Schedule Arrival: {schedule_arrival}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Live Train Status")

# Create a frame for input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Train Number Entry
tk.Label(input_frame, text="Train Number:").grid(row=0, column=0)
entry_train_number = tk.Entry(input_frame)
entry_train_number.grid(row=0, column=1)

# Button to fetch train status
fetch_button = tk.Button(input_frame, text="Fetch Status", command=fetch_train_status)
fetch_button.grid(row=0, column=2, padx=10)

# Create a label to display the status
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the application
root.mainloop()
