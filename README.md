# EEE3097S-Group-3
This GitHub page is used to share files that are used in the EEE3097S design project. It mainly focuses on the zlib compression algorithm as well as the AES encryption algorithm.

The different encryption algorithms used are within the Encryption folder. The different compression algorithms used are within the Compression folder.

Note that the files used in the first stage of testing are in the 'Old data' folder in the 'Testing Data Sets' folder. The files used in the second stage of testing are in the 'Sense HAT B data' folder in the 'Testing Data Sets' folder. The files used in stage 2 of the project are from data from the Sense HAT pushed to csv files. These files can be seen are named as "Number of readings taken".csv.

The folder called Combined has three python files in it. CompressEncrypt.py compresses and encrypts the inputted file. DecryptDecompress.py decrypts then decompresses the file. TestLostData.py is used to first shallow and then deep check if the original file and the final decompressed file match.

To run the files in the Combined folder once the data files to deal with have been outputted, first use the command line code to call the CompressEncrypt.py code: python3 CompressEncrypt.py fileName.csv password (for example python3 CompressEncrypt.py 1400.csv thisIsMyPassword). Then run the DecryptDecompress.py code by running the command line code: python3 DecryptDecompress.py fileName_c_e.bz2 password (for example python3 DecryptDecompress.py 1400_c_e.bz2 thisIsMyPassword). To finally test that the original file and the final decompressed file match run the TestLostData.py using the command line code: TestLostData.py fileName.csv (for example python3 TestLostData.py 1400.csv). Note that all this code is intended to be run an a Raspberry Pi Zero.

The project report is also in the repo.
