def sum_odd_and_even(lst):
    odd_sum = sum(num for num in lst if num % 2 != 0)
    even_sum = sum(num for num in lst if num % 2 == 0)
    return [even_sum, odd_sum]

def main():
    print(sum_odd_and_even([1, 2, 3, 4, 5, 6])) 
    print(sum_odd_and_even([0, -1, -2, -3, -4, -5])) 
    print(sum_odd_and_even([]))

if __name__ == "__main__":    
    main()