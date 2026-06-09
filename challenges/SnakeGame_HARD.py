def snakeFill(space):
    space = space*space
    snake_size = 1
    apples_eaten = 0
    while snake_size < space:
        apples_eaten += 1
        snake_size *= 2
    apples_eaten -= 1
    return apples_eaten

def main():
    print(snakeFill(3)) 
    print(snakeFill(6)) 
    print(snakeFill(24))

if __name__ == "__main__":    
    main()