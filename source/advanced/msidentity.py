import hashlib
import codecs
from  base64 import b64decode

def check_password (password:str, identity_record:str) -> bool:
    
    password_bytes = bytes(password, "utf-8")
    
    #ASP.NET Identity Version 2: PBKDF2 with HMAC-SHA1, 128-bit salt, 256-bit subkey, 1,000 iterations##
    #ASP.NET Core Identity Version 3: PBKDF2 with HMAC-SHA256, 128-bit salt, 256-bit subkey, 10,000 iterations
    #https://www.strathweb.com/2023/03/beware-of-the-default-aspnet-identity-settings/
    #sha512
    #https://stackoverflow.com/questions/76498759/what-python-code-was-used-to-generate-this-pbkdf2-sha512-password-entry
    
    #pw_as_bytes = b64decode(password)
    identity_decoded = b64decode(identity_record)
    
    # Itentity version 0 or 1 Expected 1
    p1_1 = identity_decoded[0:1]
    identity_version = int.from_bytes(p1_1, "little")
    
    # Hash algorithm version, expected 1 (0=SHA1, 1=SHA256, 2=SHA512 )
    p2_5 = identity_decoded[1:5]
    hash_algorithm_version = int.from_bytes(p2_5, "big")
    hashalgorithm_name = getHashAlgorithmAsString(hash_algorithm_version)
    
    # Number of iterations    
    p6_9 = identity_decoded[5:9]
    iterations = int.from_bytes(p6_9, "big")
    
    # Length of salt string (Expected 16)
    p10_13 = identity_decoded[9:13]
    saltsize = int.from_bytes(p10_13, "big")

    # Actual salt string (16 characters)
    p14_29 = identity_decoded[13:29]
    
    # The result we should have...
    p30_61 = identity_decoded[29:61]
        
    salt_bytes = p14_29          
    subkeySize = 32    
    
    if hashalgorithm_name == 'PBKDF2WithHmacSHA256':
        actualSubkey = hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, iterations, subkeySize)
    else:
        return False

    ch_org:str = codecs.getencoder('hex_codec')(p30_61)[0] 
    ch_new:str = codecs.getencoder('hex_codec')(actualSubkey)[0] 
    
    return ch_org == ch_new
 
def getHashAlgorithmAsString (i:int) -> str:

    if i == 0:
        return "SHA1"
    elif i == 1:
        return "PBKDF2WithHmacSHA256"
    elif i == 2:
        return "SHA512"

    return ""
    

password = "Test123!"
identity_field = 'AQAAAAEAACcQAAAAEFF6kaUfVFtKu8JuTDq5PuuBXLGFIdrLCqUGivmyNiyQfn3WGCWBcr9wtSwJ9A1E7A=='

if check_password(password, identity_field):
     print("Password is OK")
else:
     print("Shit, wrong password!")
