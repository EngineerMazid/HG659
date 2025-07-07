# HG659 Ooredoo Config Decryptor

This is a simple Python script that decrypts and decompresses config backups from Huawei HG659 routers branded by Ooredoo. It turns the `.conf` file into a readable XML so you can inspect the settings.

---

## How it works

1. Takes the encrypted file (`downloadconfigfile.conf`)
2. Uses AES (CBC) with a hardcoded key and IV to decrypt
3. Then decompresses the data using zlib
4. Removes some garbage from the end (129 bytes)
5. Saves the output as `output.xml`

---

## Requirements

- Python3
- `pycryptodome` library

Install it with:

```bash
pip install pycryptodome
```
 ## How to Use
1. Put your encrypted config file in the same folder and name it:
`downloadconfigfile.conf`
2. Run the script:
`python3 decrypt.py`
3. If successful, it will generate:
`output.xml`
You can open that in any text editor or XML viewer.
