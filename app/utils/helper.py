def validate_file_type(filename: str, allowed_extensions: list):
    ext = filename.split(".")[-1]
    if ext not in allowed_extensions:
        raise ValueError(f"File type '{ext}' is not allowed.")
    return True
