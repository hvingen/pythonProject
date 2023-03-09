# Stripes spaces around a text variable

first_name = "      albert      "
last_name = "einstein"

full_name = f"{first_name.lstrip()} {last_name}"
message = f'\n\t{full_name.title()} once said, "A person who never made a\n\tmistake never tried anything new."'
print(message)

full_name = f"{first_name.rstrip()} {last_name}"
message = f'\n\t{full_name.title()} once said, "A person who never made a' \
          f'\n\tmistake never tried anything new."'
print(message)

full_name = f"{first_name.strip()} {last_name}"
message = f"\n\t{full_name.title()} once said, \"A person who never made a" \
          f"\n\tmistake never tried anything new.\""
print(message)
