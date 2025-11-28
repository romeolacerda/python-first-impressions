
credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4]) #first four
print(credit_number[5:9]) # from 5th to 9th
print(credit_number[5:]) # from 5th
print(credit_number[-1]) # last one
print(credit_number[::3]) # by 3

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse_number = credit_number[::-1]
print(credit_number)