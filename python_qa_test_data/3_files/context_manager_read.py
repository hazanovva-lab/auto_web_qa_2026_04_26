from files import TXT_FILE_PATH

with open(TXT_FILE_PATH, "r") as file:
    print(file.read())

print("\n", 20 * "=", "\n")