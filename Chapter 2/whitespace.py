# Chapter 2 page 22 - Whitespace

# add a tab to a string
print("Python")
print("\tPython")

# adding a newline and a tab
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Striping whitespace, this doesn't show up in the console well, the semi colon should move over one place.
favorite_language = ' python '
print(favorite_language, ';')
print(favorite_language.rstrip(), ';')
print(favorite_language.lstrip())
print(favorite_language.strip())

url = "https://www.google.com"
print(url.removeprefix("https://"))