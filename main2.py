import random
# STEP  1 Is n composite?
# STEP  2 select an integer b at random with 1 <b<n 
# STEP  3 whether n passes Millers test to the base b
# STEP  4 we perform the miller test k times, where k is a positive integer.
# STEP  5 a random integer b will determine whether n passes Millers test to the base b

def millerTest(n,k):
    # Returns True if num is a prime number.
    # STEP 1 b a random 1<b<n
    # b = random.randint(1,n)
    a = n - 1
    t = 0
    while a % 2 == 0:
        a = a // 2
        t += 1
    # STEP # 3 whether n passes Millers test to the base b
    # STEp # 4 we perform the miller test k times, where k is a positive integer.
    for trials in range(k):  # try to falsify num's primality 5 times
        b = random.randrange(2, n - 1) # our range has to be between 1 and n
        failureCounter = 0
        remainder = pow(b, a, n)
        # remainder = pow(b,e,n)
        if remainder != 1:  
        ## unknown at each step  the algorithm answers false it says that n is not composite so that it is prime.
		# STEP # 6 with 10 iterations the probability that
		# the algorithm decides that n is prime when it really is composite is less than 1 in 1000000.
            i = -1
            while remainder != (n - 1):
                #print(i)
                #print(t)
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    remainder = (remainder ** 2) % n
    return True


def isPrime(num, k):
    # edge cases test since 2 and 3 is prime
    # 1 is not a prime num aand all non-postive numbers are non prime 
    if (num < 2):
        return False
    if (num == 2 or num == 3):
        return True
    if (k <= 3):
        print("for better result please set k to 3 < k < 10")	
    return millerTest(num, k)


n = input('Enter your number in question:')	
k = input('Enter your k (3-10) :')
number = int(n)
loop = int(k)
result = isPrime(number,loop)
print(result)
#140 AVG 
# test 1-1000000 prime numbes against give alg 
