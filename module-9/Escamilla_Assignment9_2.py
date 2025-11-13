"""
---

# CSD325-T301 - Week 9.2 Assignment: JSON and Application Programming Interfaces (APIs)

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
- 1.0.4 - 2025.10.06 Week5: Forest Fire Simulation 1
- 1.0.5 - 2025.10.13 Week6: Forest Fire Simulation 2
- 1.0.6 - 2025.10.20 Week7: Test Cases
- 1.0.7 - 2025.10.27 Week8: JSON Practice
- 1.0.8 - 2025.11.03 Week9: JSON and Application Programming Interfaces (APIs)

**Description**:
Create a program that includes the following:
- Find a simple API. The link above has a couple that you can work with, but the examples are not in Python...the concept is the same..
- Test the connection to your API, output results.
- Print out the response from the request, with no formatting.
- Print out the response with same formatting as the tutorial program.
- Run the program and take a screenshot of the results. Paste that screenshot into your Word document.

"""
# ==================================================
# Description:
#    Testing basic API connection to Google
# ==================================================
# import requests
#
# # Test connection to Google
# print('Testing connection to Google...')
# response = requests.get('http://www.google.com')
# print(response.status_code)


# ==================================================
# Description:
#    API Tutorial - Retrieving current astronauts in space
# ==================================================
# import requests
# import json
# 
# def main():
#     print("=" * 50)
#     print("ASTRONAUTS API TUTORIAL")
#     print("=" * 50)
# 
#     # API endpoint for astronauts currently in space
#     api_url = "http://api.open-notify.org/astros.json"
# 
#     # Test the connection
#     print("\n1. Testing connection to Open Notify API...")
#     response = requests.get(api_url)
#     print(f"   Status Code: {response.status_code}")
# 
#     if response.status_code == 200:
#         print("   Connection successful!")
#     else:
#         print("   Connection failed!")
#         return
# 
#     # Get the raw response
#     print("\n2. Raw JSON response:")
#     print("-" * 50)
#     print(response.text)
#     print("-" * 50)
# 
#     # Parse the JSON response
#     data = response.json()
# 
#     # Display formatted output
#     print("\n3. Formatted Output:")
#     print("-" * 50)
#     print(f"Number of people in space: {data['number']}")
#     print(f"\nAstronauts currently in space:")
#     print()
# 
#     for person in data['people']:
#         print(f"   Name: {person['name']}")
#         print(f"   Craft: {person['craft']}")
#         print()
# 
#     print("=" * 50)
# 
# 
# if __name__ == "__main__":
#     main()


# ==================================================
# Description:
#    International Space Station (ISS) Location API
# ==================================================
import requests
import json
from datetime import datetime

def main():
    print("=" * 50)
    print("ISS LOCATION TRACKER")
    print("=" * 50)

    # API endpoint for ISS current location
    api_url = "http://api.open-notify.org/iss-now.json"

    # Step 1: Test the connection
    print("\n1. Testing connection to ISS Location API...")
    response = requests.get(api_url)
    print(f"   Status Code: {response.status_code}")
    print(f"   Response Type: {type(response)}")

    if response.status_code == 200:
        print("   ✓ Connection successful!")
    else:
        print("   ✗ Connection failed!")
        return

    # Step 2: Print raw response (no formatting)
    print("\n2. Raw JSON Response (Unformatted):")
    print("-" * 50)
    print(response.text)
    print("-" * 50)

    # Step 3: Parse and format the response (similar to tutorial)
    print("\n3. Formatted Response (Tutorial Style):")
    print("-" * 50)

    # Parse JSON data
    iss_data = response.json()

    # Extract latitude and longitude
    latitude = iss_data['iss_position']['latitude']
    longitude = iss_data['iss_position']['longitude']
    timestamp = iss_data['timestamp']

    # Convert timestamp to readable format
    readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Display formatted information
    print(f"\n   International Space Station Current Location:")
    print(f"   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"   Latitude:  {latitude}°")
    print(f"   Longitude: {longitude}°")
    print(f"   Timestamp: {timestamp}")
    print(f"   Date/Time: {readable_time} UTC")
    print(f"   Message:   {iss_data['message']}")

    # Additional formatting - display all data in a structured way
    print(f"\n   Complete ISS Data:")
    print(f"      Message: {iss_data['message']}")
    print(f"      Timestamp: {timestamp}")
    print(f"      ISS Position:")
    print(f"         Latitude:  {latitude}°")
    print(f"         Longitude: {longitude}°")

    # Calculate and display hemisphere information
    lat_hemisphere = "North" if float(latitude) >= 0 else "South"
    lon_hemisphere = "East" if float(longitude) >= 0 else "West"

    print(f"\n   Location Details:")
    print(f"      Hemisphere: {lat_hemisphere}ern {lon_hemisphere}ern")
    print(f"      Coordinates: {abs(float(latitude)):.2f}°{lat_hemisphere[0]}, "
          f"{abs(float(longitude)):.2f}°{lon_hemisphere[0]}")

    print("\n" + "=" * 50)
    print("The ISS orbits Earth every ~90 minutes at ~17,500 mph!")
    print("Run the program again in a few seconds to see it move!")
    print("=" * 50)


if __name__ == "__main__":
    main()


    