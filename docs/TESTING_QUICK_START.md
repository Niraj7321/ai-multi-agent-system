# 🚀 Coding Tests - Quick Start Guide

## What You Can Do

✅ **Create coding tests** with multiple programming languages
✅ **Candidates take tests** and submit their code
✅ **Automatic evaluation** with test case validation
✅ **View detailed results** with feedback

---

## 1️⃣ Access the System

```bash
streamlit run app.py
```

Click on **"Coding Tests"** in the sidebar.

---

## 2️⃣ Try Sample Tests (Demo)

We've created 3 sample tests for you:

```bash
python create_sample_tests.py
```

**Sample Tests:**
- 📗 **Beginner**: String Operations (30 min, 30 points)
- 📘 **Intermediate**: Arrays and Math (60 min, 50 points)
- 📕 **Advanced**: Algorithm Design (90 min, 100 points)

---

## 3️⃣ Create Your First Test

### Navigate to "Create Test" Tab

**Basic Info:**
- Title: "Python Assessment"
- Description: "Test Python programming skills"
- Time Limit: 60 minutes
- Difficulty: medium

**Add a Question:**
- Title: "Reverse a String"
- Description: "Write a function to reverse a string"
- Language: Python
- Points: 10

**Add Test Cases:**
- Input: `hello` → Expected: `olleh`
- Input: `Python` → Expected: `nohtyP`

Click **"Create Test"** → Save the Test ID

---

## 4️⃣ Take a Test (As Candidate)

### Navigate to "Take Test" Tab

1. Select a test from dropdown
2. Click "Start Test"
3. Enter your name and email
4. Write code for each question
5. Click "Submit Test"
6. **Save your Submission ID!**

---

## 5️⃣ Check Results

### Navigate to "View Results" Tab

1. Enter your Submission ID
2. Click "Get Results"
3. View your score and feedback

---

## 6️⃣ Evaluate Submissions (As Admin)

### Navigate to "Evaluate Submissions" Tab

1. View all submissions
2. Click "Evaluate Now" for pending submissions
3. System automatically grades based on test cases
4. View detailed results

---

## 💻 Supported Languages

| Language   | Status | Requirement |
|------------|--------|-------------|
| Python     | ✅     | Built-in    |
| JavaScript | ✅     | Node.js     |
| Java       | ✅     | JDK         |
| C++        | ✅     | g++         |

### Install Requirements

**JavaScript:**
```bash
# Install Node.js from https://nodejs.org/
node --version  # Verify
```

**Java:**
```bash
# Install JDK from https://adoptium.net/
javac -version  # Verify
```

**C++:**
```bash
# Install MinGW from https://www.mingw-w64.org/
g++ --version  # Verify
```

---

## 📝 Example: Simple Question

### Question: Sum Two Numbers

**Description:**
```
Write a program that reads two integers and prints their sum.

Example:
Input: 5 10
Output: 15
```

**Test Cases:**
```
Input: 5 10     → Output: 15
Input: 100 200  → Output: 300
Input: -5 5     → Output: 0
```

**Python Solution:**
```python
numbers = input().split()
a, b = int(numbers[0]), int(numbers[1])
print(a + b)
```

---

## 🎯 Scoring System

```
Question Score = (Passed Tests / Total Tests) × Points
Total Score = Sum of Question Scores
Percentage = (Total Score / Max Score) × 100
Pass = Percentage ≥ 60%
```

**Example:**
- Question has 10 points
- 3 test cases
- You pass 2 test cases
- Your score: (2/3) × 10 = 6.67 points

---

## 📊 What Gets Evaluated

✅ **Correct Output**: Exact match with expected output
✅ **All Test Cases**: Hidden test cases included
✅ **Execution Time**: Must complete within timeout
✅ **No Errors**: Code must run without errors

---

## 🔧 Troubleshooting

### "Language not supported"
→ Install the required compiler/interpreter

### "Execution timeout"
→ Optimize your code, avoid infinite loops

### "Output mismatch"
→ Check exact format (spaces, newlines, data types)

### "Compilation error"
→ Check syntax and required imports

---

## 📂 Where Data is Stored

```
tests_data/
├── test_*.json              # Test definitions
├── submissions/
│   └── sub_*.json          # Candidate submissions
└── results/
    └── sub_*_result.json   # Evaluation results
```

---

## 🎓 Best Practices

### For Test Creators
1. Write clear problem statements
2. Provide examples
3. Add 3-5 test cases per question
4. Test edge cases

### For Test Takers
1. Read the problem carefully
2. Test your code with examples
3. Handle edge cases
4. Write clean, readable code

---

## 🚀 Quick Commands

**Run the app:**
```bash
streamlit run app.py
```

**Create sample tests:**
```bash
python create_sample_tests.py
```

**Check language installations:**
```bash
python --version
node --version
javac --version
g++ --version
```

---

## 📖 Full Documentation

For detailed documentation, see: **[CODING_TESTS.md](CODING_TESTS.md)**

---

## 🎉 You're Ready!

Start creating tests and assessing coding skills!

**Next Steps:**
1. Create your first test
2. Share the Test ID with candidates
3. Let them take the test
4. Evaluate and view results

**Need Help?** Check [CODING_TESTS.md](CODING_TESTS.md) for examples and detailed guides.
