# Validate magical spell
spell = "Expelliarmus"

if spell.isalpha():
    print("Spell accepted!")

# Password check (palindrome)
password = "level"

if password == password[::-1]:
    print("Scroll unlocked!")

# Student names
names = ["Harry", "Ron", "Hermione"]

# Display initials
initials = [name[0] for name in names]
print("Initials:", initials)

# Conceal names with asterisks
concealed = ["*" * len(name) for name in names]
print("Concealed:", concealed)