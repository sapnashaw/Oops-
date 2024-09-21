#15. Implement a static method in a class that checks if a given year is a leap year.

class YearChecker:
    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

# Example usage
year = 2024
if YearChecker.is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
