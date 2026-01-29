# 📝 Coding Tests & Examinations System

Complete system for creating, administering, and evaluating coding tests and technical examinations.

## 🎯 Features

### For Test Creators
- ✅ Create custom coding tests with multiple questions
- ✅ Support for multiple programming languages (Python, JavaScript, Java, C++)
- ✅ Define test cases with input/output validation
- ✅ Set time limits and difficulty levels
- ✅ Automatic grading with detailed feedback
- ✅ Track submissions and results

### For Test Takers
- ✅ Take tests directly in the browser
- ✅ Write code in multiple languages
- ✅ Instant code execution and testing
- ✅ View detailed results with test case breakdowns
- ✅ Get feedback on each question

### For Evaluators
- ✅ Automatic evaluation with test case validation
- ✅ Detailed performance metrics
- ✅ Question-wise scoring
- ✅ Pass/fail determination
- ✅ Export results for analysis

---

## 🚀 Quick Start

### 1. Access the Testing System

Run the Streamlit app:
```bash
streamlit run app.py
```

Navigate to **"Coding Tests"** in the sidebar.

---

## 📋 Creating a Test

### Step-by-Step Guide

1. **Go to "Create Test" tab**

2. **Enter Test Details:**
   - **Title**: e.g., "Python Programming Assessment"
   - **Description**: What the test covers
   - **Time Limit**: Duration in minutes (5-180)
   - **Difficulty**: easy/medium/hard
   - **Tags**: Python, Algorithms, Data Structures (comma-separated)
   - **Passing Percentage**: Minimum score to pass (default: 60%)

3. **Add Questions:**
   - **Question Title**: Brief title (e.g., "Reverse a String")
   - **Description**: Detailed problem statement
   - **Language**: Python, JavaScript, Java, or C++
   - **Points**: Score for this question

4. **Define Test Cases:**
   - **Input**: What to provide to the code
   - **Expected Output**: What the code should return
   - Add multiple test cases for thorough validation

5. **Click "Create Test"**

You'll receive a **Test ID** that candidates can use to take the test.

---

## ✍️ Example Test Creation

### Example: "Fibonacci Sequence" Question

**Question Title:** Generate Fibonacci Sequence

**Description:**
```
Write a function that generates the first n numbers in the Fibonacci sequence.

The Fibonacci sequence starts with 0 and 1, and each subsequent number
is the sum of the previous two numbers.

Example: First 7 numbers: 0, 1, 1, 2, 3, 5, 8

Your function should accept one integer parameter 'n' and return a list.
```

**Language:** Python

**Points:** 20

**Test Cases:**

Test Case 1:
- Input: `5`
- Expected Output: `[0, 1, 1, 2, 3]`

Test Case 2:
- Input: `7`
- Expected Output: `[0, 1, 1, 2, 3, 5, 8]`

Test Case 3:
- Input: `1`
- Expected Output: `[0]`

---

## 📝 Taking a Test

### For Candidates

1. **Go to "Take Test" tab**

2. **Select a test** from the dropdown

3. **Click "Start Test"**

4. **Enter your details:**
   - Name
   - Email

5. **Solve each question:**
   - Read the problem description
   - Write your code in the provided editor
   - Test locally if needed

6. **Click "Submit Test"**

7. **Save your Submission ID** to check results later

---

## 📊 Viewing Results

### Check Your Score

1. **Go to "View Results" tab**

2. **Enter your Submission ID**
   - Format: `sub_test_1234567890_1234567890`

3. **Click "Get Results"**

### What You'll See:
- **Total Score**: Your points vs maximum points
- **Percentage**: Score as a percentage
- **Status**: PASSED or FAILED
- **Question-wise Results**:
  - Passed test cases
  - Expected vs actual output
  - Execution errors (if any)
  - Execution time

---

## 🎯 Evaluating Submissions

### For Evaluators

1. **Go to "Evaluate Submissions" tab**

2. **View all submissions:**
   - Candidate name and email
   - Test ID
   - Submission time
   - Evaluation status

3. **Click "Evaluate Now"** for pending submissions

4. **View Results:**
   - Automatic grading based on test cases
   - Detailed feedback per question
   - Pass/fail status

---

## 💻 Supported Languages

### Python
```python
def solution(n):
    # Your code here
    return result

print(solution(5))
```

