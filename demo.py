from .Parser.parser import parse
if __name__ == '__main__':
    print("--- Narsese parser ---")
    while True:
        text = input("Input: ")
        task = parse(text)
        print(task)