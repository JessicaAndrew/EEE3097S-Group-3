import zipfile, os, time

# shuf -n5 /usr/share/dict/words > words.txt
file = "../Testing Data Sets/2018-09-19-03_57_11_VN100.csv"
archive = "zipfile_compressed_data.zip"
#password = b"verysecret"

start = time.time()

with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(file)

stop = time.time()
time = stop - start
print(time)

print(f"Uncompressed size: {os.stat(file).st_size}")
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(archive).st_size}")
# Compressed size: 1023

    # zf.setpassword(password)

"""
with zipfile.ZipFile(archive, "r") as zf:
    crc_test = zf.testzip()
    if crc_test is not None:
        print(f"Bad CRC or file headers: {crc_test}")

    info = zf.infolist()  # also zf.namelist()
    print(info)  # See all attributes at https://docs.python.org/3/library/zipfile.html#zipinfo-objects
    # [ <ZipInfo filename='words1.txt' filemode='-rw-r--r--' file_size=37>,
    #   <ZipInfo filename='words2.txt' filemode='-rw-r--r--' file_size=47>,
    #   ... ]

    file = info[0]
    with zf.open(file) as f:
        print(f.read().decode())
        # Olav
        # teakettles
        # ...

"""
