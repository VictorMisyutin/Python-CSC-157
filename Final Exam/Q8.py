def list_total(list):
    total = 0
    for number in list:
        total += number
    return total

def main():
    list = [1,7,3,6,89,1,3,4,5]
    print(list_total(list))

if __name__ == "__main__":
    main()