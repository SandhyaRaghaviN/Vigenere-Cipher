# This function returns the encrypted text generated with the help of the key

def encryption(s, Key):

    # O(n)--time complexity
    # O(n)--auxilliary space complexity

    output = ""

    # key iterations

    j = 0
    for i in range(len(s)):

        # iterating through all characters in the give string.

        if s[i] != ' ':

            # new character after encryption is equal to the given character shifted
            # by alphabetical number of the corresponding key character
            # e.g: A+L=L => A shifted L times which is equal L

            mappedNumber = (ord(s[i]) + ord(Key[j])) % 26

            # Why %26? ==> to give cyclic nature while shifting
            # --> if u shift Z by one unit it should give A
            # but according to ASCII charcters it should give the next ASCII charcter of Z
            # alphabetical number of the new character

            c = chr(mappedNumber + ord('A'))
            output = output + c

            # adding a new character into the output string

            if j == (len(Key) - 1):

                # if key characters are exhausted reuse the key

                j = 0
            else:
                j = j + 1
        else:

            # add to output if it is a space

            output = output + s[i]
    return output

# This function decrypts the encrypted text and returns the original text

def decryption(s, Key):
    output = ""

    # start with a empty string

    j = 0
    for i in range(len(s)):

        # iterate through all the elements in the string

        if s[i] != ' ':

            # decrypted literal = key(corresponding character of key) times back shifted the given literal
            # e.g: L after decryption with key character L --> A
            # L(key character) times backshifted L gives A

            mappedNumber = (ord(s[i]) - ord(Key[j])) % 26

            # alphabetical number of the given character

            c = chr(mappedNumber + ord('A'))
            output = output + c

            # adding new character into the output string

            if j == (len(Key) - 1):

                # if key characters get exhausted(or key is totally used) start with the same key again

                j = 0
            else:
                j = j + 1
        else:

            # add the element as it is => if it is a space

            output = output + s[i]
    return output


if __name__ == "__main__":
    print("Key and Message can only be alphabetic")
    str = input("Enter the Message: ").upper()
    Key = input("Enter the Key: ").upper()
    encyrpted_text = encryption(str, Key)
    print("Encrypted Text: ", encyrpted_text)
    decyrpted_text = decryption(encyrpted_text, Key)
    print("Decrypted Text: ", decyrpted_text)

