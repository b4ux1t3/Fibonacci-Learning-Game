from math import sqrt

print "Welcome. If you need help, type 'help()'."
# Establishes the Fibonnacci number at the nth degree.
def fib(g):
    f = int(((1.0+sqrt(5.0))**g-(1.0-sqrt(5.0))**g)/(2.0**g*sqrt(5.0)))
    return f

# Converts the Fibonacci (or any) number into a decimal.
def bin_conv(number):
    return bin(number)

# Puts everything together, returning the binary notation for any nth degree.
def all_together_now():
    degree = int(raw_input("Which degree of Fibonacci numbers would you like to see in binary?"))
    if degree > 1:
        print str(fib(degree)) + ", which is the " + str(degree) + "th Fibonacci number, would be " + str(bin_conv(fib(degree)))[2:] + " in binary notation."
    return bin_conv(fib(degree))


# Prints each Fibonacci number up to n.
def range_fibs():
    n = int(raw_input("At which degree of Fibonacci numbers would you like to stop?"))
    li = []
    z = 0
    print "This is a list of all Fibonacci numbers up to the " + str(n) + "th degree in decimal and binary notation:"
    for i in range(n):
        z += 1
        print str(z) + ".", fib(z), ":", str(bin_conv(fib(z)))[2:]
        li.append(bin_conv(fib(n)))
    return li

def help():
    print"Command List:"
    print "_" * 30
    print "fib(n): Calculates Fibonacci number at nth degree. Returns an integer."
    print "_" * 30
    print "bin_conv(n): Converts 'n' to binary. Returns non-string binary notation."
    print "_" * 30
    print "all_together_now(): Asks for user-input. Converts user-input into Fibonacci number at that degree, then displays the binary form. Returns non-string binary notation."
    print "_" * 30
    print "range_fibs(): Asks for user input. Converts all degrees of Fibonacci numbers up to and including user input. Returns list containing each non-string binary notation."
