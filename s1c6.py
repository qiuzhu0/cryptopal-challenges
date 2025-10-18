from base64 import b64decode
from functools import reduce

def hamming_dist(bytes1, bytes2):
    return reduce(
        lambda acc, byte_pair :
            acc + bin(byte_pair[0] ^ byte_pair[1]).count('1'),
        zip(bytes1, bytes2),
        0
    )

def score_english(text):
    return sum(text.lower().count(c) for c in "etaoin")

def char_xor_shift(raw_bytes, i):
    return bytes(
        b ^ i for b in raw_bytes
    ).decode("ascii")

def char_xor_solve(encrypted_bytes):
    best_score = 0
    best_char = 0
    for i in range(256):
        try:
            score = score_english(
                char_xor_shift(encrypted_bytes, i)
            )
        except UnicodeDecodeError:
            continue
        if score > best_score:
            best_score = score
            best_char = i
    return best_char

def best_keysizes(encrypted_bytes):
    return sorted(
        [
            (s, hamming_dist(
                encrypted_bytes[:s],
                encrypted_bytes[s:2*s])/s)
            for s in range(2, 41)
        ],
        key = lambda pair : pair[1]
    )

def main():
    with open("s1c6.txt") as f:
        encrypted = b64decode(f.read())
    keysizes = best_keysizes(encrypted)
    keys = []
    # temporary: select specifically the correct keysize lmao
    for ksize, _ in keysizes[18:19]:
        blocks = [
            encrypted[i:i+ksize]
            for i in range(0,len(encrypted)-ksize,ksize)
        ]
        bytes_at_index = {i : [] for i in range(ksize)}
        for block in blocks:
            for i, byte in enumerate(block):
                bytes_at_index[i].append(byte)
        keys.append([
            char_xor_solve(bytes_at_index[i])
            for i in range(ksize)
        ])
    best_string = ""
    best_score = 0
    for key in keys:
        try:
            decrypted = bytes(
                b ^ key[i % len(key)]
                for i, b in enumerate(encrypted)
            ).decode("ascii")
        except UnicodeDecodeError:
            continue
        score = score_english(decrypted)
        if score > best_score:
            best_score = score
            best_string = decrypted
    print(best_string)

if __name__ == "__main__":
    main()
