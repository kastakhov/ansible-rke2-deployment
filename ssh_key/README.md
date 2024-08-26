# Private Key

add your PRIVATE ssh key to this folder locally on your computer.

Files [ignored from git](../.gitignore) commit:

- *.private
- id_ed25519
- id_ed25519.*
- id_rsa.*
- id_rsa
- ssh_host_ecdsa_key
- ssh_host_ed25519_key
- ssh_host_rsa_key

## Do Not commit your private key

Make sure to **not commit your private key** in case if it is named differently and not ignored by git!
For example file with name `mysuperprivate.key` will not be ignored by git commit! 
