def find_and_calculate_average(file_name):
    try:
        total, count = 0.0, 0

        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2 and parts[1].replace(".", "", 1).isdigit():
                    total += float(parts[1])
                    count += 1

        if count > 0:
            average = total / count
            print(f"Sum of the numbers: {total}")
            print(f"Average value: {average}")
        else:
            print("No valid lines found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
