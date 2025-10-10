'''
---

# CSD325-T301 - Week 4.2 Assignment: CSV Read and Matplotlib

---

**Professor**: John Woods<br>
**@Copyright**: BELLEVUE.edu<br>
**Modified By**: Carlos E. Escamilla<br>
**Email**: CEEscamilla@my365.BELLEVUE.edu<br>
**OS**: Windows 11 x64<br>
**Processor**: i9-13900<br>
**GPU**: NVIDIA GeForce RTX 3060<br>
**IDE**: DataSpell 2025.2<br>
**Interpreter**: Python 3.12<br>
**Libraries Managed by**: Miniforge3

---

**Version**:
- 1.0.0 - 2025.09.08 Week1: Programming Logic
- 1.0.1 - 2025.09.15 Week2: Documenting Debugging
- 1.0.2 - 2025.09.22 Week3: Brownfield Development
- 1.0.3 - 2025.09.29 Week4: CSV Read and Matplotlib

**Description**:
This program reads weather data from a CSV file and allows the user to
visualize either high or low temperatures for Sitka, Alaska in 2018.
The user can select from a menu to view highs, lows, or exit the program.

**Modifications from original**:
- Added menu system for user interaction
- Added functionality to display low temperatures in blue
- Added loop to allow multiple visualizations
- Added sys module for clean exit
- Added input validation and error handling

'''

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

def display_menu():
    """Display the menu options to the user."""
    print("\n" + "=" * 50)
    print("   Sitka Weather Temperature Visualization")
    print("=" * 50)
    print("\nPlease select an option:")
    print("  1. View High Temperatures")
    print("  2. View Low Temperatures")
    print("  3. Exit Program")
    print("-" * 50)


def get_user_choice():
    """
    Get and validate user menu choice.

    Returns:
        str: User's menu choice ('1', '2', or '3')
    """
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def read_temperature_data(filename, temp_type='high'):
    """
    Read temperature data from CSV file.

    Args:
        filename (str): Path to the CSV file
        temp_type (str): Type of temperature to read ('high' or 'low')

    Returns:
        tuple: Two lists containing dates and temperatures
    """
    dates, temps = [], []

    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Determine which column to read based on temp_type
            # Column 5 contains highs, column 6 contains lows
            temp_column = 5 if temp_type == 'high' else 6

            # Get dates and temperatures from the file
            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)

                    temp = int(row[temp_column])
                    temps.append(temp)
                except ValueError:
                    # Skip rows with invalid data
                    print(f"Warning: Skipping invalid data in row")
                    continue

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return dates, temps


def plot_temperatures(dates, temps, temp_type='high'):
    """
    Create and display a temperature plot.

    Args:
        dates (list): List of datetime objects
        temps (list): List of temperature values
        temp_type (str): Type of temperature ('high' or 'low')
    """
    # Set color based on temperature type
    color = 'red' if temp_type == 'high' else 'blue'
    title_text = f"Daily {temp_type} temperatures - 2018"

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color, linewidth=2)

    # Format the plot
    plt.title(title_text, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Display the plot
    plt.show()


def main():
    """Main program function that controls the flow."""
    filename = 'sitka_weather_2018_simple.csv'

    # Display welcome message
    print("\n" + "*" * 50)
    print("  Welcome to Sitka Weather Temperature Viewer!")
    print("*" * 50)
    print("\nThis program displays temperature data from 2018.")

    # Main program loop
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            # Display high temperatures
            print("\nLoading high temperature data...")
            dates, highs = read_temperature_data(filename, 'high')
            plot_temperatures(dates, highs, 'high')

        elif choice == '2':
            # Display low temperatures
            print("\nLoading low temperature data...")
            dates, lows = read_temperature_data(filename, 'low')
            plot_temperatures(dates, lows, 'low')

        elif choice == '3':
            # Exit the program
            print("\n" + "=" * 50)
            print("  Thank you for using the Temperature Viewer!")
            print("  Goodbye!")
            print("=" * 50 + "\n")
            sys.exit(0)


# Run the program
if __name__ == "__main__":
    main()