### JavaScript
```javascript
function solution(n) {
    // Your code here
    return result;
}

console.log(solution(5));
```

### Java
```java
public class Solution {
    public static void main(String[] args) {
        // Your code here
        System.out.println(solution(5));
    }

    public static int solution(int n) {
        // Your code here
        return result;
    }
}
```

### C++
```cpp
#include <iostream>
using namespace std;

int solution(int n) {
    // Your code here
    return result;
}

int main() {
    cout << solution(5) << endl;
    return 0;
}
```

---

## 🔧 Language Requirements

### Python
✅ **Built-in** - No setup required

### JavaScript
Requires **Node.js**:
```bash
# Windows (using Chocolatey)
choco install nodejs

# Or download from: https://nodejs.org/
```

Verify installation:
```bash
node --version
```

### Java
Requires **JDK**:
```bash
# Windows (using Chocolatey)
choco install openjdk

# Or download from: https://adoptium.net/
```

Verify installation:
```bash
javac -version
java -version
```

### C++
Requires **g++** compiler:
```bash
# Windows (using Chocolatey)
choco install mingw

# Or download MinGW from: https://www.mingw-w64.org/
```

Verify installation:
```bash
g++ --version
```

---

## 📂 File Structure

```
tests_data/
├── test_1234567890.json          # Test definitions
├── submissions/
│   └── sub_test_1234567890.json  # Candidate submissions
└── results/
    └── sub_test_1234567890_result.json  # Evaluation results
```

---

## 🎓 Example Tests

### Beginner Level Tests

#### 1. **String Manipulation**
- Reverse a string
- Count vowels
- Check palindrome
- **Time**: 30 minutes
- **Points**: 30

#### 2. **Basic Math**
- Sum of array
- Find maximum
- Calculate factorial
- **Time**: 30 minutes
- **Points**: 30

### Intermediate Level Tests

#### 3. **Data Structures**
- Implement a stack
- Binary search
- Linked list operations
- **Time**: 60 minutes
- **Points**: 60

#### 4. **Algorithms**
- Sorting algorithms
- Fibonacci sequence
- Prime number checker
- **Time**: 60 minutes
- **Points**: 60

### Advanced Level Tests

#### 5. **Problem Solving**
- Dynamic programming
- Graph algorithms
- Tree traversals
- **Time**: 90 minutes
- **Points**: 100

---

## 🎯 Best Practices

### For Test Creators

1. **Clear Problem Statements**
   - Explain the problem thoroughly
   - Provide examples
   - Specify input/output format
   - Mention constraints

2. **Comprehensive Test Cases**
   - Test edge cases (empty input, single element, etc.)
   - Test normal cases
   - Test boundary values
   - Include at least 3-5 test cases per question

3. **Fair Scoring**
   - Allocate points based on difficulty
   - Easy questions: 10-20 points
   - Medium questions: 20-40 points
   - Hard questions: 40-60 points

4. **Reasonable Time Limits**
   - Simple tests: 30 minutes
   - Standard tests: 60 minutes
   - Complex tests: 90-120 minutes

### For Test Takers

1. **Read Carefully**
   - Understand the problem fully
   - Check input/output format
   - Note any constraints

2. **Test Your Code**
   - Verify with the examples provided
   - Think of edge cases
   - Check for syntax errors

3. **Time Management**
   - Don't spend too long on one question
   - Start with easier questions
   - Leave time for review

4. **Clean Code**
   - Write readable code
   - Use meaningful variable names
   - Add comments if helpful

---

## 📈 Evaluation System

### Automatic Grading

The system evaluates submissions by:

1. **Running your code** against test cases
2. **Comparing output** with expected output
3. **Calculating score** based on passed tests
4. **Generating feedback** for each question

### Scoring Formula

```
Question Score = (Passed Tests / Total Tests) × Question Points
Total Score = Sum of all Question Scores
Percentage = (Total Score / Maximum Score) × 100
```

### Pass/Fail Criteria

- **PASSED**: Percentage ≥ Passing Percentage (default: 60%)
- **FAILED**: Percentage < Passing Percentage

---

## 🔐 Security Features

### Code Execution Safety

- **Timeout Protection**: Code execution limited to 5 seconds
- **Isolated Environment**: Code runs in temporary files
- **Error Handling**: Compilation and runtime errors caught safely
- **No File System Access**: Restricted permissions

### Data Privacy

