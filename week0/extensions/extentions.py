file = input("whats the file name?").strip().lower()
if ".pdf" in file:
    print("application/pdf")
elif ".gif" in file:
    print("image/gif")
elif ".jpg" in file:
    print("image/jpg")
elif ".jepg" in file:
    print("image/jepg")
elif ".png" in file:
    print(image/png)
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
