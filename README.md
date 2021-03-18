# password_hashing

Project allows to store and verify passwords in an SQLite database.

# Description
password_hashing is an console app storing passwords (hashes and their salts) in an SQLite database. Each user has an ID (Primary Key), password's hash and unique salt.

# Hashing functions 
Password hashes for new users are being generated using SHA256 hashing algorithm, either by manually implemented SHA256 algorithm or by pbkdf2_hmac from the hashlib library.
Password salts are of length 5, generated randomly. 

# Author
Jan Gregor

# License
Distributed under no License.

