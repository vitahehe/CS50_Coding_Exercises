file = input("whats the file name?").strip().lower()
if ".pdf" in file:
    print("application/pdf")
if ".gif" in file:
    print("image/gif")
if ".jpg" in file:
    print("image/jpg")
if ".jepg" in file:
    print("image/jepg")
if ".png" in file:
    print(image/png)
if ".txt" in file:
    print("text/plain")
if ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
