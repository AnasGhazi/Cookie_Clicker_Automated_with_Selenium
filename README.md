# 🍪 Cookie Clicker Automated with Selenium

Automated testing script for the classic [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game using **Selenium WebDriver** and **pytest**.

This project simulates clicking the giant cookie and automates gameplay actions for a fixed duration.

---

## 🧪 Tech Stack

- [Selenium](https://pypi.org/project/selenium/)
- [pytest](https://docs.pytest.org/)
- [pytest-html](https://pypi.org/project/pytest-html/) (for generating test reports)
- Python 3.10+

---

## 📂 Project Structure

## 📂 Project Structure

cookieclicker/
├── test_cookie_clicker.py # Main test file using Selenium
├── conftest.py # Pytest fixture for browser setup
├── report.html # (Generated) Test report
└── README.md

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/AnasGhazi/Cookie_Clicker_Automated_with_Selenium.git
cd Cookie_Clicker_Automated_with_Selenium

### 2. Create and activate virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

### 3. Install dependencies
pip install selenium pytest pytest-html

### Run with HTML report:
bash
Copy
Edit
pytest test_cookie_clicker.py --html=report.html --self-contained-html

⚠️ CAPTCHA Note
The Cookie Clicker site sometimes triggers a CAPTCHA, which the script cannot bypass automatically. If it appears, close the browser and re-run the test.


