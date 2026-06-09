def number_length(num):
    len = 0
    for i in str(num):
        len += 1
    return len

def main():
    print(number_length(10)) 
    print(number_length(500)) 
    print(number_length(0))

if __name__ == "__main__":    
    main()