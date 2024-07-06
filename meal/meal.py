def main():
    given = str(input("whats the time?").strip().lower())
    #def convert(x,y,z):
        #return x.replace(y,z)

    #converted_time = float(convert(time, ":", "."))
    # 07.00 <= converted_time <= 08.00:
       # print("breakfast tifime")
    #if 12.00 <= converted_time <= 13.00:
       # print("lunch time")
    #if 18.00 <= converted_time <= 19.00:
       # print("dinner time")
    def convert(time):
       split_time = time.split(":")
       splitrtime1= float(split_time[0])
       splitrtime2= float(split_time[1])
       return splitrtime1 + splitrtime2/60
    aaaaa = convert(given)
    if 07.00 <= aaaaa <= 08.00:
       print("breakfast tifime")
    elif 12.00 <= aaaaa <= 13.00:
        print("lunch time")
    elif 18.00 <= aaaaa <= 19.00:
        print("dinner time")
if __name__ == "__main__":
    main()
