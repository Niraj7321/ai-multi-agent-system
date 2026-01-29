"""
Create Sample Coding Tests
Run this to create example tests for demonstration
"""
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from src.coding_test_manager import CodingTestManager

def create_sample_tests():
    """Create sample tests for different difficulty levels"""
    manager = CodingTestManager()

    # Test 1: Beginner - String Operations
    print("Creating Beginner Test: String Operations...")
    test1 = manager.create_test(
        title="String Operations - Beginner Level",
        description="Test your basic string manipulation skills with Python",
        questions=[
            {
                "id": "q1",
                "title": "Reverse a String",
                "description": """Write a Python function that reverses a string.

Example:
Input: "hello"
Output: "olleh"

Your function should read input from stdin and print the reversed string.""",
                "language": "python",
                "points": 10,
                "test_cases": [
                    {"input": "hello", "expected_output": "olleh"},
                    {"input": "Python", "expected_output": "nohtyP"},
                    {"input": "12345", "expected_output": "54321"}
                ]
            },
            {
                "id": "q2",
                "title": "Count Vowels",
                "description": """Write a Python function that counts vowels in a string.

Example:
Input: "hello"
Output: 2

Count both uppercase and lowercase vowels (a, e, i, o, u).
Read string from stdin and print the count.""",
                "language": "python",
                "points": 10,
                "test_cases": [
                    {"input": "hello", "expected_output": "2"},
                    {"input": "Python Programming", "expected_output": "4"},
                    {"input": "xyz", "expected_output": "0"}
                ]
            },
            {
                "id": "q3",
                "title": "Check Palindrome",
                "description": """Write a Python function to check if a string is a palindrome.

Example:
Input: "madam"
Output: True

Input: "hello"
Output: False

Read string from stdin and print True or False.""",
                "language": "python",
                "points": 10,
                "test_cases": [
                    {"input": "madam", "expected_output": "True"},
                    {"input": "hello", "expected_output": "False"},
                    {"input": "racecar", "expected_output": "True"}
                ]
            }
        ],
        time_limit_minutes=30,
        difficulty="easy",
        tags=["Python", "Strings", "Beginner"]
    )
    print(f"✅ Created: {test1['test_id']}\n")

    # Test 2: Intermediate - Arrays and Math
    print("Creating Intermediate Test: Arrays and Math...")
    test2 = manager.create_test(
        title="Arrays and Math - Intermediate Level",
        description="Test your array manipulation and mathematical problem-solving skills",
        questions=[
            {
                "id": "q1",
                "title": "Sum of Array",
                "description": """Write a Python function that calculates the sum of numbers in an array.

Example:
Input: 1 2 3 4 5
Output: 15

Read space-separated integers from stdin and print the sum.""",
                "language": "python",
                "points": 15,
                "test_cases": [
                    {"input": "1 2 3 4 5", "expected_output": "15"},
                    {"input": "10 20 30", "expected_output": "60"},
                    {"input": "5", "expected_output": "5"}
                ]
            },
            {
                "id": "q2",
                "title": "Find Maximum",
                "description": """Write a Python function to find the maximum number in an array.

Example:
Input: 3 7 2 9 1
Output: 9

Read space-separated integers from stdin and print the maximum.""",
                "language": "python",
                "points": 15,
                "test_cases": [
                    {"input": "3 7 2 9 1", "expected_output": "9"},
                    {"input": "5 5 5", "expected_output": "5"},
                    {"input": "-3 -1 -5", "expected_output": "-1"}
                ]
            },
            {
                "id": "q3",
                "title": "Fibonacci Sequence",
                "description": """Write a Python function to generate the first n Fibonacci numbers.

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...

Example:
Input: 5
Output: 0 1 1 2 3

Read n from stdin and print space-separated Fibonacci numbers.""",
                "language": "python",
                "points": 20,
                "test_cases": [
                    {"input": "5", "expected_output": "0 1 1 2 3"},
                    {"input": "7", "expected_output": "0 1 1 2 3 5 8"},
                    {"input": "1", "expected_output": "0"}
                ]
            }
        ],
        time_limit_minutes=60,
        difficulty="medium",
        tags=["Python", "Arrays", "Math", "Algorithms"]
    )
    print(f"✅ Created: {test2['test_id']}\n")

    # Test 3: Advanced - Algorithms
    print("Creating Advanced Test: Algorithm Design...")
    test3 = manager.create_test(
        title="Algorithm Design - Advanced Level",
        description="Test your advanced algorithm design and optimization skills",
        questions=[
            {
                "id": "q1",
                "title": "Binary Search",
                "description": """Implement binary search to find an element in a sorted array.

Example:
Input Line 1: 1 3 5 7 9 (sorted array)
Input Line 2: 5 (target)
Output: 2 (index where 5 is found)

If not found, output: -1

Read two lines from stdin:
1. Space-separated sorted integers
2. Target integer to find

Print the index (0-based) or -1.""",
                "language": "python",
                "points": 25,
                "test_cases": [
                    {"input": "1 3 5 7 9\n5", "expected_output": "2"},
                    {"input": "2 4 6 8 10\n6", "expected_output": "2"},
                    {"input": "1 2 3 4 5\n10", "expected_output": "-1"}
                ]
            },
            {
                "id": "q2",
                "title": "Two Sum Problem",
                "description": """Find two numbers in an array that add up to a target sum.

Example:
Input Line 1: 2 7 11 15 (array)
Input Line 2: 9 (target)
Output: 0 1 (indices of 2 and 7)

Return indices in ascending order.
If no solution exists, output: -1 -1

Read two lines from stdin:
1. Space-separated integers
2. Target sum

Print two indices or -1 -1.""",
                "language": "python",
                "points": 30,
                "test_cases": [
                    {"input": "2 7 11 15\n9", "expected_output": "0 1"},
                    {"input": "3 2 4\n6", "expected_output": "1 2"},
                    {"input": "1 2 3\n10", "expected_output": "-1 -1"}
                ]
            },
            {
                "id": "q3",
                "title": "Longest Common Subsequence",
                "description": """Find the length of the longest common subsequence between two strings.

Example:
Input Line 1: "abcde"
Input Line 2: "ace"
Output: 3 (common: a, c, e)

Read two strings from stdin and print LCS length.""",
                "language": "python",
                "points": 45,
                "test_cases": [
                    {"input": "abcde\nace", "expected_output": "3"},
                    {"input": "abc\nabc", "expected_output": "3"},
                    {"input": "abc\ndef", "expected_output": "0"}
                ]
            }
        ],
        time_limit_minutes=90,
        difficulty="hard",
        tags=["Python", "Algorithms", "Data Structures", "Advanced"]
    )
    print(f"✅ Created: {test3['test_id']}\n")

    print("="*60)
    print("✅ Sample tests created successfully!")
    print("="*60)
    print("\nTest IDs:")
    print(f"1. Beginner: {test1['test_id']}")
    print(f"2. Intermediate: {test2['test_id']}")
    print(f"3. Advanced: {test3['test_id']}")
    print("\nYou can now view these tests in the Streamlit app!")
    print("Run: streamlit run app.py")
    print("Navigate to: Coding Tests page")

if __name__ == "__main__":
    create_sample_tests()
