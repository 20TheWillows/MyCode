import sys, os
import re

# Find code directory relative to our directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Functions')))

import General_Functions


def get_valid_year():
    year = input("Enter your chosen year:")
    # Check number format
    num_format = re.compile(r"^[\-]?[1-9][0-9]*\.?[0-9]+$")
    if not re.match(num_format,year):
        raise TypeError("Year must be a number")
    # Convert number to integer
    year = int(year)
    # Must be larger than 0 and less than 3000
    if year < 0:
        raise ValueError("Year cannot be negative")
    if year > 3000:
        raise ValueError("Year must be less than 3000")
    return year
#------------------
# Main function
#------------------
if __name__ == "__main__":
    try:
        # Get year
        year = get_valid_year()
        # Get Roman numeral representation
        print(General_Functions.get_roman_year(year))
    except Exception as error:
        print("Exception: " + str(error))
    
