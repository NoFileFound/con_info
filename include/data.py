from include import aes, binary
from os import urandom

class EncryptInformation:
    def __init__(self):
        self.key = urandom(32)
        self._bin = binary.BinaryFile()
        self._aes = None
        
    def Encrypt(self, info) -> None:
        self._aes = aes.AESCipher(self.key)
    
        encryped_bytes = self._aes.AES_Encrypt(info)
        self._bin.SaveBinary(self.key, encryped_bytes)
        
    def Decrypt(self) -> str:
        info = self._bin.ReadBinary()
        self.key = info[0]
        encryped_bytes = info[1]
        self._aes = aes.AESCipher(self.key)
        
        decrypted_data = self._aes.AES_Decrypt(encryped_bytes)
        return decrypted_data.decode('utf-8')