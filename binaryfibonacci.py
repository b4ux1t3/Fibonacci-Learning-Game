#Simple program which will provide the conversion and quiz engine for the project.

print "Welcome. If you need help, type 'help()'."
# Establishes the Fibonnacci number at the nth degree.
def fib(g):
    terms = [0, 1]
    i = 2
    while i <= g:
        terms.append(terms[i-1] + terms [i - 2])
        i = i + 1
    return terms[g]

# Converts the Fibonacci (or any) number into a decimal.
def bin_conv(number):
    return bin(number)

# Puts everything together, returning the binary notation for any nth degree.
def nth_fib():
    degree = int(raw_input("Which Fibonacci number would you like to see in binary?"))
    if degree > 1:
        print str(fib(degree)) + ", which is the " + str(degree) + "th Fibonacci number, would be " + str(bin_conv(fib(degree)))[2:] + " in binary notation."
    return bin_conv(fib(degree))


# Prints each Fibonacci number up to n.
def fib_in_range():
    n = int(raw_input("At which degree of Fibonacci numbers would you like to stop?"))
    li = []
    z = 0
    print "This is a list of all Fibonacci numbers up to the " + str(n) + "th degree in decimal and binary notation:"
    for i in range(n):
        z += 1
        print str(z) + ".", fib(z), ":", str(bin_conv(fib(z)))[2:]
        li.append(bin_conv(fib(z)))
    return li

def help():
    print"Command List:"
    print "_" * 30
    print "fib(n): Calculates Fibonacci number at nth degree. Returns an integer."
    print "_" * 30
    print "bin_conv(n): Converts 'n' to binary. Returns non-string binary notation."
    print "_" * 30
    print "nth_fib(): Asks for user-input. Converts user-input into Fibonacci number at that degree, then displays the binary form. Returns non-string binary notation."
    print "_" * 30
    print "fib_in_range(): Asks for user input. Converts all degrees of Fibonacci numbers up to and including user input. Returns list containing each non-string binary notation."
