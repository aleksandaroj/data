# class Validator:

def username_is_valid(self, username):
    if len(username) > 10:
        return False

    if " " in username:
        return False

    if username.islower():
        return False

    return True

# Validator.username_is_valid(Validator, "Ski")
# Validator.username_is_valid(Validator, "Sk i")
# Validator.username_is_valid(Validator, "ski")
# Validator.username_is_valid(Validator, "Ski45678901")
