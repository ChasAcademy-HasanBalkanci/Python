from menu import display_menu
from monitor import start_monitoring, list_active_monitoring
from alarms import create_alarm, show_alarms, remove_alarm, load_alarms, save_alarms
from logger import setup_logging
from email_notifier import send_email_notification

def main():
    setup_logging()  # Set up logging
    load_alarms()  # Load alarms from file
    
    while True:
        display_menu()
        choice = input("Enter a choice: ")
        
        if choice == '1':
            start_monitoring()
        elif choice == '2':
            list_active_monitoring()
        elif choice == '3':
            create_alarm()
        elif choice == '4':
            show_alarms()
        elif choice == '5':
            start_watch_mode()  # Start watch mode (function not shown here)
        elif choice == '6':
            remove_alarm()
        elif choice == '7':
            print("Exiting...")
            save_alarms()  # Save alarms to file
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()