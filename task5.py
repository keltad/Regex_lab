import re

def replace_places(text: str) -> str:
    pattern = r"\s+"
    result = re.sub(pattern, '_', text)
    return result 

def main():
    text = "Python   regex   це	цікаво"
    print(replace_places(text))

if __name__ == "__main__":
    main()