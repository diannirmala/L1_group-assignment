# 2-1 simple message 
msg = "I love learning to use Python."
print(f"2-1 {msg}")

# 2-2 simple messages 
msg = "I love learning to use Python."
print(f"2-2 {msg}")

msg = "It's really satisfying!"
print(f"2-2 {msg}")

# 2-3 personal message
name = "eric"
msg = f"Hello {name.title()}, would you like to learn some Python today?"

print(f"2-3 {msg}")

# 2-4 name cases
name = "eric"

print(f"2-4 {name.lower()}")
print(f"2-4 {name.upper()}")
print(f"2-4 {name.title()}")

# 2-5 famous quote
print(f'2-5 Albert Einstein once said, "A person who never made a mistake')
print(f'never tried anything new."')

# 2-5 famous quote 2
famous_person = "Albert Einstein"

message = f'2-6 {famous_person} once said, "A person who never made a mistake never tried anything new."'

print(message)

# 2-7 stripping names
name = "\tEric Matthes\n"

print("2-7 Unmodified:")
print(name)

print("\n2-7 Using lstrip():")
print(name.lstrip())

print("\n2-7 Using rstrip():")
print(name.rstrip())

print("\n2-7 Using strip():")
print(name.strip())

# 2-8 file extensions
filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(f"2-8 {simple_filename}")

# 2-9 favorite number
fav_num = 42
msg = f"My favorite number is {fav_num}."

print(f"2-9 {msg}")