import os



def main():
    print(os.system("git pull origin master"))
    print(os.system("git add ."))
    print(os.system("git commit -m \".\""))
    print(os.system("git push origin master"))


if __name__ == '__main__':
    main()
