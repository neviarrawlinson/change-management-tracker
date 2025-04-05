import csv
import os
import uuid
from datetime import datetime

# File to store the change request data
file_name = "changes.csv"

# Function to create a new change request
def add_change_request():
    change_id = str(uuid.uuid4())[:8]  # Unique ID (shortened)
    requester = input("Enter Requester Name: ")
    description = input("Enter Change Description: ")
    risk_level = input("Enter Risk Level (Low, Medium, High): ").capitalize()
    requested_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    scheduled_date = input("Enter Scheduled Implementation Date (YYYY-MM-DD): ")
    approval_status = "Pending"
    implementation_status = "Not Started"

    new_change = [change_id, requester, description, risk_level, requested_date, scheduled_date, approval_status, implementation_status]

    file_exists = os.path.isfile(file_name)

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Change ID", "Requester", "Description", "Risk Level", "Requested Date", "Scheduled Date", "Approval Status", "Implementation Status"])
        writer.writerow(new_change)

    print(f"\nChange request '{change_id}' created successfully!\n")

# Function to view all change requests
def view_change_requests():
    if not os.path.exists(file_name):
        print("\nNo change requests found.\n")
        return

    print("\n📋 Change Management Register:\n")
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()

# Main menu
if __name__ == "__main__":
    while True:
        print("=== Change Management Tracker ===")
        print("1. Add a new change request")
        print("2. View all change requests")
        print("3. Exit")
        choice = input("Select an option (1, 2, or 3): ")

        if choice == "1":
            add_change_request()
        elif choice == "2":
            view_change_requests()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
