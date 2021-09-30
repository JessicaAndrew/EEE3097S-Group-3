import zlib
import binascii

original_data = open('Dummy.txt', 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
decompressed_data = zlib.decompress(compressed_data)

compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

#print('Compressed: %d%%' % (100.0 * compress_ratio))
#print('Original: '+ original_data.decode('utf-8'))
print(binascii.hexlify(compressed_data).decode('utf-8'))
#print('Decompressed data: ' + decompressed_data.decode('utf-8'))
