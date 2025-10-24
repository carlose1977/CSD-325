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
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Test cases for city_country function."""

    # def test_city_country(self):
    #     """Test city and country formatting."""
    #     result = city_country("santiago", "chile")
    #     self.assertEqual(result, "santiago, chile")

    # def test_city_country_population(self):
    #     """Test city, country, and population formatting."""
    #     result = city_country("santiago", "chile", 5000000)
    #     self.assertEqual(result, "santiago, chile - population 5000000")

    def test_city_country_population_language(self):
        """Test city, country, population, and language formatting."""
        result = city_country("santiago", "chile", 5000000, "Spanish")
        self.assertEqual(result, "santiago, chile - population 5000000, Spanish")


if __name__ == "__main__":
    unittest.main()
