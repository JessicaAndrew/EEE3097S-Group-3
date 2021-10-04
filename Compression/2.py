import bz2, os, sys, time
# bz2 data compression method

filename_in = "9.csv"
filename_out = "compressed_data.bz2"

start = time.time()
with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
    fout.write(fin.read())
stop = time.time()

time = stop - start
print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 48
print("Time:",time)
