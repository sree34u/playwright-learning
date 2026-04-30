# 🎭 Playwright Learning Sandbox (Python + Pytest)

This repository is a personal learning space for practicing browser automation using **Playwright with Python** and **Pytest**. It contains experimental scripts, test cases, and small automation scenarios built while exploring Playwright features.

---

## 📌 Purpose

- Learn and experiment with Playwright automation  
- Practice writing test cases using Pytest  
- Explore browser interactions, selectors, and assertions  
- Build a strong foundation in end-to-end (E2E) testing  

---

## 🧰 Tech Stack

- **Language:** Python  
- **Automation Tool:** Playwright  
- **Test Framework:** Pytest  
- **Environment:** Sandbox / Practice Setup  

---

## 📁 Project Structure


playwright-learning/
│
├── tests/ # Test scripts using Pytest
│ ├── test_example.py
│ ├── test_login.py
│ └── ...
│
├── pages/ # Page Object Models (optional)
│ ├── base_page.py
│ └── login_page.py
│
├── utils/ # Helper functions/utilities
│
├── conftest.py # Pytest fixtures & setup
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd playwright-learning
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
3. Install Dependencies
pip install -r requirements.txt
4. Install Playwright Browsers
playwright install
🚀 Running Tests

Run all tests:

pytest

Run tests with verbose output:

pytest -v

Run a specific test file:

pytest tests/test_example.py

Run tests in headed mode:

pytest --headed
🧪 Sample Features Covered
Page navigation
Element locators (CSS, XPath, text)
Assertions
Form handling
Screenshots & tracing
Fixtures and test setup
Page Object Model (POM) basics
📚 Learning Notes

This repo may include:

Trial-and-error scripts
Experimental code snippets
Notes and quick examples

Expect frequent changes and non-production-ready code.

🤝 Contributions

This is a personal learning repository, but suggestions and improvements are welcome.

📄 License

This project is for educational purposes.