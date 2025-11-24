

1.Write a function factorial(n) that calculates the factorial of
a non-negative integer n (n!).

Explanation of the factorial(n) 

What is factorial?: Factorial is a mathematical operation for non-negative integers. For example, \(4!=4\times 3\times 2\times 1=/24). The factorial of 0 (\(0!\)) is defined as 1.

What is a function?: A function is a block of reusable code that performs a specific task. In this case, the factorial(n) function takes an integer n as input and returns its factorial as the output.

Why non-negative?: Factorial is not defined for negative integers, so the function needs to handle non-negative inputs, typically by either raising an error for negative inputs or assuming valid input. 

2.Write a function prime_factors(n) that returns the list of
prime factors of a number. 

Explanation of the Logic
The function uses an optimized trial division algorithm to find all prime factors, including repeated ones. 
Handling the factor 2: The code first addresses the only even prime number, 2.
 It repeatedly checks if the number n is divisible by 2. If it is, 2 is added to the factors list, and n is divided by 2.
  This step ensures that once this loop finishes, the remaining n must be an odd number, allowing subsequent checks to focus solely on odd divisors.

3.Write a function count_distinct_prime_factors(n) that returns
how many unique prime factors a number has.
.Explanation:
The function count_distinct_prime_factors(n) identifies the unique prime numbers that divide n. It iterates through potential divisors starting from 2. If a divisor d divides n, it is added to a set (to ensure uniqueness) and n is repeatedly divided by d until it's no longer divisible. This process continues until d*d exceeds the remaining n. If, after this loop, n is still greater than 1, it means the remaining n is itself a prime factor, which is then added to the set. Finally, the size of the set represents the count of distinct prime factors.

4.Write a function multiplicative_persistence(n) that counts
how many steps until a number's digits multiply to a
single digit.

Explanation:
Base Case: If the input number n is already a single digit (less than 10), its multiplicative persistence is 0, as no steps are needed.
Initialization: A steps counter is initialized to 0, and current_num is set to the input n.
Iteration: The while loop continues as long as current_num is a multi-digit number (greater than or equal to 10).
Inside the loop, product is initialized to 1.
The current_num is converted to a string to easily access its individual digits.
Each digit is converted back to an integer and multiplied into product.
current_num is updated to this new product.
The steps counter is incremented.
Return: Once current_num becomes a single-digit number, the loop terminates, and the total steps taken are returned.

5.Write a function Fibonacci Prime
Check is_fibonacci_prime(n) that checks if a number is
both Fibonacci and prime.

Explanation:

is_prime(num): This helper function checks if a number is prime. It returns False for numbers less than or equal to 1. Otherwise, it iterates from 2 up to the square root of num, checking for divisibility. If any divisor is found, it's not prime, returning False. If no divisors are found, it's prime, returning True.
is_fibonacci(num): This helper function checks if a number is a Fibonacci number using a mathematical property: a number n is Fibonacci if and only if 5*n^2 + 4 or 5*n^2 - 4 is a perfect square. It uses another helper is_perfect_square to check this condition. 
is_fibonacci_prime(n): This main function combines the checks. It calls is_fibonacci(n) and is_prime(n). If both return True, then n is a Fibonacci prime, and the function returns True. Otherwise, it returns False.

6.Write a function Polygonal Numbers polygonal_number(s,
n) that returns the n-th s-gonal number.
Explanation 
Polygonal Numbers: These are figurate numbers representing the number of points in a regular polygon with a given number of sides (\(s\)).
The Formula: The function uses the standard formula for the \(n\)-th \(s\)-gonal number:\(P(s,n)=\frac{n^{2}(s-2)-n(s-4)}{2}\)Parameters: 
s is the number of sides of the polygon (e.g., 3 for triangular, 4 for square, 5 for pentagonal).
n is the position in the sequence (e.g., the 1st, 2nd, 3rd number).
Function Logic: The Python code directly implements this formula, ensuring integer division (// 2) as all results are integers.  
 
7.Write a function Partition Function
p(n) partition_function(n) that calculates the number of
distinct ways to write n as a sum of positive integers.

Explanation:

Base case: The function initializes a list dp of size n+1 with all zeros, and sets dp[0] to 1 because there is one way to partition zero (the empty sum).
Dynamic programming: It iterates through each integer i from 1 to n. For each i, it then iterates through j from i to n, updating dp[j] by adding dp[j - i] to it. This represents adding the integer i to all partitions of j-i to form a partition of j.
Result: The final result is stored in dp[n], which is the total number of partitions for the integer n
