greeting = input("Greeting good sir").strip().lower()
response = list(greeting)
if response[0] == "h" and response != "hello":
    print("20$")
else:
    print("100$")
