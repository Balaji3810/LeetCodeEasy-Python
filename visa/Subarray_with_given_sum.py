//https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&company[]=Visa&sortBy=submissions
  
def subArraySum(arr, n, sum_):
    for i in range(n):
        currSum = arr[i]
        j = i + 1
        while j <= n:
            if currSum == sum_:
                print("Sum of elements %d from %d" % (i+1, j))
                return 1
            if currSum > sum_ or j == n:
                break
            currSum += arr[j]
            j += 1
    print("No subarray found")
    return 0


# Driver program
if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum_ = 6

    subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
