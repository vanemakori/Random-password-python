# Random-password-python
Writing a simple one line code in python to generate random passwords by combining letters, numbers and symbols

Creating a 'strong' password is not an easy task and to rememeber it precisely is not easy.

This code is a one line code that generates a random password using random library in python and combining the ascii characters. 

The commented code # runs too just gives different results and it does not combine lowers case, upper case.

The final code running combines all the uppercase and lowercase letters, digits and the symbols to produce a random password each time. I used random.SystemRandom for the cryptography aspect (someone might explain this better) but it's meant to generate a 'stronger' password.

I used .sample() for the output purposes (specified to print out a password of length 10) and trial and just because :), you can use .choice() if prefered.

Otherwise you can pay for LastPass and use it to generate a password for you and store it. PS: it uses the same procedure.

