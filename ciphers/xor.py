def encrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

def decrypt(text):
    results = []
    try:
        for key in range(256):
            possible = ""
            for char in text:
                decry = chr(ord(char) ^ key)
                possible += decry
            results.append(f"Key: {key} ==> {possible}")
        return results
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

