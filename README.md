# UBIT CGPA Calculator 📊

A simple and automated CGPA (Cumulative Grade Point Average) calculator specifically designed for **University of Balochistan Institute of Technology (UBIT) Computer Science Department** students.

## 🎯 Overview

This tool helps UBIT CS students calculate their CGPA based on the university's grading scale. You can use it locally on your computer or automatically through GitHub Actions whenever you update your marks.

## 📈 UBIT Grading Scale

The calculator uses the official UBIT grading scale:

| Marks Range | Grade | GPA Points |
| ----------- | ----- | ---------- |
| 85-100      | A     | 4.0        |
| 80-84       | A-    | 3.8        |
| 75-79       | B+    | 3.4        |
| 71-74       | B     | 3.0        |
| 68-70       | B-    | 2.8        |
| 64-67       | C+    | 2.4        |
| 61-63       | C     | 2.0        |
| 57-60       | C-    | 1.8        |
| 53-56       | D+    | 1.4        |
| 50-52       | D     | 1.0        |
| Below 50    | F     | 0.0        |

## 🚀 Quick Start

### Method 1: Local Usage

#### Prerequisites

- Python 3.7 or higher installed on your computer
- Basic knowledge of editing CSV files

#### Steps

1. **Clone or Download this repository:**

   ```bash
   git clone https://github.com/zawwar-ahmed/UBIT-CGPA-Calculator.git
   cd UBIT-CGPA-Calculator
   ```

2. **Update your marks in `marksheet.csv`:**

   - Open `marksheet.csv` in any text editor or spreadsheet application
   - Add your marks in the second column next to each subject
   - Save the file

   Example:

   ```csv
   Subject,Marks
   Introduction to Computer Science-I,85
   Mathematics-I,78
   Statistics-I,82
   ```

3. **Run the calculator:**

   ```bash
   python calculateCGPA.py
   ```

4. **View your CGPA:**
   The program will display your calculated CGPA in the terminal.

### Method 2: GitHub Actions (Automated)

#### Prerequisites

- A GitHub account
- Basic knowledge of forking repositories

#### Steps

1. **Fork this repository:**

   - Click the "Fork" button on the top-right of this repository
   - This creates your own copy of the calculator

2. **Update your marks:**

   - Go to your forked repository
   - Click on `marksheet.csv`
   - Click the pencil icon (Edit this file)
   - Add your marks in the Marks column
   - Scroll down and click "Commit changes"

3. **Automatic calculation:**
   - GitHub Actions will automatically run when you commit changes
   - Go to the "Actions" tab in your repository
   - Click on the latest workflow run
   - Expand "Calculate CGPA" to see your result

## 📝 CSV Format Guide

The `marksheet.csv` file contains all CS subjects from UBIT curriculum. Here's how to fill it:

### Complete Subject List (UBIT CS Curriculum)

The CSV includes all subjects from the 8-semester CS program:

**Semester 1-2 Foundation:**

- Introduction to Computer Science I & II
- Mathematics I & II
- Statistics I & II
- Physics I & II
- English I & II
- Islamiat, Pakistan Studies, Urdu

**Core CS Subjects:**

- Digital Computing and Design Fundamentals
- Assembly Language
- Object Oriented Programming
- Data Structures
- Software Engineering and Project Management
- Computer Architecture and Organization
- Database Management Systems
- Operating Systems
- And many more...

### How to Fill Your Marks

1. **Enter only numerical marks** (0-100) in the Marks column
2. **Leave empty** for subjects you haven't taken yet
3. **Use decimal points** if needed (e.g., 85.5)

Example:

```csv
Subject,Marks
Introduction to Computer Science-I,85
Mathematics-I,78.5
Statistics-I,
```

## 🔄 GitHub Actions Workflow

The repository includes an automated workflow that:

1. **Triggers on:**

   - Push to main branch
   - Pull request to main branch

2. **Automatically:**

   - Sets up Python environment
   - Runs the CGPA calculation
   - Displays results in the Actions log

3. **View Results:**
   - Go to Actions tab → Latest run → Calculate CGPA step

## 🛠️ Technical Details

### Files Structure

```
UBIT-CGPA-Calculator/
├── calculateCGPA.py      # Main calculation script
├── marksheet.csv         # Your marks data
├── .github/
│   └── workflows/
│       └── python-app.yml # GitHub Actions workflow
└── README.md            # This guide
```

### Algorithm

The calculator:

1. Reads marks from CSV file
2. Converts each mark to GPA points using UBIT scale
3. Calculates average GPA across all subjects
4. Returns CGPA rounded to 2 decimal places

## 🤝 Contributing

Feel free to contribute by:

- Adding new features
- Fixing bugs
- Improving documentation
- Adding semester-wise SGPA calculation

## 📞 Support

For UBIT CS students:

- Check with your academic advisor for official CGPA verification
- This tool is for estimation purposes
- Always refer to official university transcripts for formal records

## 📄 License

This project is open source and available under the MIT License.

---

**Made with ❤️ for UBIT CS Department Students**

_Calculate your CGPA, track your progress, achieve your goals!_
