def print_header(text):
    print("\n" + "="*len(text))
    print(text)
    print("="*len(text))

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")
