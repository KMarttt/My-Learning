def main():
    file_name = input("File name: ").lower()
    if extension(file_name) != None:
        print(extension(file_name))

#Would have used match if it works in this version of python
def extension(file_name):
    extension = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }


    for suffix in extension:
        if file_name.endswith(suffix):
            return (extension[suffix])

main()