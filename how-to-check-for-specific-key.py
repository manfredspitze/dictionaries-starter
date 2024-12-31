# Checking for a specific key in a dictionary
# Technique 1
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages:
    if name == 'eric':  # Replace 'eric' with the specific name you want to check
        print(f"{name}'s favorite language is {favorite_languages[name]}")
    else:
        print(f"{name} is not the name you're looking for.")


# Checking for a specific key in a dictionary using the get ( ) method
# Technique 2
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

desired_key = 'eric'  # Replace with the specific name you want to check for

language = favorite_languages.get(desired_key)

if language:
    print(f"{desired_key}'s favorite language is {language}")
else:
    print(f"{desired_key} is not in the dictionary.")
