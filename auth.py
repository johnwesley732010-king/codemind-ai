import hashlib
ADMIN_PASSWORD_HASH = hashlib.sha256("JOHNCLARA".encode()).hexdigest()
def verify_admin(p):
    return hashlib.sha256(p.encode()).hexdigest()==ADMIN_PASSWORD_HASH
