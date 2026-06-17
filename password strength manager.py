password = input("Enter your password")
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()_+"for char in password)

score = sum([length_ok , has_upper , has_lower , has_digit , has_special])

print("length 8+:" , length_ok)
print("has uppercase:" , has_upper)
print("has lowecase:" , has_lower)
print("has digit:" , has_digit)
print("has special character:" , has_special)

if score == 5:
  print("Strength: STRONG")
elif score >= 3:
  print("Strength: MEDIUM")
else :
  print("Stength: WEAK")

