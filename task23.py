import re

def find_shorts_words (text: str, n: int) -> list[str]:
    pattern = fr'\w{{{n}}}'
    result = re.findall(pattern, text)
    return result

def main():
    text = "кіт пес лис вовк сова"
    n = 3
    print(find_shorts_words(text, n))

if __name__ == "__main__":
    main()