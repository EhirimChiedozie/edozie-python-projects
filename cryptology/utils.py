def create_binary_blocks(text):
    text_list = [bin(ord(i)).replace('b', '') for i in text]
    text_to_base_two_list = []
    for i in text_list:
        if len(i) <= 7:
            i = '0' + i
        else:
            i = i
        text_to_base_two_list.append(i)
    text_to_base_two = ''.join(text_to_base_two_list)
    return text_to_base_two


def vigenere_encrypt(plaintext, key):
    #Convert the plaintext to binary
    plaintext_to_base_two = create_binary_blocks(plaintext)

    #Convert the key to binary
    key_to_base_two = create_binary_blocks(key)

    comb_base_two_key = key_to_base_two * (len(plaintext_to_base_two)//len(key_to_base_two)) + key_to_base_two[:len(plaintext_to_base_two)%len(key_to_base_two)]

    add_items = [(int(plaintext_to_base_two[i]) + int(comb_base_two_key[i]))%2 for i in range(len(plaintext_to_base_two))]
    ciphertext = [str(i) for i in add_items]
    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, key):
    key_to_base_two = create_binary_blocks(key)

    comb_base_two_key = key_to_base_two * (len(ciphertext)//len(key_to_base_two)) + key_to_base_two[:len(ciphertext)%len(key_to_base_two)]

    subtract_items = [(int(ciphertext[i]) - int(comb_base_two_key[i]))%2 for i in range(len(ciphertext))]
    plaintext_str = [str(i) for i in subtract_items]
    joint_plaintext = ''.join(plaintext_str)

    plaintext_binary = []

    for i in range(0, len(joint_plaintext), 8):
        plaintext_binary.append(joint_plaintext[i:i+8])

    plaintext_base_ten = [int(i, 2) for i in plaintext_binary]
    plaintext_list = [chr(i) for i in plaintext_base_ten]
    return ''.join(plaintext_list)


def convert_to_text(binary_number):
    plaintext_binary = []

    for i in range(0, len(binary_number), 8):
        plaintext_binary.append(binary_number[i:i+8])

    plaintext_base_ten = [int(i, 2) for i in plaintext_binary]
    plaintext_list = [chr(i) for i in plaintext_base_ten]
    return ''.join(plaintext_list)

print(convert_to_text('01110010011001010110000101100100'))