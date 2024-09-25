import hashlib

def quantum_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_hash(data, hash_value):
    return quantum_hash(data) == hash_value
