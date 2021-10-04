import os, sys, shutil, gzip, time
# tests the gzip compression method

filename_in = "1.csv"
filename_out = "compressed_data2.gz"

start = time.time()
with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
    # Reads the file by chunks to avoid exhausting memory
    shutil.copyfileobj(fin, fout)

stop = time.time()
time = stop -start

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 1023
print("Exectuion time in seconds: ", time)
