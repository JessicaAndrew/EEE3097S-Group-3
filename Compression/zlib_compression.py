import zlib, sys, time

filename_in = "../Sense-Hat-Data/2000.csv"
filename_out = "zlib_compressed_data"

start = time.time()
with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    stop = time.time()
    print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 1000033
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 1024
    print("Compression time: ", stop-start)
    fout.write(compressed_data)


