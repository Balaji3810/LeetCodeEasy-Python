//https://www.geeksforgeeks.org/check-whether-an-array-is-subarray-of-another-array/
def isSubArray(A, B, n, m):
    i, j = 0, 0
    while (i < n and j < m):
        if A[i] == B[j]:
            i += 1
            j += 1
            
            if j == m:
                return True
        else:
            i = i - j + 1
            j = 0
    return False


# Driver Code
if __name__ == '__main__':
    A = [ 2, 3, 0, 5, 1, 1, 2 ];
    n = len(A);
    B = [ 3, 0, 5, 1 ];
    m = len(B);
 
    if (isSubArray(A, B, n, m)):
        print("YES");
    else:
        print("NO");
 
# This code is contributed by Rajput-Ji  
 
