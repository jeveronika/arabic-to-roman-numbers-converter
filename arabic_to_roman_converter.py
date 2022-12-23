# convert numbers from arabic to roman

# we can get a number as an input from user
user_input = int(input("Enter a number you want to convert: "))

def convert_numbers(number):
    # set result as an empty string to get roman numbers from arabic numbers:
    result = ""
    # arabic and roman digits:
    roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # this loop runs every digit in user_input and assigns a arabic number:
    for x in range(len(roman)):
        while number >= arabic[x]:
            result += roman[x]
            number -= arabic[x]
    print(f"Arabic number {user_input} is '{result}' in arabic.")

#run the convert_numbers function:
convert_numbers(user_input)
