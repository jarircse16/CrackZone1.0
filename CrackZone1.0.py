import hashlib
import argparse
import os

def crack_md5_hash(hash_to_crack, dictionary):
    # Load a list of potential passwords from the specified dictionary file
    with open(dictionary, 'r') as file:
        potential_passwords = [line.strip() for line in file]

    # Iterate through potential passwords and hash them to compare with the target hash
    for password in potential_passwords:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == hash_to_crack:
            return password

    return None

def main():
    parser = argparse.ArgumentParser(description='MD5 Hash Cracker')
    parser.add_argument('--dictionary-file', help='File containing potential passwords (one per line)')
    parser.add_argument('--hash-file', help='File containing MD5 hashes to crack (one per line)')
    parser.add_argument('--single-hash', help='Single MD5 hash to crack')
    parser.add_argument('--dictionary-directory', help='Directory containing multiple dictionary files')
    args = parser.parse_args()

    if args.dictionary_file and args.single_hash:
        password = crack_md5_hash(args.single_hash, args.dictionary_file)
        if password:
            print(f'Cracked hash: {args.single_hash} -> Password: {password}')
        else:
            print(f'Failed to crack hash: {args.single_hash}')

    elif args.dictionary_file and args.hash_file:
        with open(args.hash_file, 'r') as file:
            hashes = [line.strip() for line in file]

        for hash_to_crack in hashes:
            password = crack_md5_hash(hash_to_crack, args.dictionary_file)
            if password:
                print(f'Cracked hash: {hash_to_crack} -> Password: {password}')
            else:
                print(f'Failed to crack hash: {hash_to_crack}')

    elif args.dictionary_directory:
        dictionary_files = [f for f in os.listdir(args.dictionary_directory) if f.endswith('.txt')]
        
        for dictionary_file in dictionary_files:
            with open(os.path.join(args.dictionary_directory, dictionary_file), 'r') as file:
                dictionary = os.path.join(args.dictionary_directory, dictionary_file)
                with open(args.hash_file, 'r') as hashfile:
                    hashes = [line.strip() for line in hashfile]
                
                for hash_to_crack in hashes:
                    password = crack_md5_hash(hash_to_crack, dictionary)
                    if password:
                        print(f'Cracked hash: {hash_to_crack} -> Password: {password}')
                    else:
                        print(f'Failed to crack hash: {hash_to_crack}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
