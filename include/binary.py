"""
Simple implementation of binary file I/O.
"""

class BinaryFile:
    def __init__(self):
        self.fileName = "convention.bin"
        self.header = bytes.fromhex("2e434f4e5f494e464f000000000000000000000000000000000000000000")
         # .CON_INFO

    def SaveBinary(self, key : bytes, data : bytes):
        empty_bytes = bytes.fromhex("00000000000000000000000000000000")
        header = self.header + b'\x00\x00' + empty_bytes + key + empty_bytes
        
        with open(self.fileName, 'wb') as file:
            file.write(header + data)
        
    def ReadBinary(self) -> tuple:
        with open(self.fileName, 'rb') as file:
            file.seek(16 * 3)
            key = file.read(16 * 2)
            file.seek(16 * 6)
            data = file.read()
            
        return [key, data]