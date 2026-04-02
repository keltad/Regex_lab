import re

def find_digits(text: str) -> list[str]:
    pattern = r"\d+"
    result = re.findall(pattern, text)
    return result

def main():
    text = "У кімнаті 12 стільців, 3 столи і 25 книжок."
    print(find_digits(text))

if __name__ == "__main__":
    main()
