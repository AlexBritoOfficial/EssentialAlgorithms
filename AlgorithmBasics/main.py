
# Euclidean Method
def gcd(a, b):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a

if __name__ == "__main__":

    print(gcd(123456,789012))

"""
                                                Big O Notation
    ----------------------------------------------------------------------------------------------------------------
    Big O Notation: A function used to describe how the algorithm worst-case performance relates to the problem 
    size as the size grows large.
    
    -----------------------------------------------------------------------------------------------------------------
    Five Basic Rules for Big O Notation:
    
    #1) If an algorithm performs a certain sequence of steps f(n) times for a mathematical function f,
    it takes O(f(n)) steps.
    
        PseudoCode Example: 
        
            Integer: FindLargest(Integer: array[])
                Integer: largest = array[0]
                
                For i = 1 To <largest index>
                    If(array[i] > largest) Then largest = array[i]
                Next i
                
                Return largest
            
            End  FindLargest
            
            * This algorithm examines each of the N items in the array once, so it has O(N) performance.
    
    #2) If an algorithm performs an operation that takes O(f(n)) steps and then performs a second operation that tekes
    O(g(n)) steps for functions f and g, then the algorithms total performance is O(f(n) + g(n)).
    
        PseudoCode Example: 
        
            Integer: FindLargest(Integer: array[])
                Integer: largest = array[0] // O(1)
                
                For i = 1 To <largest index> // O(N)
                    If(array[i] > largest) Then largest = array[i] O(1)
                Next i
                
                Return largest
            
            End  FindLargest
            
            *   This algorithm performs one setup step before it enters its loop and then performs one more step after it finishes the loop. 
                Both steps cost O(1), so the total runtime of the algorithm is O(1 + N + 1) = O(2 + N)
                examines each of the N items in the array once, so it has O(N) performance.
    
        
    #3) If an algorithm performs an operation that takes O(f(n) + g(n)) time, and the function f(n) is greater than 
    g(n) for large N, the algorithms performance can be simplified to O(f(n))
    
        *   The preceding example showed example showed that the FindLargest algorithm has a runtime of O(2 + N), When N grows large, the function 
            N is larger than the constant value 2, so O(2 + N), simplifies to O(N). Ignoring the smaller function lets you focus on the algorithms 
            asymptotic behavior as the problem size becomes very large.
    
    #4) If an algorithm performs an operation that takes O(f(n)) steps, and for every step in that operation it performs
    another O(g(n)) steps, then the algorithms total performance is O(f(n)) * g(n))
    
        PseudoCode Example: Consider the following algorithm that determines whether an array contains any duplicate items. (Note that this isn't
        the most efficient way to detect duplicates)
        
            Boolean: ContainsDuplicates(Integer: array[])
                // Loop over all the array's items
                For i = 0 to <largest index>
                    For j = 0 to <largest index>
                        // See if these two items are duplicates
                        If (i != j) Then
                            if(array[i] == array[j]) Then Return True
                        End If
                    Next j
                Next i
                // If we get to this point, there are no duplicates.
                Return False
            End ContainsDuplicates
            
            *   This algorithm contains two nested loops. The outer loop iterates over all the array's N items, so it takes O(N) steps
               
                For each trip through the outer loop, the inner loop also iterates over the N items in the array, so it also takes O(N)
                steps.
                
                Because one loop is nested inside the other, the combined performance is O(N * N) = O(N^2)  
            
    #5) Ignore constant multiples. If C is a constant, O(C * f(n)) is the same as O(f(n)) and O(f(C * n)) is the same as O(f(n))
    
"""

"""
                                                    Common Runtime Functions

"""