- All submissions stored locally
- No external code execution services
- Results accessible only via Submission ID

---

## 🛠️ Troubleshooting

### Code Not Running

**Problem:** "Language not supported" error

**Solution:**
- Ensure the compiler/interpreter is installed
- Check PATH environment variable
- Restart terminal after installation

### Timeout Errors

**Problem:** Code execution timeout

**Solution:**
- Optimize your code (avoid infinite loops)
- Reduce time complexity
- Check for unnecessary operations

### Output Mismatch

**Problem:** Test cases failing

**Solution:**
- Check exact output format (spaces, newlines)
- Verify data types
- Test with provided examples

### Compilation Errors

**Problem:** Java/C++ code won't compile

**Solution:**
- Check class name (Java: must match `public class`)
- Verify syntax
- Include necessary imports/headers

---

## 📊 Sample Test Results

### Example Result Output

```
====================================
TEST RESULTS
====================================

Candidate: John Doe (john@example.com)
Test: Python Programming Assessment
Submission ID: sub_test_1234567890_9876543210

OVERALL SCORE: 45/60 (75.0%)
STATUS: ✅ PASSED

------------------------------------
Question 1: Reverse a String (20/20)
✅ Passed 3/3 test cases

Test Case 1: ✅ PASSED
  Input: "hello"
  Expected: "olleh"
  Actual: "olleh"
  Time: 0.002s

Test Case 2: ✅ PASSED
  Input: "Python"
  Expected: "nohtyP"
  Actual: "nohtyP"
  Time: 0.001s

Test Case 3: ✅ PASSED
  Input: ""
  Expected: ""
  Actual: ""
  Time: 0.001s

------------------------------------
Question 2: Fibonacci Sequence (15/20)
✅ Passed 2/3 test cases

Test Case 1: ✅ PASSED
Test Case 2: ❌ FAILED
  Expected: [0, 1, 1, 2, 3, 5, 8]
  Actual: [0, 1, 1, 2, 3, 5]
Test Case 3: ✅ PASSED

------------------------------------
Question 3: Prime Number Checker (10/20)
✅ Passed 1/3 test cases

...
====================================
```

---

## 🔄 Workflow

### Complete Testing Workflow

1. **Create Test** → Test ID generated
2. **Share Test ID** → With candidates
3. **Candidates Take Test** → Submit answers
4. **Automatic Evaluation** → System grades submissions
5. **Review Results** → View detailed feedback
6. **Share Results** → Send Submission ID to candidates

---

## 💡 Tips & Tricks

### For Maximum Efficiency

1. **Pre-create Templates**: Save common question templates
2. **Reuse Test Cases**: Build a library of standard tests
3. **Batch Evaluation**: Evaluate multiple submissions at once
4. **Export Results**: Save JSON files for record-keeping

### For Better Assessment

1. **Mix Difficulties**: Include easy, medium, and hard questions
2. **Real-world Problems**: Use practical scenarios
3. **Multiple Solutions**: Accept different approaches
4. **Partial Credit**: Award points for passing some test cases

---

## 🆘 Support & FAQs

### Common Questions

**Q: Can I edit a test after creating it?**
A: Currently, tests are immutable. Create a new version if needed.

**Q: How long are results stored?**
A: Results are stored indefinitely in `tests_data/results/`.

**Q: Can candidates retake a test?**
A: Yes, they can submit multiple times with different Submission IDs.

**Q: What happens if code has infinite loops?**
A: Execution automatically times out after 5 seconds.

**Q: Can I export results to CSV/Excel?**
A: Results are stored as JSON. Use Python/Excel to convert.

**Q: Is internet required for code execution?**
A: No, all code runs locally on your machine.

---

## 📞 Quick Reference

### Key Commands

**Run Tests System:**
```bash
streamlit run app.py
# Navigate to "Coding Tests" page
```

**Check Language Installation:**
```bash
python --version
node --version
javac --version
g++ --version
```

### Important Paths

- Tests: `tests_data/test_*.json`
- Submissions: `tests_data/submissions/sub_*.json`
- Results: `tests_data/results/sub_*_result.json`

---

## 🎉 Ready to Start!

You now have a complete coding test system that can:
- Create professional assessments
- Execute code in multiple languages
- Automatically grade submissions
- Provide detailed feedback

**Start creating your first test and assess coding skills like a pro!** 🚀
