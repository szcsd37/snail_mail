email = input("Your email address: ")


error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_no_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"

ok_message = "Valid email."

is_valid = True

number_of_at_characters = email.count("@")
if number_of_at_characters == 0:
    print(error_message_no_at)
    is_valid = False
elif number_of_at_characters > 1:
    print(error_message_too_many_at)
    is_valid = False

elif email.find('@') == 0:
    print(error_message_no_username)
    is_valid = False
elif email[0] == ".":
    print(error_message_invalid_username)
    is_valid = False

else:
    position_of_at = email.find("@")
    username = email[:position_of_at]
    domain = email[position_of_at + 1:]

    if not domain:
        print(error_message_no_domain)
        is_valid = False

    elif domain[0] == ".":
        print(error_message_no_server_name)
        is_valid = False

    elif "." not in domain:
        print(error_message_no_dot_in_domain)
        is_valid = False

    elif domain.endswith("."):
        print(error_message_no_tld)
        is_valid = False

    else:
        domain_parts = domain.split(".")
        if len(domain_parts[-1]) < 2:
            print(error_message_short_tld)
            is_valid = False

if "." not in email:
    print(error_message_no_dot)
    is_valid = False

if is_valid:
    print(ok_message)