# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SWETHA JAGANNATHAN

*INTERN ID*: CT08NNB

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

The File Integrity Checker is a Python-based utility that monitors changes in files within a specified directory. It calculates cryptographic hash values for files and compares them with previously stored hashes to detect modifications, additions, or deletions.

How It Works
Hash Calculation:

The script computes a hash (default: SHA-256) for each file in the target directory.
Hashes are generated in chunks (4 KB) to handle large files efficiently.
Storing & Loading Hashes:

The script saves computed hashes to a JSON file (file_hashes.json).
If the JSON file exists, previously stored hashes are loaded for comparison.
Integrity Check:

The script scans the directory and compares current hashes with stored values.
It classifies files as:
Unchanged ([OK]): Hash matches the stored value.
Modified ([WARNING]): Hash differs from the stored value.
Newly Added ([NEW]): File exists but has no stored hash.
Deleted ([DELETED]): File was in the previous record but is missing.
Execution & User Input:

The user provides a directory to monitor via input.
The script then performs an integrity check and updates the hash database.

OUTPUT:

![Image](https://github.com/user-attachments/assets/dcc03925-ac4b-4737-a7a6-dea6b3afec2d)

![Image](https://github.com/user-attachments/assets/79425bc1-5bcd-4a07-be01-21f52ea44a74)

![Image](https://github.com/user-attachments/assets/713f3b34-89e7-426e-98bb-16f2a2a3ff06)
