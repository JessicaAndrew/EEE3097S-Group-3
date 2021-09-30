import gzip
import zlib

data = 'Hello world'
print("Original Data: ", data)

compressed_data = zlib.compress(data, 2)
print("Compressed Data: ", compressed_data)
#compressed_data = open('compressed.dat', 'rb').read()

decompressed_data = zlib.decompress(compressed_data)
print("Decompressed Data: ", decompressed_data)

#print("Hello")
#res = bytes(test_string, 'utf-8')
