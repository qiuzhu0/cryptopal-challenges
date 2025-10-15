hex_string = "1c0111001f010100061a024b53535009181c"
xor_against = "686974207468652062756c6c277320657965"

def main():
    print(
        bytes(a ^ b for a,b in zip(
            bytes.fromhex(hex_string),
            bytes.fromhex(xor_against)))
        .hex()
    )

if __name__ == "__main__":
    main()
