from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad

def decrypt_file(key):
    global content
    ciphertext = content

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # List of padding schemes to try
    padding_schemes = [pad.NoPadding]

    for padding_scheme in padding_schemes:
        try:
            # Perform decryption attempt with a padding scheme
            decrypted = cipher.decrypt(padding_scheme().unpad(ciphertext, AES.block_size))
            
            # Write the decrypted file
            with open('decrypted_file', 'wb') as file:
                file.write(decrypted)
            
            print(f"Decryption successful using {padding_scheme.__name__}. Decrypted content saved in 'decrypted_file'.")
            break  # Exit the loop on successful decryption

        except ValueError as e:
            print(f"Decryption failed using {padding_scheme.__name__}: {e}. Trying the next padding scheme.")

    else:
        print("Decryption failed with all padding schemes. Check padding or altered content.")

# Rest of your code remains the same...



# Function to remove both front and back preambles and sequence from file
def remove_preamble(file_path):
    global content
    detect_sequence = b'0011001100110011'
    preamble = bytes([0b10101010]) * 3000

    with open(file_path, 'rb') as file:
        content = file.read()

    start_index = content.find(detect_sequence)
    if start_index != -1:
        content = content[start_index + len(detect_sequence):]

    end_index = content.rfind(detect_sequence)
    if end_index != -1:
        content = content[:end_index]

    preamble_length = len(preamble)
    while True:
        start_index = content.find(preamble)
        if start_index == -1:
            break
        else:
            content = content[start_index + preamble_length:]

    while True:
        end_index = content.rfind(preamble)
        if end_index == -1:
            break
        else:
            content = content[:end_index]

#Key
predefined_key = b'Hello_IamMihiran'


# Remove both front and back preambles and sequence from the output.tmp file
remove_preamble('output.tmp')


decrypt_file(predefined_key)
