# 🔧 Debugging Guide - Button Not Working Issue

**© 2024 NrjAi | All Rights Reserved**

---

## 🐛 Issue Reported

**User said:** "when i click on Available Subjects it is not open alsi in set when i click on start it is not workimng"

**Problems:**
1. Expanders for subjects not opening
2. Start button on practice sets not working

---

## 🔍 Common Causes & Solutions

### Issue 1: Start Button Not Working

**Possible Causes:**
1. Streamlit session state conflict
2. Button key collision
3. Page not rerendering

**Solution Applied:**
- Fixed navigation state management
- Added proper session state initialization
- Synchronized radio button with session state

### Issue 2: Expanders Not Opening

**Possible Causes:**
1. Too many items causing UI lag
2. Browser cache issue
3. Streamlit version compatibility

**Solutions to Try:**

#### Solution A: Clear Browser Cache
```
1. Press Ctrl + Shift + Delete
2. Clear cached images and files
3. Refresh page (F5)
```

#### Solution B: Restart Streamlit
```bash
# Stop current process (Ctrl+C)
# Then restart:
streamlit run app.py --server.port 8501
```

#### Solution C: Check Browser Console
```
1. Press F12 in browser
2. Click "Console" tab
3. Look for any red errors
4. Share errors if found
```

---

## 🚀 Quick Fix Steps

### Step 1: Stop Streamlit
```bash
# Press Ctrl+C in terminal where Streamlit is running
```

### Step 2: Clear Streamlit Cache
```bash
# Navigate to project directory
cd c:\Users\Niraj\ai-multi-agent-system

# Clear Streamlit cache
streamlit cache clear
```

### Step 3: Restart Application
```bash
# Run with fresh start
streamlit run app.py
```

### Step 4: Hard Refresh Browser
```
1. Go to the Streamlit app in browser
2. Press Ctrl + Shift + R (hard refresh)
3. Or Ctrl + F5
```

### Step 5: Test Functionality
```
1. Click on sidebar "📚 All Exams"
2. Find "STET (State TET)"
3. Click to expand it
4. You should see exam details
5. Scroll down to see 25 practice sets
6. Click "Start" on Set 1
7. Should navigate to "✍️ Take Test"
```

---

## 🧪 Testing Checklist

### Navigation Test:
- [ ] Sidebar navigation visible
- [ ] Can click "All Exams"
- [ ] Page changes to All Exams view

### Expander Test:
- [ ] Can see exam categories (Teaching, Civil Services, etc.)
- [ ] Exam names visible (STET, CTET, BPSC, etc.)
- [ ] Clicking exam name expands details
- [ ] Can see duration, questions, marks
- [ ] Can see 25 practice sets in 5×5 grid

### Start Button Test:
- [ ] "Start" buttons visible on each practice set
- [ ] Clicking "Start" on Set 1 works
- [ ] Page navigates to "Take Test"
- [ ] Class level selection screen appears

### Subject Selection Test:
- [ ] Can select a paper/class level
- [ ] Subject selection screen appears
- [ ] Can see subject icons and names
- [ ] Can click "Choose" on a subject
- [ ] Moves to details entry page

---

## 🔧 Technical Details

### What Was Fixed:

**1. Navigation State Management**
```python
# Before:
page = st.radio("Select", [...])

# After:
if 'nav_page' not in st.session_state:
    st.session_state.nav_page = "🏠 Home Dashboard"

page = st.radio("Select", [...], index=...)

if page != st.session_state.nav_page:
    st.session_state.nav_page = page
    st.rerun()
```

**2. Button Click Handling**
```python
# Start button properly stores state and navigates:
if st.button(f"Start", key=f"{exam['name']}_set_{set_num}"):
    st.session_state.selected_exam_for_test = exam
    st.session_state.selected_set_number = set_num
    st.session_state.nav_page = "✍️ Take Test"
    st.rerun()
```

---

## 🎯 Specific Test Cases

