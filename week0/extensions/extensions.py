file = input("whats the file name?").strip().lower()
if ".pdf" in file:
    print("application/pdf")
elif ".gif" in file:
    print("image/gif")
elif ".jpg" in file:
    print("image/jpg")
elif ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print(image/png)
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
