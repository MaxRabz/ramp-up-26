def stutter(word):
    return f"{word[:2]}... {word[:2]}... {word}?"

def main():
    print(stutter("incredible")) 
    print(stutter("enthusiastic")) 
    print(stutter("outstanding"))

if __name__ == "__main__":    
    main()