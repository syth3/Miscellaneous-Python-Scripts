def string_to_hex(s):
    """Converts ASCII string to hexadecimal string.
        Example: "Hello, world!" should return "48656c6c6f2c20776f726c6421"
    Args:
        s (string): Given ASCII string.
    Returns:
        string: Equivalent hexadecimal string.
    """
    encoded_string = s.encode('ascii')
    hex_string = encoded_string.hex()
    return hex_string


def hex_to_string(h):
    """Converts hexadecimal string to ASCII string.
        Example: "48656c6c6f2c20776f726c6421" should return  "Hello, world!"
    Args:
        h (string): Given hexadecimal string.
    Returns:
        string: Equivalent ASCII string.
    """
    byte_array = bytearray.fromhex(h)
    string = byte_array.decode('ascii')
    return string


def hex_to_bytes(h):
    """Converts hexadecimal string to list of ASCII byte values in range of 0-255.
        Example: "48656c6c6f2c20776f726c6421" should return [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
    Args:
        h (string): Given hexadecimal string.
    Returns:
        list: Equivalent list of integer bytes.
    """
    byte_array = bytearray.fromhex(h)
    bytes_in_decimal = []
    for byte in byte_array:
        bytes_in_decimal.append(byte)
    return bytes_in_decimal


def bytes_to_hex(b):
    """Converts list of ASCII byte values in range of 0-255 to hexadecimal string.
        Example: [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33] should return "48656c6c6f2c20776f726c6421"
    Args:
        b (byte list): Given list of integer bytes.
    Returns:
        string: Equivalent hexadecimal string.
    """
    byte_array = bytearray()
    for byte in b:
        byte_array.append(byte)
    hex_string = byte_array.hex()
    return hex_string


def string_to_bytes(s):
    """Converts ASCII string to list of ASCII byte values in range of 0-255.
        Example: "Hello, world!" should return [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
    Args:
        s (string): Given ASCII string.
    Returns:
        list: Equivalent list of integer bytes.
    """
    encoded_string = s.encode('ascii')
    byte_list = []
    for byte in encoded_string:
        byte_list.append(byte)
    return byte_list


def bytes_to_string(b):
    """Converts list of ASCII byte values in range of 0-255 to ASCII string.
        Example: [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33] should return "Hello, world!"
    Args:
        b (byte list): Given list of integer bytes.
    Returns:
        string: Equivalent ASCII string.
    """
    byte_array = bytearray()
    for byte in b:
        byte_array.append(byte)
    string = byte_array.decode('ascii')
    return string
