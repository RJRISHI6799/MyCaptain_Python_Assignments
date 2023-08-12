filename = input("Input the Filename: ")
if '.' in filename:
    extension = filename.split('.')[-1]
    print(f"The extension of the file is: '{extension}'")
else:
    print("Invalid filename. No extension found.")
