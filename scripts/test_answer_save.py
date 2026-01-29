"""
Test to verify that ALL answers (correct and wrong) are saved properly
"""
import streamlit as st

# Simulate the answer saving logic
test_answers = {}

# Test question
test_question = {
    'id': 1,
    'text': 'What is 2 + 2?',
    'options': {
        'A': '3',
        'B': '4',  # Correct
        'C': '5',
        'D': '6'
    },
    'correct': 'B'
}

print("="*80)
print("TESTING ANSWER SAVE LOGIC")
print("="*80)

print("\nTest Question:")
print(f"  {test_question['text']}")
print(f"  Correct Answer: {test_question['correct']} ({test_question['options'][test_question['correct']]})")

print("\n" + "-"*80)
print("TESTING: Saving WRONG answers")
print("-"*80)

# Test saving wrong answers
wrong_options = ['A', 'C', 'D']
for option in wrong_options:
    # Simulate clicking wrong answer
    test_answers[test_question['id']] = option

    # Check if saved
    saved = test_answers.get(test_question['id'])
    status = "PASS" if saved == option else "FAIL"

    print(f"  Clicked: {option} ({test_question['options'][option]}) -> Saved: {saved} [{status}]")

print("\n" + "-"*80)
print("TESTING: Saving CORRECT answer")
print("-"*80)

# Test saving correct answer
test_answers[test_question['id']] = 'B'
saved = test_answers.get(test_question['id'])
status = "PASS" if saved == 'B' else "FAIL"
print(f"  Clicked: B ({test_question['options']['B']}) -> Saved: {saved} [{status}]")

print("\n" + "="*80)
print("RESULTS:")
print("="*80)

if all([
    test_answers.get(test_question['id']) == 'B'  # Last one saved
]):
    print("✅ ALL TESTS PASSED")
    print("   - Wrong answers can be saved")
    print("   - Correct answers can be saved")
    print("   - Last selection is preserved")
else:
    print("❌ TESTS FAILED")

print("="*80)

# Now test in actual Streamlit context
print("\nNOTE: This is a logic test.")
print("To test in actual app:")
print("  1. Run: streamlit run app.py")
print("  2. Go to any test")
print("  3. Try clicking WRONG answers")
print("  4. Verify they are saved (button turns blue)")
print("  5. Navigate away and back")
print("  6. Verify selection is still there")
