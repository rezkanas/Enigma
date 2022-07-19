from cryptography.fernet import Fernet


class additional_encrypt_layer:
    def generate_key(self):
        """
        Generates a key and save it into a file and close the stream
        """
        self.key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)
        return

    @staticmethod
    def load_key():
        """
        Loads the key named `secret.key` from the current directory.
        """
        return open("secret.key", "rb").read()

    def encrypt_message(self, char):
        self.generate_key()
        key = self.load_key()
        # since data must be bytes  before feeding it to Fernet, we use
        # .encode() transferring it to utf-8
        encoded_message = char.encode()
        # instantiate an Fernet object
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)

        return encrypted_message.decode()

    def decrypt_message(self, encrypted_message):
        key = self.load_key()
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        decoded_message = decrypted_message.decode()
        return decoded_message


if __name__ == "__main__":
    layer = additional_encrypt_layer()
    message_to_be_coded = "Yes, we can"
    encrypted = layer.encrypt_message(message_to_be_coded)
    print("\033[1m" + f"Encrypted message of (  {message_to_be_coded}  ) is:\n" + ", \
     ""\033[0m", encrypted, '\n\n\n')
    decode = layer.decrypt_message(encrypted.encode())
    print("\033[1m" + f"Decrypted message of (  {encrypted}  ) is:\n" + "\033[0m", decode)
