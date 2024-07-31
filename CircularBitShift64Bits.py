def circular_shift_64bits(bits, shift):
    shift %= 64
    return (bits >> shift) | (bits << (64 - shift)) & 0xFFFFFFFFFFFFFFFF

def decode_binary_string(binary_string, shift):
    # Remove any spaces from the binary string
    binary_string = binary_string.replace(' ', '')
    
    # Ensure the binary string length is a multiple of 64
    if len(binary_string) % 64 != 0:
        raise ValueError("The length of the binary string is not a multiple of 64.")
    
    # Split the binary string into 64-bit blocks
    blocks = [binary_string[i:i+64] for i in range(0, len(binary_string), 64)]
    
    decoded_message = ""

    for block in blocks:
        # Convert the binary string to an integer
        block_int = int(block, 2)
        
        # Apply the circular shift
        shifted_block_int = circular_shift_64bits(block_int, shift)
        
        # Convert the shifted integer back to a binary string
        shifted_block = format(shifted_block_int, '064b')
        
        # Convert the shifted binary string to bytes
        for i in range(0, len(shifted_block), 8):
            byte = shifted_block[i:i+8]
            decoded_message += chr(int(byte, 2))
    
    return decoded_message

file_path = "Path_Here"

with open(file_path, "r") as file:
    binary_data = file.read().replace('\n', '')

# Change it as you need it
shift = 3

decoded_message = decode_binary_string(binary_data, shift)
print("Message décodé :")
print(decoded_message)
