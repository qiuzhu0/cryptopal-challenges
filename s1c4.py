def score_english(text):
    return sum(text.lower().count(c) for c in "etaoin")

def main():
    with open("s1c4.txt") as f:
        hex_strings = f.read().split('\n')
    best_score = 0
    best_string = ""
    for hex_string in hex_strings:
        raw_bytes = bytes.fromhex(hex_string)
        for i in range(256):
            try:
                xor_string = bytes(
                    b ^ i for b in raw_bytes
                ).decode("ascii")
            except UnicodeDecodeError:
                continue
            score = score_english(xor_string)
            if score > best_score:
                best_score = score
                best_string = xor_string
    print(best_string)

if __name__ == "__main__":
    main()
