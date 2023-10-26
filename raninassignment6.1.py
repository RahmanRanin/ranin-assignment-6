def convert_to_uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            line_number = 1
            for line in file:
                print(f'LINE NUMBER : {line_number}')
                print(line.upper(), end='')
                line_number += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    file_name = input("Enter a file name: ")
    convert_to_uppercase(file_name)
