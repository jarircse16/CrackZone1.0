# CrackZone1.0
# It is a python written bruteforce based command line tool to crack MD5 Hashes.
# Useage:
CrackZone1.0.py [-h] [--dictionary-file DICTIONARY_FILE] [--hash-file HASH_FILE] [--single-hash SINGLE_HASH]
                       [--dictionary-directory DICTIONARY_DIRECTORY]

MD5 Hash Cracker

options:
  -h, --help            show this help message and exit
  --dictionary-file DICTIONARY_FILE
                        File containing potential passwords (one per line)
  --hash-file HASH_FILE
                        File containing MD5 hashes to crack (one per line)
  --single-hash SINGLE_HASH
                        Single MD5 hash to crack
  --dictionary-directory DICTIONARY_DIRECTORY
                        Directory containing multiple dictionary files
