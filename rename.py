import os


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f


def main():
    x = 1
    base = 'C:/Users/JJTOM/Desktop/2/'
    for i in findAllFile(base):
        print(i)
        os.rename(base + i, base + '20210711-(' + str(x) + ').jpg')
        x = x + 1


if __name__ == '__main__':
    main()
