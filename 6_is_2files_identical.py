import hashlib

def hash_file(file_name):
    h = hashlib.sha1()

    try:
        with open(file_name, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
        return None


file1 = "a.txt"
file2 = "b.txt"

hash1 = hash_file(file1)
hash2 = hash_file(file2)

if hash1 is None or hash2 is None:
    print("Comparison failed due to file error.")
elif hash1 == hash2:
    print("The files are identical.")
else:
    print("The files are not identical.")
