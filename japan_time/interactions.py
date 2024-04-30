import json
import threading
import time
import os
from main_server import server()

class Interactions:
    def __init__(self, filename='trains.json'):
        self.filename = filename

    def load_trains(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_trains(self, trains):
        with open(self.filename, 'w') as file:
            json.dump(trains, file, indent=4)

    def add_train(self, trains):
        call_sign = input("Enter train call sign: ")
        if call_sign in trains:
            print("Train already exists.")
        else:
            operator_name = input("Enter operator name: ")
            employee_number = input("Enter employee number: ")
            current_route = input("Enter current route: ")
            is_active = input("Is the train active? (yes/no): ").lower() == 'yes'
            current_stop = input("Enter current stop: ") if is_active else "N/A"
            current_conductor = input("Enter current conductor: ")
            crew_active_duration = input("Enter crew active duration: ")
            is_on_time = input("Is the train on time? (yes/no): ").lower() == 'yes'

            trains[call_sign] = {
                "operator_name": operator_name,
                "employee_number": employee_number,
                "current_route": current_route,
                "is_active": is_active,
                "current_stop": current_stop,
                "current_conductor": current_conductor,
                "crew_active_duration": crew_active_duration,
                "is_on_time": is_on_time
            }
            print(f"Train {call_sign} added.")
            self.save_trains(trains)

    def display_train_data(self, call_sign, trains, stop_event):
        while not stop_event.is_set():
            if call_sign in trains:
                print(f"\nCurrent data for {call_sign}:")
                for key, value in trains[call_sign].items():
                    print(f"{key}: {value}")
            else:
                print("\nTrain not found.")
            time.sleep(3)

    def select_train(self, trains):
        self.list_trains(trains)
        call_sign = input("Enter train call sign to select: ")
        if call_sign in trains:
            stop_event = threading.Event()
            display_thread = threading.Thread(target=self.display_train_data, args=(call_sign, trains, stop_event), daemon=True)
            display_thread.start()

            print("\nOptions for selected train:")
            print("1. Edit train")
            print("2. Delete train")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.edit_train(trains, call_sign)
            elif choice == '2':
                self.delete_train(trains, call_sign)
            else:
                print("Invalid choice.")
            
            stop_event.set()
            display_thread.join()
        else:
            print("Train not found.")

    def delete_train(self, trains, call_sign):
        del trains[call_sign]
        print(f"Train {call_sign} deleted.")
        self.save_trains(trains)

    def edit_train(self, trains, call_sign):
        print("Enter new values (leave blank to keep current value):")
        for key in list(trains[call_sign].keys()):
            new_value = input(f"{key} ({trains[call_sign][key]}): ")
            if new_value:
                if key in ['is_active', 'is_on_time']:
                    trains[call_sign][key] = new_value.lower() == 'yes'
                else:
                    trains[call_sign][key] = new_value
        print(f"Train {call_sign} updated.")
        self.save_trains(trains)

    def list_trains(self, trains):
        if trains:
            print("Current trains and their call signs:")
            for call_sign in trains:
                print(call_sign)
        else:
            print("No trains available.")

    def print_file_location(self):
        file_path = os.path.abspath(self.filename)
        print(f"The file {self.filename} is located at: {file_path}")

    def main(self):
        trains = self.load_trains()
        while True:
            self.print_file_location()
            print("\nMain Menu:")
            print("1. List all trains")
            print("2. Add a train")
            print("3. Select a train (to edit or delete)")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.list_trains(trains)
            elif choice == '2':
                self.add_train(trains)
            elif choice == '3':
                self.select_train(trains)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Unsupported choice")

if __name__ == "__main__":
    app = Interactions()
    app.main()