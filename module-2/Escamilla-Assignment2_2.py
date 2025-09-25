'''
---

# CSD325-T301 - Week 2.2 Assignment: Documenting Debugging

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
- 1.0.1 - 2025.09.15 Week2: Documenting Debugging

**Description**:
This program created on 06/24/2024 from Week4 CIS245 assignment demonstrates the usage of functions in Python by converting miles to kilometers.
It prompts the user to input a number of miles, then uses a dedicated function to perform the conversion and display both values.
The program includes error handling for invalid inputs and uses a conversion factor of 1 mile = 1.60934 kilometers.

'''
# ============================================================================
# Assignment CIS245-T303 Week4 - Convert miles to kilometers
# ============================================================================
# Write a program that uses a function to convert miles to kilometers. Your program
# should prompt the user for the number of miles driven, then call a function that
# converts miles to kilometers. The program should then display the total miles and kilometers.
#   Note: 1 Mile = 1.60934 Kilometers
# ============================================================================
def main():
    # Display the intro screen
    fnIntro()

    try:
        # Get the number of miles
        iInMiles = int(input("Enter the number of miles to convert: "))

        # Convert Miles to Kilometers.
        iKilometers = fnMiles2Kilometers(iInMiles)
        print(iInMiles, "miles coverts to", iKilometers[0], iKilometers[1])

    except:
        print("An exception occurred, try again by entering only a number\n")
        main()


# ============================================================================
# The intro function displays an introductory screen
# ============================================================================
def fnIntro():
    print("Escamillas Miles to Kilometers Conversion")
    print("Note: 1 Mile = 1.60934 Kilometers\n")


# ============================================================================
# Miles to Kilometers Function
# ============================================================================
def fnMiles2Kilometers(iMiles):
    fKilometers = iMiles * 1.60934
    return fKilometers, "kilometers."


# ============================================================================
# Call the main function.
# ============================================================================
main()


