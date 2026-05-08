def replace_function(original_file, old_code, new_code):
    with open(original_file, "r") as f:
        content = f.read()

    updated = content.replace(old_code, new_code)

    with open(original_file, "w") as f:
        f.write(updated)