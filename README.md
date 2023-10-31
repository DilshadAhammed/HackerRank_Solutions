# Here is my HackerRank Solutions

> The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

---
## Solution Approach

>You can find the problem statements and descriptions for these solutions by following the provided commands within the Python programs or by visiting the Hackerrank website [here](https://www.hackerrank.com/challenges). Simply search for the program name to access the detailed problem statement.

---

## Extra Long Factorials

- [Solution](./Extra%20Long%20Factorials/ExtraLongFactorials.py)

### - Explanation:

        1. result = 1: We initialize the result variable to 1 because in factorials, any number multiplied by 1 is itself. Setting the initial value to 1 ensures that the multiplication process starts correctly.
        2. for i in range(1, n + 1): This for loop iterates through the numbers from 1 to n, inclusive. In other words, it considers all the integers from 1 to the input number n.
        3. result *= i: Inside the loop, the current result value is multiplied by the loop variable i. This operation accumulates the factorial by multiplying the current result with the next number in the sequence.
        4. After the loop completes, result contains the factorial of the input number n. It stores the total product of all integers from 1 to n.
        5. print(result): This line of code prints the calculated factorial. The print function outputs the final result, which is the factorial of the input number n.
---

## Apple and Orange

- [Solution](./AppleandOrange/AppleandOrange.py)

### - Explanation:

        The function iterates through the lists of apples and oranges, adjusting their positions based on the tree positions (a and b). If the adjusted position falls within the range from s to t (inclusive), it increments the respective fruit count.

---

## Birthday Cake Candles

- [Solution](./Birthday%20Cake%20Candles/Birthday%20Cake%20Candles.py)

### - Explanation:

        1.The max function is used to find the maximum height among all the candles in the input list candles.

        2.The count method is then used to count how many times the maximum height appears in the list, indicating how many candles have the tallest height.

        3.The count is returned as the result.

        For example, if the input list candles is [4, 4, 1, 3, 2, 4], the function will identify that the tallest candles have a height of 4 and count how many times 4 appears in the list, which is 3. Therefore, the function will return 3 as the output.

---

## Circular Array Rotation

- [Solution](./CircularArrayRotation/CircularArrayRotation.py)

### - Explanation:

        1. rotation_index = k % len(a): Calculate the effective rotation index to avoid unnecessary full rotations. Taking the modulo with the length of the array ensures that the rotation index is within the bounds of the array length.

        2. rotated_array = a[-rotation_index:] + a[:-rotation_index]: Perform the circular rotation by slicing the array into two parts: elements from the negative rotation index to the end, and elements from the start to the negative rotation index. Concatenate these two parts to form the rotated array.

        3. results = [rotated_array[q] for q in queries]: For each query index q, extract the corresponding element from the rotated array and store it in the results list. This answers the queries about the rotated array.

---

## Day Of The Programmer

- [Solution](./DayOfTheProgrammer/DayOfTheProgrammer.py)

### - Explanation:

        The function first checks for the special case of the transition year 1918, returning '26.09.1918'. For other years, it uses a ternary conditional operator to check if the year is a leap year based on either the Julian or Gregorian calendar, returning '12.09.YYYY' for leap years and '13.09.YYYY' for non-leap years, where 'YYYY' is the input year."

---

## Jumping on the Clouds

- [Solution](./Jumping%20on%20the%20Cloudsn/JumpingontheClouds.py)

### - Explanation:

        1. jumps = 0: Initialize a variable to count the number of jumps needed to reach the end, starting at 0.

        2. i = 0: Initialize the current position to the first cloud (index 0).

        3. The while loop continues until the current position i is less than the index of the last cloud (i.e., len(c) - 1).

        4. Inside the loop:
        Check if a double jump (two clouds ahead) is safe and within bounds (i + 2 < len(c)). If it is, perform the double jump by increasing i by 2.
If a double jump is not safe or not within bounds, perform a single jump by increasing i by 1.
        5. Increment the jumps count after each jump.

        6. Once the loop ends, return the total number of jumps, which represents the minimum number of jumps required to reach the end of the cloud sequence.
---

## Minimum Distance

- [Solution](./MinimumDistance/MinimumDistance.py)

### - Explanation:

        1. Create a dictionary element_indices to store the most recent index of each element encountered in the array a.

        2. Initialize the min_distance variable to a large value (float('inf')).

        3. Iterate through the array a using enumeration to keep track of the indices.

        4. For each element, check if it has been encountered before (num in element_indices). If it has, calculate the distance between the current index and the most recent index where the element was seen (i - element_indices[num]). Update min_distance with the smaller value between the current minimum distance and the calculated distance.

        5. Update the most recent index of the current element in the element_indices dictionary.

        6. After iterating through the array, if min_distance remains as the initial large value, it means no equal elements were found, so return -1. Otherwise, return the calculated min_distance representing the minimum distance between equal elements.
---

## Save The Prisoner

- [Solution](./SaveThePrisoner/SaveThePrisoner.py)

### - Explanation:

        1. remaining_sweets = m % n: Calculate the number of sweets left after distributing to complete rounds of all prisoners. This helps determine the position of the prisoner who will receive the last sweet.

        2. (s + remaining_sweets - 1) % n: Calculate the final position of the prisoner who receives the last sweet. Subtracting 1 accounts for 1-based indexing (Python uses 0-based indexing) and the modulo operation ensures the position remains within the range [1, n].

        3. Handle the edge case where the final position is 0 (the last prisoner). In this case, return the total number of prisoners n.

---

## Sherlock And Squares

- [Solution](./SherlockAndSquares/SherlockAndSquares.py)

### - Explanation:

        1. math.sqrt(b): Calculate the square root of the largest number b.
        2. math.sqrt(a): Calculate the square root of the smallest number a.
        3. math.floor(math.sqrt(b)): Take the floor value of the square root of b to get the largest integer whose square is less than or equal to b.
        4. math.ceil(math.sqrt(a)): Take the ceiling value of the square root of a to get the smallest integer whose square is greater than or equal to a.
        5. Subtract the ceiling value from the floor value and add 1. This represents the count of perfect squares within the range [a, b].
        6. Return the count of perfect squares as the result.
---

## Taum and B'day

- [Solution](./Taum%20and%20B'day/Taum%20and%20B'day.py)

### - Explanation:

        1. min(bc, wc + z): Calculates the minimum cost of purchasing black gifts. It compares the cost of black gifts (bc) with the cost of converting white gifts to black gifts (wc + z). It chooses the lower cost option.

        2. min(wc, bc + z): Calculates the minimum cost of purchasing white gifts. It compares the cost of white gifts (wc) with the cost of converting black gifts to white gifts (bc + z). It chooses the lower cost option.

        3. b * min(bc, wc + z) + w * min(wc, bc + z): Calculates the total minimum cost. Multiplies the minimum cost of black gifts by the number of black gifts (b) and the minimum cost of white gifts by the number of white gifts (w), then sums the two costs.

---
