def main():
    ...


def value(greeting):
     greeting = input("Greeting good sir").strip().lower()
response = list(greeting)
if response[0] == "h" and "hello" not in greeting:
       print("$20")
elif "hello" in greeting:
    print("$0")
else:
    print("$100")



if __name__ == "__main__":
    main()
