def main():
    openText = open('nbCoverPage.txt', 'r')

    readingLines = openText.readlines()
    print('readLines', openText.readlines)
    for x in readingLines:
        print(x)


if __name__ == '__main__':
    main()

