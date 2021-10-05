# this function creates the b vector, according to the rules
import sys
import time


def create_b_vector(n):
    b = []  # empty vector
    for i in range(n):  # for loop to fill the b vector
        if i == 0 or i == n - 1:  # if we are at the end of the b vector append just 7
            b.append(7)
        elif i == (n / 2) - 1 or i == (n / 2):  # if we are in the middle of the b vector append just 10
            b.append(10)
        else:  # otherwise, 9
            b.append(9)
    return b  # return this vector


# the main function to implement gauss method, taking as parameters n (size of matrix A) and b vector
def gauss_method(n, b):
    x = []  # at the beginning we get x vector to fulfill
    for i in range(n):  # for loop to set our x vector fulfilled of zeros
        x.append(0.0)
    c = 0  # just a counter to know how many iterations are required to get the solutions
    while True:  # while true, just to iterate
        max_value_differ = 0.0  # let's define a max value as the difference between x-new and x-old
        for i in range(n):  # for loop to iterate all values. We need just O(n).
            x_i = x[i]  # getting i-th element of x array
            s = 0.0  # this is the sum, set to zero at each iteration
            if i > 0:  # if i is greater then zero, we must add to sum 2*(x-ith-1)
                s += 2.0 * x[i - 1]
            if (i > n / 2) or i < (n / 2) - 1:  # if we are in part of matrix A greater then the middle of A,
                # add -1*x[size of A-1-i]
                s += -1.0 * x[n - 1 - i]
            if i + 1 < n:  # if i+1 is less than n, add 2*x[i-th+1]
                s += 2.0 * x[i + 1]

            x[i] = (b[i] - s) / 6.0  # according to the formula, so subtracting the computed sum and dividing
            #  by a(i-th, i-th)
            if abs(x_i - x[i]) > max_value_differ:  # if the difference is greater than previous max, assign new value
                max_value_differ = abs(x_i - x[i])

        print("MEX DIFFER: ", max_value_differ)
        c += 1  # increase counter
        if max_value_differ < 10 ** (-16):  # condition for break
            break

    return x, c  # return solutions and max iterations to get our them


if __name__ == '__main__':

    #############################################
    # This program allows the user to define a n*n matrix (with some constraints,
    # according to the assignment)
    # ###########################################
    # we must not store matrix A, it is not necessary because we already know the values of A and where they are

    n = 1  # just initialize to enter in the loop
    counter = 0  # counter, if equal to 5, the program exits
    while n % 2 == 1 and counter < 5:  # try to get a number that is even from the user
        time.sleep(0.5)
        n = int(input("Insert the value of n: "))  # get n
        if n % 2 == 1:  # if n is not even, print a warning
            print("\n***** n is not even, retry *****\n", file=sys.stderr)
            continue
        counter += 1  # increase counter, it can be maximum equal to 5, then exit
    b = create_b_vector(n)  # create the vector b
    # print("Vector b is: \n", b)
    x, counter = gauss_method(n, b)  # get our values from here
    print(x)  # print x if you wanna show results

    print("Max iterations: ", counter)  # print number of iterations to get the results
    print("EVERYTHING WENT OKAY: ", sum(x) == n and len(x) == n)  # just a little check if everything went right

    #  THIS PART CAN BE USED TO ROUND values of X if you want them to be integers
    for j in range(len(x)):
        x[j]=round(x[j])
    #print(x)



# ------------------- EX 1: with n=100'000, we will have 86 iterations -------------------------
