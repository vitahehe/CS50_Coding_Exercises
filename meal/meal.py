def main():
    time = str(input("whats the time?").strip().lower())
    def convert(x,y,z):
        return x.replace(y,z)
    converted_time = float(convert(time, ":", "."))
    if 07.00 <= converted_time <= 08.00:
        print("breakfast time")
    if 12.00 <= converted_time <= 13.00:
        print("lunch time")
    if 18.00 <= converted_time <= 19.00:
        print("dinner time")7
main()
