import re 

def extract_words_starting_with_a(text: str) -> list[str]:
    pattern = r"\b[aA]\w*+"
    result = re.findall(pattern, text)
    return result

def main():
    text = "Apple and apricot are amazing, but banana is also good."
    print(extract_words_starting_with_a(text))

if __name__ == "__main__":
    main()