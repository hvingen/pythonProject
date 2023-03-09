# Presents a composed message as a quote with indent on two lines

first_name = "albert"
last_name = "einstein"
post_name = "genius"
full_name = f"{first_name} {last_name} {post_name}"

message = f'\n\t{full_name.title()} once said, "A person who never made a\n\tmistake never tried anything new."'
print(message)

message = f'\n\t{full_name.title()} once said, "A person who never made a' \
          f'\n\tmistake never tried anything new."'
print(message)

message = f"\n\t{full_name.title()} once said, \"A person who never made a" \
          f"\n\tmistake never tried anything new.\""
print(message)