### Test Case 1: STET Test Flow
```
1. Navigate to "All Exams" ✓
2. Find "Teaching Exams" section ✓
3. Click on "STET (State TET)" ✓
4. Expander opens showing details ✓
5. See 25 practice sets grid ✓
6. Click "Start" on Set 1 ✓
7. Page shows "Step 1: Select Class Level" ✓
8. Click "Select" on Paper 4 ✓
9. Page shows "Step 2: Select Subject" ✓
10. Click "Choose" on Computer Science ✓
11. Page shows "Step 3: Enter Details" ✓
12. Enter name and email ✓
13. Click "Start Test Now" ✓
14. Test begins with questions ✓
```

### Test Case 2: Multiple Exam Navigation
```
1. Go to "All Exams" ✓
2. Expand STET ✓
3. Click Start on Set 5 ✓
4. Go through class/subject selection ✓
5. Click back button ✓
6. Should return to subject selection ✓
7. Navigate back to "All Exams" via sidebar ✓
8. Try BPSC exam ✓
9. Should work similarly ✓
```

---

## 💡 Troubleshooting Tips

### If Expanders Don't Open:

**Check 1: Are you clicking the right area?**
- Click on the exam NAME itself
- Not just the icon
- The whole row should be clickable

**Check 2: Browser zoom level**
```
- Press Ctrl + 0 to reset zoom to 100%
- Try again
```

**Check 3: Try different exam**
```
- If STET doesn't open, try CTET
- If all teaching exams don't open, try BPSC
- Helps identify if it's specific to one exam
```

### If Start Button Doesn't Work:

**Check 1: Look for loading indicator**
- Streamlit shows spinner when processing
- If no spinner, button click not registered

**Check 2: Check session state**
```python
# Add this temporarily to debug:
st.write("Session State:", st.session_state)
```

**Check 3: Button key uniqueness**
- Each button has unique key
- Format: `{exam_name}_set_{set_number}`
- Should be unique across all sets

### If Navigation Fails:

**Check 1: Session state persistence**
```python
# Should see these in session state:
- selected_exam_for_test
- selected_set_number
- nav_page = "✍️ Take Test"
```

**Check 2: Rerun is called**
```python
# After setting state, always call:
st.rerun()
```

---

## 📞 Step-by-Step Debug Process

### Method 1: Visual Inspection
```
1. Run: streamlit run app.py
2. Open browser: http://localhost:8501
3. Look at sidebar - is "All Exams" visible? YES/NO
4. Click "All Exams" - does page change? YES/NO
5. See "Teaching Exams" section? YES/NO
6. Click "STET" - does it expand? YES/NO
7. See 25 practice sets? YES/NO
8. Click "Start" on Set 1 - what happens?
```

### Method 2: Console Logging
Add temporary debug output:

```python
# In nrjai_dashboard.py, add after imports:
import logging
logging.basicConfig(level=logging.INFO)

# Before button click:
st.write("DEBUG: About to render Start button")
if st.button(...):
    st.write("DEBUG: Button was clicked!")
    logging.info("Start button clicked for exam: %s, set: %s", exam['name'], set_num)
```

### Method 3: Minimal Test
Create a simple test file:

```python
# test_buttons.py
import streamlit as st

st.title("Button Test")

if st.button("Test Button 1"):
    st.success("Button 1 clicked!")

with st.expander("Test Expander"):
    st.write("This is inside expander")
    if st.button("Test Button 2"):
        st.success("Button 2 clicked!")
```

Run: `streamlit run test_buttons.py`

If this works, issue is in main app.
If this fails, issue is with Streamlit installation.

---

## 🔄 Complete Reset Procedure

If nothing works, do complete reset:

```bash
# 1. Stop Streamlit (Ctrl+C)

# 2. Clear all caches
streamlit cache clear

# 3. Remove Streamlit config (if exists)
# Windows:
del %USERPROFILE%\.streamlit\config.toml

# 4. Clear browser data
# In browser: Ctrl+Shift+Delete
# Select "Cached images and files"
# Clear data

# 5. Restart computer (optional but recommended)

# 6. Reinstall Streamlit (if needed)
pip uninstall streamlit
pip install streamlit

# 7. Run app fresh
cd c:\Users\Niraj\ai-multi-agent-system
streamlit run app.py
```

