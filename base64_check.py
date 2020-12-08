# (V) Read the content of a binary file, e.g. cmd.exe
# (V) Write to file its base64 encoding
# (V) Read the base64 encoded file
# (V) View the content the encode file
# (V) Decode the file content to a new file
# (V) Run the decoded file and see if it works well

import base64

def main():
    binary_filepath = 'C:\\Windows\\System32\\cmd.exe'
    encoded_filepath = 'encoded.txt'
    decoded_filepath = 'decoded.exe'
    
    with open(binary_filepath, 'rb') as f:
        binary_content = f.read()
    
    with open(encoded_filepath, 'wb') as f:
        f.write(base64.b64encode(binary_content))

    with open(encoded_filepath, 'rb') as f:
        content = f.read()
        print(content[:25])
    
    with open(decoded_filepath, 'wb') as f:
        f.write(base64.b64decode(content))
    
if __name__ == "__main__":
    main()