hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def score_english(text):
    return sum(text.lower().count(c) for c in "etaoin")

def main():
    raw_bytes = bytes.fromhex(hex_string)
    best_score = 0
    best_string = ""
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
