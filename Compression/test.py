import zlib
import binascii

data = 'Hello world'
data = bytes(data, 'utf-8')
compressed_data = zlib.compress(data, 2)

print('Original data: '+ data.decode('utf-8'))
print('Compressed data: '+ binascii.hexlify(compressed_data).decode('utf-8'))
