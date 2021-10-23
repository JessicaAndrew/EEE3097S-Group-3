import lzma, os, time
lzc = lzma.LZMACompressor()

filename_in = "../Sense-Hat-Data/2000.csv"
filename_out = "lzma_compressed_data.xz"

start = time.time()
with open(filename_in, mode="r") as fin, open(filename_out, "wb") as fout:
    for chunk in fin.read():
        compressed_chunk = lzc.compress(chunk.encode("ascii"))
        fout.write(compressed_chunk)
    fout.write(lzc.flush())
stop = time.time()
time = stop - start

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 972398
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 736
print(time)
