# 🎨 Question Palette - Color-Coded Status

**© 2024 NrjAi | All Rights Reserved**

---

## ✅ Feature: Visual Question Palette

**Purpose:** Quick navigation and status overview for all 150 questions in the test.

**Location:** Sidebar during test-taking

---

## 🎨 Color Scheme

### Status Colors:

| Status | Color | Icon | Meaning |
|--------|-------|------|---------|
| 🟢 **Answered** | Green | ✓ | Question has been answered |
| 🟡 **Marked** | Yellow | 🔖 | Marked for review (may or may not be answered) |
| ⚪ **Not Visited** | Gray | - | Not visited yet |
| 🔵 **Current** | Blue Border | - | Currently viewing this question |

---

## 📊 Visual Layout

### Question Palette Grid:
```
┌─────────────────────────────────────────────┐
│ 📊 Question Palette                         │
│ 🟢 Green: Answered | 🟡 Yellow: Marked     │
│ ⚪ Gray: Not Visited                        │
├─────────────────────────────────────────────┤
│ [✓1] [✓2] [3] [4] [🔖5] [6] [7] [8] [9] [10]│
│ [11] [12] [13] [14] [15] [16] [17] [18] ... │
│ ...                                          │
└─────────────────────────────────────────────┘

✓1, ✓2 = Green (Answered)
🔖5 = Yellow (Marked for Review)
3, 4, 6-18 = Gray (Not Visited)
```

---

## 🎯 How It Works

### Status Determination:

**1. Answered (Green):**
```python
if question_id in st.session_state.answers:
    # Question has been answered
    color = GREEN
    label = "✓{number}"
```

**2. Marked for Review (Yellow):**
```python
elif question_id in st.session_state.marked_for_review:
    # Question marked (may or may not be answered)
    color = YELLOW
    label = "🔖{number}"
```

**3. Not Visited (Gray):**
```python
else:
    # Question not yet visited or answered
    color = GRAY
    label = "{number}"
```

**4. Current Question (Blue Border):**
```python
if question_id == current_question:
    border = "3px solid blue"
```

---

## 🖱️ Interaction

### Click Any Question Number:

**Action:** Navigate directly to that question

**Example:**
```
Currently on Question 5
Click "✓2" in palette
→ Jumps to Question 2
→ Shows previously saved answer
→ Blue border moves to Q2
```

---

## 📊 Status Examples

### Scenario 1: Start of Test
```
All questions: [1] [2] [3] [4] ... [150]
All Gray - None answered yet
Question 1 has blue border (current)
```

### Scenario 2: Answered 5 Questions
```
[✓1] [✓2] [✓3] [✓4] [✓5] [6] [7] ...
Green: 1-5 (answered)
Gray: 6+ (not visited)
Current: Question 6 (blue border)
```

### Scenario 3: Mixed Status
```
[✓1] [✓2] [3] [✓4] [🔖5] [✓6] [7] ...
✓1, ✓2, ✓4, ✓6 = Green (answered)
🔖5 = Yellow (marked for review)
3, 7+ = Gray (not visited)
```

### Scenario 4: Ready to Submit
```
All [✓1] [✓2] [✓3] ... [✓150]
All Green - All answered!
Metrics show: 150/150 answered (100%)
```

---

## 💡 Use Cases

### 1. Quick Navigation
**Scenario:** Want to review Question 42
**Action:** Click "42" in palette → Jumps there instantly

### 2. Find Unanswered
**Scenario:** Before submitting, find unanswered questions
**Action:** Look for gray numbers in palette

### 3. Review Marked Questions
**Scenario:** Review all questions marked with 🔖
**Action:** Look for yellow numbers, click to review

### 4. Check Progress
**Scenario:** How many questions completed?
**Action:** Count green numbers or check metrics below

---

## 🎨 Visual Design Details

### Color Values:

```css
/* Answered - Green */
background: #d4edda;
color: #28a745;
label: ✓{number}

/* Marked - Yellow */
background: #fff3cd;
color: #ffc107;
label: 🔖{number}

/* Not Visited - Gray */
background: #e9ecef;
color: #6c757d;
label: {number}

/* Current Question Border */
border: 3px solid #667eea;
```

### Button Layout:
```html
<div style="
    background: {status_color};
    border: {current_border};
    border-radius: 5px;
    padding: 0.3rem;
    text-align: center;
    font-weight: bold;">
    {label}
</div>
```

