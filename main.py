def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
        'CD': 400, 'CM': 900
    }
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num

def main():
    while True:
        choice = input("Would you like to convert a number to Roman numerals or a Roman numeral to a number? (Enter 'number' or 'roman', or 'exit' to quit): ").strip().lower()
        
        if choice == 'number':
            num = int(input("Enter a number to convert to Roman numerals: "))
            if num < 1 or num > 3999:
                print("Please enter a number between 1 and 3999.")
            else:
                print(f"The Roman numeral for {num} is {int_to_roman(num)}")
                
        elif choice == 'roman':
            roman_numeral = input("Enter a Roman numeral to convert to a number: ").strip().upper()
            print(f"The number for the Roman numeral {roman_numeral} is {roman_to_int(roman_numeral)}")
            
        elif choice == 'exit':
            print("Exiting the converter.")
            break
            
        else:
            print("Invalid choice, please enter 'number', 'roman', or 'exit'.")

if __name__ == "__main__":
    main()
