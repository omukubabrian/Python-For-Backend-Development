"""PIN hashing and verification"""
import hashlib
import hmac
import secrets

ITERATIONS=200_000

def hash_pin(pin:str,salt:bytes|None=None)->tuple[str,str]:
    """Return(salt_hex,hash_hex).Generates a new salt if none is given."""
    salt=salt or secrets.token_bytes(16)
    digest=hashlib.pbkdf2_hmac("sha256",pin.encode(),salt,ITERATIONS)
    return salt.hex(),digest.hex()



def verify_pin(pin:str,salt_hex:str,hash_hex:str)->bool:
    _,candidate=hash_pin(pin,bytes.fromhex(salt_hex))
    return hmac.compare_digest(candidate,hash_hex)