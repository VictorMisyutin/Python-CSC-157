def larger_than_n(list, n):
    for number in list:
        if number > n:
            print(number)

def main():
    list = [1,8,2,9,17,34,6] 
    n = 10
    larger_than_n(list,n)

if __name__ == "__main__":
    main()