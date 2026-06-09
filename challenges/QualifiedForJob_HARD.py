def interview(list, timeTaken):
    qualified = True
    if len(list) != 8 or list[0] > 5 or list[1] > 5 or list[2] > 10 or list[3] > 10 or list[4] > 15 or list[5] > 15 or list[6] > 20 or list[7] > 20:
        qualified = False
    if timeTaken > 120:
        qualified = False
    return "qualified" if qualified else "disqualified"

def main():
    print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
    print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
    print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
    print(interview([5, 5, 10, 10, 15, 15, 20], 120))
    print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))

if __name__ == "__main__":    
    main()