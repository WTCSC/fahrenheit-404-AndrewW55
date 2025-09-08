def fahrToCelsius(temp):
    celsius = (temp - 32) * 5.0 / 9.0
    return celsius
def celsiusToFahr(temp):
    fahr = (temp * 9.0 / 5.0) + 32
    return fahr
def main(): 
    print("wasuh twin")
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (F or C): ").strip().upper()
    if unit == 'F':
        converted = fahrToCelsius(temp)
        print(f"{temp} F is {converted:.2f} C")
    elif unit == 'C':
        converted = celsiusToFahr(temp) 
        print(f"{temp} C is {converted:.2f} F")
    else:  
        print("Error, wrong unit gang")
main()