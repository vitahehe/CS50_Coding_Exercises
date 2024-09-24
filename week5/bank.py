def main():
    juging = value(input("Greeting good sir").strip().lower())
    print(juging)

def value(greeting):
     if 'hello' == greeting[:4]:
         x=0
     elif 'h'== greeting[0]:
         x=20
     else:
         x=100
     return x



if __name__ == "__main__":
    main()
