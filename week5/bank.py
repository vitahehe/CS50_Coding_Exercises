def main():
    juging = value(input("Greeting good sir"))
    print(int(juging))

def value(s):
     greeting=s.strip().lower()
     if 'hello' == greeting[:5]:
         x=0
     elif 'h'== greeting[0]:
         x=20
     else:
         x=100
     return x



if __name__ == "__main__":
    main()
