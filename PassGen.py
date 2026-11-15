import gc
import os
import secrets

# Printable letters, digits, and common symbols. Keep this as a string so
# password generation doesn't need a temporary list of characters.
CHARACTERS = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*()-_=+[]{};:,.?/"
)

PASSWORD_LENGTH = 10
OUTPUT_FILE = "/opt/PassGen/src/Password.txt"
NOTICE = "IMPORTANT - This will be erased in 30 minutes."


def pass_gen():
    """Generate and save a password, releasing temporary memory afterward."""
    if not CHARACTERS:
        raise ValueError("CHARACTERS must not be empty")
    if PASSWORD_LENGTH <= 0:
        raise ValueError("PASSWORD_LENGTH must be greater than zero")

    gc.collect()
    try:
        password = "".join(
            secrets.choice(CHARACTERS) for _ in range(PASSWORD_LENGTH)
        )

        # The context manager ensures the file is closed even if writing fails.
        with open(OUTPUT_FILE, "w") as textfile:
            textfile.write("Password =  \n\n")
            textfile.write(password)
            textfile.write("\n\n")
            textfile.write(NOTICE)
            textfile.write("\n")
            textfile.flush()

        # Some MicroPython ports provide os.sync(); use it when available.
        sync = getattr(os, "sync", None)
        if sync is not None:
            sync()
    finally:
        # Frees Python objects when possible; this is not secure memory wiping.
        gc.collect()


if __name__ == "__main__":
    pass_gen()
