def is_curzon(num):
    return True if (2 ** num + 1) % (2 * num + 1) == 0 else False

def main():
    print(is_curzon(5)) 
    print(is_curzon(10)) 
    print(is_curzon(14))   

if __name__ == "__main__":    
    main()