---

## 📱 Grid Layout

### Questions Per Row: 10

```
Row 1:  Q1-Q10
Row 2:  Q11-Q20
Row 3:  Q21-Q30
...
Row 15: Q141-Q150
```

**Total:** 15 rows for 150 questions

---

## 🔄 Real-Time Updates

### Auto-Updates When:

1. **Answer Selected:**
   - Question turns GREEN
   - Shows ✓ mark

2. **Mark for Review Clicked:**
   - Question turns YELLOW
   - Shows 🔖 mark

3. **Navigate to Question:**
   - Blue border moves to new question
   - Previous border removed

4. **Clear Selection:**
   - If was only marked: Stays yellow
   - If only answered: Turns gray (no answer)

---

## 📊 Summary Metrics

**Below Question Palette:**

```
┌──────────────┬──────────────┬─────────────────┐
│  Answered    │ Not Answered │ Marked for Rev. │
│    45        │     105      │       12        │
│    30%       │              │                 │
└──────────────┴──────────────┴─────────────────┘

⚠️ You have 105 unanswered questions!

         [📥 Submit Test]
```

---

## ✅ Testing Steps

### Test 1: Answer Questions
```
1. Start test
2. Answer Q1 → See [✓1] turn green
3. Answer Q2 → See [✓2] turn green
4. Check palette: 2 green, rest gray
```

### Test 2: Mark for Review
```
1. Go to Q5
2. Click "Mark for Review"
3. Check palette: [🔖5] turns yellow
```

### Test 3: Navigation
```
1. Currently on Q10
2. Click [✓2] in palette
3. Jumps to Q2
4. Blue border moves from Q10 to Q2
```

### Test 4: Mixed Status
```
1. Answer: Q1, Q2, Q4, Q6
2. Mark: Q3, Q5
3. Palette shows:
   - [✓1][✓2][🔖3][✓4][🔖5][✓6][7][8]...
   - Green for answered
   - Yellow for marked
   - Gray for not visited
```

---

## 🐛 Known Behaviors

### Marked + Answered:
If a question is both marked AND answered:
- Shows as GREEN (answered takes priority)
- Still in marked_for_review set
- Can unmark by clicking "Mark for Review" again

### Empty Answer:
If you clear an answer:
- Question goes from green to gray
- Removed from answers dictionary
- Stays in marked set if was marked

---

## 💻 Technical Implementation

### Key Variables:

```python
st.session_state.answers = {
    0: 'A',  # Q1 answered A
    1: 'B',  # Q2 answered B
    3: 'C',  # Q4 answered C
}

st.session_state.marked_for_review = {
    2,  # Q3 marked
    4,  # Q5 marked
}

st.session_state.current_question = 5  # Viewing Q6
```

### Color Logic:

```python
for q_num in range(150):
    if q_num in answers:
        # GREEN - Answered
        render_green(q_num)
    elif q_num in marked:
        # YELLOW - Marked
        render_yellow(q_num)
    else:
        # GRAY - Not visited
        render_gray(q_num)

    if q_num == current_question:
        # BLUE BORDER - Current
        add_blue_border()
```

---

## 🎯 User Benefits

### Easy Navigation:
✅ Jump to any question instantly
✅ No need to click Next 50 times
✅ Review specific questions quickly

### Status Overview:
✅ See at-a-glance what's done
✅ Find unanswered questions easily
✅ Track marked questions

### Progress Tracking:
✅ Visual progress indicator
✅ Count answered vs total
✅ Percentage complete

### Time Management:
✅ Skip difficult questions (mark)
✅ Come back later via palette
✅ Focus on unanswered first

---

## 📞 Summary

**Feature:** Question Palette with color-coded status
**Colors:** Green (answered), Yellow (marked), Gray (not visited)
**Layout:** 10 questions per row, 15 rows total
**Interaction:** Click any number to jump to that question
**Updates:** Real-time as you answer/mark questions

**Status:** ✅ WORKING WITH PROPER COLORS

---

**© 2024 NrjAi | All Rights Reserved**

**Date:** 2026-01-23
**Version:** 2.6 - Question Palette Enhancement
**Status:** ✅ ENHANCED WITH COLORS

---

**Try it now:**
```bash
streamlit run app.py
# Take any test and see the colorful question palette!
```

---

**The palette now shows proper GREEN, YELLOW, and GRAY colors!** 🎨✨
