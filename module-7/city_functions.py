"""
---

# CSD325-T301 - Week 7.2 Assignment: Test Cases

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

"""

def city_country(city:str, country:str, population:int = None, language:str = None):
    """
    Format city and country information with optional population and language.

    Args:
        city (str): Name of the city
        country (str): Name of the country
        population (int, optional): Population of the city
        language (str, optional): Primary language spoken in the city

    Returns:
        str: Formatted string with city, country, and optional population and language
    """
    if population is not None and language is not None:
        return f"{city}, {country} - population {population}, {language}"
    elif population is not None:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


# Test calls with different parameter combinations
if __name__ == "__main__":
#     print("City, Country format:")
#     print(city_country("Santiago", "Chile"))
#     print(city_country("Tokyo", "Japan"))
#     print(city_country("Zaragoza", "Mexico"))

#     print("\nCity, Country, Population format:")
#     print(city_country("Santiago", "Chile", 5000000))
#     print(city_country("Tokyo", "Japan", 37000000))
#     print(city_country("Zaragoza", "Mexico", 16752))

    print("\nCity, Country, Population, Language format:")
    print(city_country("Santiago", "Chile", 5000000, "Spanish"))
    print(city_country("Tokyo", "Japan", 37000000, "Japanese"))
    print(city_country("Zaragoza", "Mexico", 16752, "Spanish"))


