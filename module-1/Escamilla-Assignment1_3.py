'''
---

# CSD325-T301 - Week 1.3 Assignment: On the Wall + Flowchart

---

**Professor**: John Woods<br>
**@Copyright**: BELLEVUE.edu<br>
**Author**: Carlos E. Escamilla<br>
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

**Description**:
For this assignment, you have two tasks. The first is to create a flowchart (or flowcharts) for the following requirements, then to write a Python program that produces the required results:
If you are not familiar with the reverse counting song "100 bottles of beer on the wall", you'll need to do a little research to familiarize yourself with it.

- Ask the user how many bottles of beer are on the wall.
- Pass that input to a function that manages the countdown.
- The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
- Once the count is down to 1, change lyrics to show "1 bottle of beer..."
- At the end of the countdown, get back to the main program and remind the user to buy more beer.
- The output should look similar to:
    Enter number of bottles: 3
    3 bottles of beer on the wall, 3 bottles of beer.
    Take one down and pass it around, 2 bottle(s) of beer on the wall.

    2 bottles of beer on the wall, 2 bottles of beer.
    Take one down and pass it around, 1 bottle(s) of beer on the wall.

    1 bottles of beer on the wall, 1 bottles of beer.
    Take one down and pass it around, 0 bottle(s) of beer on the wall.

    Time to buy more bottles of beer.

'''

def countdown_bottles(num_bottles):
    """
    Function to manage the countdown of bottles of beer on the wall

    Args:
        num_bottles (int): The starting number of bottles
    """
    current_bottles = num_bottles

    while current_bottles > 0:
        if current_bottles > 1:
            # Display lyrics for multiple bottles
            print(f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer.")
        elif current_bottles == 1:
            # Display lyrics for the last bottle
            print(f"{current_bottles} bottle of beer on the wall, {current_bottles} bottle of beer.")

        current_bottles -= 1
        print(f"Take one down and pass it around, {current_bottles} bottle(s) of beer on the wall.\n")


def main():
    """
    Main program function that gets user input and manages the program flow
    """
    try:
        # Get user input for number of bottles
        num_bottles = int(input("Enter number of bottles: "))

        # Validate input (must be positive)
        if num_bottles <= 0:
            print("Please enter a positive number of bottles.")
            return

        # Call the countdown function
        countdown_bottles(num_bottles)

        # Remind user to buy more beer
        print("Time to buy more bottles of beer.")

    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()


