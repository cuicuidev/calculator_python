from core import calculator

def main() -> None:
    while True:
        opt = input("Select an option:\n1 - Calculator\n0 - Quit\n")
        if opt == "1":
            input_str = input("Enter your mathematical expression:\n\n")
            try:
                print("\nResult:", calculator(input_string=input_str), "\n")
            except Exception as err:
                print(f"{type(err)}: {err}")
            continue
        if opt == "0":
            break
        
        print("\nWrong option!!!\n")

if __name__ == "__main__":
    main()