import base64
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def main():
    private_key1_path, public_key1_path = 'private1.pem', 'public1.pem'
    private_key2_path, public_key2_path = 'private2.pem', 'public2.pem'
    signature_path = 'signature.txt'
    generate_keys(private_key1_path, public_key1_path)
    generate_keys(private_key2_path, public_key2_path)
    content = read_file_content('text.txt')
    print(f'signing message: {content[:10]}...')
    sign_content(content, private_key1_path, signature_path)

    # this should print that the signature is valid, since we are using the corrent public key
    if verify_content_signature(content, public_key1_path, signature_path):
        print("The signature is valid.")
    else:
        print("The signature is not valid.")

    # this should print that the signature is NOT valid, since we are using the wrong public key
    if verify_content_signature(content, public_key2_path, signature_path):
        print("The signature is valid.")
    else:
        print("The signature is NOT valid.")


def generate_keys(private_key_path, public_key_path):
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open(private_key_path, "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open(public_key_path, "wb")
    file_out.write(public_key)
    file_out.close()

def read_file_content(filepath, b64=False):
    with open(filepath, 'rb') as f:
        content = f.read()
    if b64:
        content = base64.b64decode(content)
    return content

def write_file_content(filepath, content, b64=False):
    with open(filepath, 'wb') as f:
        if b64:
            f.write(base64.b64encode(content))
        else:
            f.write(content)

def get_content_sha256_hash(content):
    hash = SHA256.new(data=content)
    return hash

def verify_content_signature(content, public_key_path, signature_path):
    is_valid = None
    public_key = RSA.import_key(open(public_key_path).read())
    h = SHA256.new(content)
    try:
        signature = read_file_content(signature_path)
        pkcs1_15.new(public_key).verify(h, signature)
        is_valid = True
    except (ValueError, TypeError):
        is_valid = False
    return is_valid

def sign_content(content, private_key_path, signature_filepath):
    private_key = RSA.import_key(open(private_key_path).read())
    sha256 = get_content_sha256_hash(content)
    signature = pkcs1_15.new(private_key).sign(sha256)
    write_file_content(signature_filepath, signature)

if __name__ == "__main__":
    main()
