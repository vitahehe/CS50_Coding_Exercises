greeting = input("Greeting good sir").strip().lower()
response = list(greeting)
if (response[0] == "h" and "hello" not in greeting):
       print("$20")
elif greeting == "hello":
    print("$0")
else:
    print("$100")
