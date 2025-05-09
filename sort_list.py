def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # Read a list of numbers from the user
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    
    # Sort the list using the bubble_sort function
    bubble_sort(numbers)
    
    # Print the sorted list
    print("Sorted list:", numbers)

# Example usage
main()