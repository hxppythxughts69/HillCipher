def Encrypt(matrix, word):
    word = word.ljust((len(word) + (len(matrix) - (len(word) % len(matrix)))), 'x')
    chunks = [word[i:(i+len(matrix))] for i in range(0, len(word), len(matrix))]
    wordToNmr = [[(ord(i)-96) for i in chunk] for chunk in chunks]

    cryptord = [[] for y in range(len(matrix))]

    for i in range(len(wordToNmr)):
        for o in range(len(matrix)):
            char_sum = 0;
            for j in range(len(matrix[0])):
                char_sum += int(matrix[o][j]) * wordToNmr[i][j]
            cryptord[o].append(char_sum)
    
    for i in range(len(cryptord)):
        for o in range(len(cryptord[0])):
            cryptord[i][o] = cryptord[i][o] % 26

    nmrToLetter = [[(chr(i+96)) for i in crypt] for crypt in cryptord]

    output = ""
    for nmrs in nmrToLetter:
        for nmr in nmrs: 
            output += str(nmr)
    print(output)



def Decrypt(matrix, word): #work in progress
    inversDict = {
        1: 1,
        9: 3,
        21: 5,
        15: 7,
        3: 9,
        19: 11,
        7: 15,
        23: 17,
        11: 19,
        5: 21,
        17: 23,
        25: 25
    }

    word = word.ljust((len(word) + (len(matrix) - (len(word) % len(matrix)))), 'x')
    chunks = [word[i:(i+len(matrix))] for i in range(0, len(word), len(matrix))]
    wordToNmr = [[(ord(i)-96) for i in chunk] for chunk in chunks]

    






def main():
    matrix = input("Input the matrix row by row, seperating rows by ',' and numbers by ' '. Like this 13 4 9,5 3 4,8 9 5\n")
    matrix = [row.split(' ') for row in matrix.split(',')]
    word = input("Input the word you want to encrypt/decrypt:\n")
    if input("Do you want to Encrypt or DeCrypt? e/d ").lower() == "e":
        Encrypt(matrix, word.lower())
    else:
        Decrypt(matrix, word.lower())


if __name__ == "__main__":
    main()