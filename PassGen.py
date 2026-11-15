import gc
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


def pass_gen():
    """Generate and print a password, releasing temporary memory afterward."""
    if not CHARACTERS:
        raise ValueError("CHARACTERS must not be empty")
    if PASSWORD_LENGTH <= 0:
        raise ValueError("PASSWORD_LENGTH must be greater than zero")

    gc.collect()
    try:
        password = "".join(
            secrets.choice(CHARACTERS) for _ in range(PASSWORD_LENGTH)
        )
        print("Password =\n")
        print(password)
        print("\nIMPORTANT - This will be erased in 30 minutes.")
    finally:
        # Frees Python objects when possible; this is not secure memory wiping.
        gc.collect()


if __name__ == "__main__":
    pass_gen()
