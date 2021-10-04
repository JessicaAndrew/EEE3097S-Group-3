import zlib, sys

filename_in = "9.csv"
filename_out = "compressed_data"

with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 1000033
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 1024

    fout.write(compressed_data)

with open(filename_out, mode="rb") as fin:
    data = fin.read()
    compressed_data = zlib.decompress(data)
    print(f"Compressed size: {sys.getsizeof(data)}")
    # Compressed size: 1024
    print(f"Decompressed size: {sys.getsizeof(compressed_data)}")
    # Decompressed size: 1000033
