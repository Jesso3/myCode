import hashlib

def validate_blockchain(blockchain):
    previous_hash = "0" * 64
    for block in blockchain:
        description, mined_number, prev_hash, record_hash = block.split("|")
        calculated_hash = hashlib.sha256((description + "|" + mined_number + "|" + previous_hash).encode()).hexdigest()
        if calculated_hash != record_hash:
            return False
        previous_hash = record_hash
    return True

blockchain = []
with open('spot the forgery input.txt', 'r') as file:
    for line in file:
        blockchain.append(line.strip())
is_valid = validate_blockchain(blockchain)
for x in blockchain
    if is_valid:
        print("Blockchain is valid!")
    else:
        print("Blockchain has been tampered with!")
