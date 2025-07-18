# 🔐 File Integrity Checker

A Python project to detect any changes in file content using hashing (SHA256). Useful for checking if a file has been tampered with.

---

## 📁 Files Used
- `file_integrity_checker.py` - The main code
- `testfile.txt` - Sample file for testing
- `notes.docx` - Another test file
- `hashes.json` - Stores original file hashes
- `README.md` - Project explanation

---

## 🧠 How It Works
1. Saves hash values of selected files using SHA256
2. Later compares current file hashes with saved ones
3. Detects and reports if any file is changed

---

## 📸 Screenshots

### 1. Full Python Code in VS Code)
![image alt](https://github.com/nikhithavadlamudi-cyber/fileintegritychecker/blob/4cb1cb77f990632a5ad7f4996e4e8e68cc7df288/code_part1.png)

![image alt](https://github.com/nikhithavadlamudi-cyber/fileintegritychecker/blob/b614e4b0ebd56b87f1efcfb4269abaca6d0068ea/code_part2.png)

![image alt](https://github.com/nikhithavadlamudi-cyber/fileintegritychecker/blob/18e798133079dc53dcf0909cfe2519306cc6c282/code_part3.png)

---

### 2. Output in Terminal (Detects Changes)
![image alt](https://github.com/nikhithavadlamudi-cyber/fileintegritychecker/blob/cfa74ad0914b948f5ad87930ade65c2f64f9936d/output_screenshot.png)

---

### 3. File List in Project Explorer
![image alt](https://github.com/nikhithavadlamudi-cyber/fileintegritychecker/blob/130a3b4b2167354e5aae7f320eeca7c69836a8af/explorer_screenshot.png)

---

## 🚀 How to Use

```python
files_to_check = ['testfile.txt', 'notes.docx']
save_hashes(files_to_check)      # Saves file hashes
compare_hashes(files_to_check)   # Checks if files changed