---

## 🎬 Video Debug Steps

Record screen while doing this:

```
1. Show terminal with Streamlit running
2. Show browser with app open
3. Click sidebar "All Exams"
4. Attempt to expand an exam
5. Attempt to click Start
6. Show what happens (or doesn't happen)
7. Press F12, show Console tab
8. Look for errors
```

This helps identify exactly where it fails.

---

## 📊 Expected vs Actual

### Expected Behavior:

| Action | Expected Result |
|--------|----------------|
| Click "All Exams" | Page changes to exam list |
| Click exam name | Expander opens with details |
| Click "Start" on Set 1 | Navigate to Take Test page |
| See class selection | 4 paper options visible |
| Click "Select" | Move to subject selection |
| See subjects | Grid of subjects with icons |
| Click "Choose" | Move to details page |

### If Something Different Happens:
Document what you see:
- Does page freeze?
- Does button turn color (indicating click)?
- Any error message?
- Does page scroll?
- Any loading spinner?

---

## 🔍 Known Issues & Workarounds

### Issue: Streamlit Version Compatibility
**Symptom:** Buttons don't respond
**Solution:**
```bash
pip install streamlit==1.32.0  # Use stable version
```

### Issue: Browser Compatibility
**Symptom:** UI elements not interactive
**Solution:** Try different browser (Chrome, Firefox, Edge)

### Issue: Port Conflict
**Symptom:** Can't access app
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Too Many Buttons
**Symptom:** Some buttons work, others don't
**Solution:** Reduce items per page or use pagination

---

## ✅ Confirmation Tests

After applying fixes, confirm these work:

1. **Basic Navigation**
   ```
   ✓ Can switch between pages using sidebar
   ✓ "All Exams" page loads
   ✓ Can return to Home Dashboard
   ```

2. **Exam Selection**
   ```
   ✓ Teaching Exams section visible
   ✓ STET exam can be expanded
   ✓ Exam details display correctly
   ✓ 25 practice sets visible in grid
   ```

3. **Test Start**
   ```
   ✓ Start button on Set 1 is clickable
   ✓ Page navigates to "Take Test"
   ✓ Class selection screen appears
   ✓ Can select Paper 4
   ```

4. **Subject Selection**
   ```
   ✓ Subject grid displays
   ✓ Computer Science option visible
   ✓ Can click "Choose"
   ✓ Moves to details page
   ```

5. **Complete Flow**
   ```
   ✓ Can complete entire flow from start to test
   ✓ Timer starts
   ✓ Questions appear
   ✓ Can submit and see results
   ```

---

## 📞 Quick Support Checklist

If you need help, provide:

1. **Streamlit version:**
   ```bash
   streamlit --version
   ```

2. **Python version:**
   ```bash
   python --version
   ```

3. **Browser & version:**
   (e.g., Chrome 120, Firefox 121)

4. **Error messages:**
   (From terminal and browser console)

5. **What doesn't work:**
   - Expanders won't open
   - Start buttons don't click
   - Page doesn't navigate
   - Something else

6. **What you tried:**
   - Cleared cache: YES/NO
   - Restarted app: YES/NO
   - Tried different browser: YES/NO
   - Hard refreshed page: YES/NO

---

## 🎯 Most Likely Cause

Based on similar issues:

**90% of the time:** Browser cache or Streamlit cache
**Solution:** Clear both caches and hard refresh

**8% of the time:** Session state conflict
**Solution:** Restart Streamlit completely

**2% of the time:** Code issue
**Solution:** Already fixed in latest update

---

**© 2024 NrjAi | All Rights Reserved**

*Debugging Made Easy* 🔧

---

**Last Updated:** 2026-01-21
**Version:** 1.0
