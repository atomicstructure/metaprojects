
# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        file.read()
except Exception as e:
        print(e, "The file could not be found")
    
