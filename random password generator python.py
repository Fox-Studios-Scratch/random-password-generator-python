import random

def generate_password(length=12, charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
  """Generates a random password of the specified length and character set.

  Args:
    length: The length of the password, in characters.
    charset: The character set to use for the password.

  Returns:
    A random password of the specified length and character set.
  """

  password = ""
  for i in range(length):
    password += random.choice(charset)

  return password


# Example usage:

password = generate_password()

print(password)
