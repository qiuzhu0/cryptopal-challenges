string_hex = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key_hex = b"ICE"

def main():
    encrypted_bytes = bytes(
        b ^ key_hex[i % len(key_hex)]
        for i, b in enumerate(string_hex)
    )
    print(encrypted_bytes.hex())

if __name__ == "__main__":
    main()
