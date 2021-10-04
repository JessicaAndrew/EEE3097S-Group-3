import lzma, os, time
lzc = lzma.LZMACompressor()

# cat /usr/share/dict/words | sort -R | head -c 1MB > data
filename_in = "9.csv"
filename_out = "compressed_data4.xz"

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
