# Program Name: ITS320_CTA3_Option1.py
# Author: Kayla Sherwood
# Date: 3/2/2025
#-------------------------------------------
# Pseudocode:
# 1. Define a function `get_gto_value(year)` that:
#    - Checks the input year against predefined ranges.
#    - Returns the corresponding estimated value.
# 2. Prompt the user to enter a year.
# 4. Call the function to determine the Ferrari 250 GTO value for that year.
# 5. Display the result to the user.
#-------------------------------------------
# Program Inputs:
# - A numerical year entered by the user.
#-------------------------------------------
# Program Outputs:
# - The estimated Ferrari 250 GTO value for the given year.
#-------------------------------------------

def get_gto_value(year):
    if 1962 <= year <= 1964:
        return "$18,500"
    elif 1965 <= year <= 1968:
        return "$6,000"
    elif 1969 <= year <= 1971:
        return "$12,000"
    elif 1972 <= year <= 1975:
        return "$48,000"
    elif 1976 <= year <= 1980:
        return "$200,000"
    elif 1981 <= year <= 1985:
        return "$650,000"
    elif 1986 <= year <= 2012:
        return "$35,000,000"
    elif 2013 <= year <= 2014:
        return "$52,000,000"
    else:
        return "No data available for this year"


year = int(input("Enter a year: ")) 
value = get_gto_value(year) 

print(f"The estimated value of a Ferrari 250 GTO in {year} was {value}.") 


