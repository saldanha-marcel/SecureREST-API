def encode(message):
    encoded_message = ""
    for char in message:
        encoded_char = chr(ord(char) + 1)
        encoded_message += encoded_char
    return encoded_message


def decode(message):
    decoded_message = ""
    for char in message:
        encoded_char = chr(ord(char) - 1)
        decoded_message += encoded_char
    return decoded_message


def main():
    action = input()
    message = input()                 

    if action == 'c':
        encoded_message = encode(message)
        print("Encoded message:", encoded_message)
    elif action == 'd':
        decoded_message = decode(message)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid action.")  

if __name__ == "__main__":
    main()