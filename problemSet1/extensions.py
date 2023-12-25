file = input("Enter file: ").strip().lower()

ext = file.split(".")[-1]

d = {
    "gif": "image/gif",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
    }

if ext in d:
    print(d[ext])
else:
    print("application/octet-stream")
