import sys
def main():
    list = sys.argv[1]
    print(f"  {"_" * len(list)}")
    print(f"< {list} >")
    print(f"  {"-" * len(list)}")
    print('''           \\
            \\   
            ^__^
            (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
        ''')
if __name__ == "__main__":
    main()