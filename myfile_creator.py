import sys

def ask_user_input(prompt: str) -> str:
    """Prompts the user for input and returns the response as long as its not an empty response. will keep asking for valid input"""
    while True:
        response = input(prompt + "\n").strip()
        if response:
            return response
        print("Input cannot be blank! Please try again")

def save_user_input(file_path: str, name: str, color: str) -> None:

    """Writes collected input to file, with error handling"""
    try:
        with open(file_path, "w") as file:
            file.write(f"{name} created this file.\n")
            file.write(f"Their favorite color is {color}.\n")
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


def main():
    name = ask_user_input("What's your name?")
    color = ask_user_input("What's your favorite color?")
    save_user_input("myexample.txt", name, color)
    print("Input saved to file!")

if __name__ =="__main__":
    main()