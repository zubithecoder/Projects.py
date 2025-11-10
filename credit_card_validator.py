# Making a credit card validator using Only Python
# 1. Remove any spaces or dashes from the input ("-" or " ")
# 2. Add all digits in the odd places from the right to left 
# 3. Double every second digit from right to left. 
# (If result is a two-digit number, add the two-digit number together to get a single digit) 
# 4. Sum all the digits from step 2 and step 3
# 5. If sum is divisible by 10, the credit card number is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1:
card_number = input("Enter your credit card number: ")
card_number = card_number.replace(" ", "").replace("-", "")
card_number = card_number[::-1]  # Reverse the card number for easier processing

# Step 2:
for x in card_number[::2]:  # Odd places from right to left
    sum_odd_digits += int(x)

# Step 3:
for x in card_number[1::2]:  # Even places from right to left
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))  # Add the digits of the two-digit number
    else:
        sum_odd_digits += x

# Step 4:
total = sum_odd_digits + sum_even_digits

# Step 5:
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
    
