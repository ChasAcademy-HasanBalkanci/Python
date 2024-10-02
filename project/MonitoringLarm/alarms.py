import json
from logger import log_event

# Global dictionary to store alarms for CPU, memory, and disk
alarms = {
    "cpu": [],
    "memory": [],
    "disk": []
}

def create_alarm():
    """Function to create alarms for CPU, Memory, or Disk usage."""
    print("1. Create CPU Usage Alarm")
    print("2. Create Memory Usage Alarm")
    print("3. Create Disk Usage Alarm")
    print("4. Back to Main Menu")
    
    choice = input("Your choice: ")
    
    # Check for valid choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid option.")
        return

    if choice == '4':
        return  # Go back to main menu without further processing

    try:
        threshold = int(input("Set alarm level (0-100): "))
        if not 0 <= threshold <= 100:
            raise ValueError  # Raise an error if out of bounds
    except ValueError:
        print("Invalid level. Please enter a number between 0 and 100.")
        return  # Exit the function if input is invalid

    # Set the alarm based on user's choice
    if choice == '1':
        alarms["cpu"].append(threshold)
        log_event(f"CPU alarm set at {threshold}%")
    elif choice == '2':
        alarms["memory"].append(threshold)
        log_event(f"Memory alarm set at {threshold}%")
    elif choice == '3':
        alarms["disk"].append(threshold)
        log_event(f"Disk alarm set at {threshold}%")
    
    print(f"Alarm level set at {threshold}%.")

    # Optionally save the alarms to disk here if needed
    # save_alarms()
    

def show_alarms():
    print("--- Alarms ---")
    for alarm_type, values in alarms.items():
        for threshold in sorted(values):
            print(f"{alarm_type.capitalize()} alarm: {threshold}%")

def remove_alarm():
    print("Select alarm to remove:")
    show_alarms()
    # Removal logic can be added here

def save_alarms():
    with open('settings.json', 'w') as f:
        json.dump(alarms, f)

def load_alarms():
    try:
        with open('settings.json', 'r') as f:
            global alarms
            alarms = json.load(f)
    except FileNotFoundError:
        pass
