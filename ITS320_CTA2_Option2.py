#-------------------------------------------
# Program Name: ITS320_CTA2_Option2.py
# Author: Kayla Sherwood
# Date: 2/23/25
#-------------------------------------------
# Pseudocode:
# 1. Prompt user to enter car details (brand, model, year, odometer readings, MPG).
# 2. Store input information in a dictionary.
# 3. Print the dictionary containing all car information.
#-------------------------------------------
# Program Inputs:
# - Car brand (string)
# - Car model (string)
# - Car year (integer)
# - Starting odometer reading (integer)
# - Ending odometer reading (integer)
# - Estimated miles per gallon (float)
#-------------------------------------------
# Program Outputs:
# - The dictionary with car details displayed to the user.
#-------------------------------------------

# Prompt user to input car details
car_brand = input('Enter car brand: ')
car_model = input('Enter car model: ')
car_year = int(input('Enter car year: '))  
start_odometer = int(input('Enter starting odometer reading (miles): '))  
end_odometer = int(input('Enter ending odometer reading (miles): '))  
mpg = float(input('Enter estimated miles per gallon (MPG): '))  

# Store data in a dictionary
car_info = {
    'Brand': car_brand,
    'Model': car_model,
    'Year': car_year,
    'Starting Odometer': start_odometer,
    'Ending Odometer': end_odometer,
    'Estimated MPG': mpg
}

# Print the dictionary containing all car information
print(car_info)  
