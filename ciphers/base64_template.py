import base64

def base64_tool(text, mode="encode"):
    if mode == "encode":
        binary_text = text.encode("utf-8")
        base64_data = base64.b64encode(binary_text)
        return base64_data.decode("utf-8")
    
    elif mode == "decode":
        base64_bytes = text.encode("utf-8")
        decoded_data = base64.b64decode(base64_bytes)
        return decoded_data.decode("utf-8")

    else:
        return "Invalid mode. Use 'encode' or 'decode'."
