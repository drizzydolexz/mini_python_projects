# Password Manager

A basic password manager using Python and cryptography. This program allows you to securely store and view passwords.

## Features

- **Encryption:** Uses the Fernet encryption library to secure passwords.
- **Master Password:** You can set a master password to encrypt and decrypt your password data.
- **Random Password Generation:** Option to generate a random password for your accounts.
- **View Passwords:** View stored passwords in a decrypted format.
- **Add Passwords:** Add new passwords securely to the manager.

## How to Use

1. **Setup:**
   - Run the program and follow the prompts to set up your master password and encryption key.
   - If it's your first time running the program, a new encryption key will be generated.

2. **Options:**
   - Enter `1` to view passwords.
   - Enter `2` to add a new password.
   - Enter `3` to quit.

3. **View Passwords:**
   - Your stored usernames and passwords will be displayed in a decrypted format.

4. **Add Passwords:**
   - Enter the username for the account.
   - Choose to generate a random password or enter your own.
   - If you choose to generate a random password, it will be displayed for you.
   - The password will be encrypted and stored securely.

5. **Quit:**
   - Enter `3` or `quit` to exit the program.

## Requirements

- Python 3.x
- cryptography library (install using `pip install cryptography`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
