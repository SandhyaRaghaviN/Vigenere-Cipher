# Vigenere-Cipher

PROBLEM STATEMENT: 
Vigenère Cipher is a method of encrypting alphabetic text. It uses a simple form  of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on  substitution, using multiple substitution alphabets. The encryption of the  original text is done using the Vigenère square or Vigenère table. 

SAMPLE INPUT & OUTPUT: 
Input: Plaintext: MICHIGAN TECHNOLOGICAL UNIVERSITY 
Keyword: HOUGHTON 
Output: Ciphertext: TWWNPZOA ASWNUHZBNWWGS NBVCSLYPMM 

For generating key, the given keyword is repeated in a circular manner until it  matches the length of the plain text. 

The keyword HOUGHTON generates the key HOUGHTON  HOUGHTONHOUGH TONHOUGNTO.  The plain text is then encrypted.
