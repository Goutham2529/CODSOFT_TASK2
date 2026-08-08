# ☁️ Cloud Data Deduplication System

A premium web-based **Cloud Data Deduplication System** built using Python Flask.

This application allows users to upload CSV files, automatically detect duplicate records using Email or Phone Number, remove duplicates, and download the cleaned dataset.

---

## 🚀 Features

- 📤 CSV File Upload
- 🔍 Automatic Duplicate Detection
- 📧 Email-based Duplicate Detection
- 📱 Phone Number-based Duplicate Detection
- 📊 Premium Dashboard
- 🔎 Search Records
- 🗑️ Delete Individual Records
- 🧹 Clear All Records
- 📥 Download Cleaned CSV
- 📄 Download Sample CSV
- 🔐 Login Authentication
- 📈 Record Statistics
- 🖱️ Drag & Drop CSV Upload
- 📱 Responsive Design
- ✨ Premium Animations
- 🩺 Application Health Check

---

## 🧠 Duplicate Detection

The system identifies a record as a duplicate when either the email address or phone number already exists.

| Email | Phone | Result |
|---|---|---|
| Same | Different | ❌ Duplicate |
| Different | Same | ❌ Duplicate |
| Same | Same | ❌ Duplicate |
| Different | Different | ✅ New Record |

### Example

```text
Rahul   rahul@gmail.com   9876543210
Arjun   arjun@gmail.com   9876543210

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JSON
- CSV

---

## 📂 Project Structure

```
cloud-data-deduplication/
│
├── app.py
├── records.json
├── sample.csv
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── static/
│   └── style.css
|   └── script.js
│
├── templates/
│   ├── login.html
│   └── index.html
│
└── uploads/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Goutham2529/CODSOFT_TASK2.git
```

Move into the project folder

```bash
cd CODSOFT_TASK2
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

## 🔑 Login Credentials

**Username**

```
admin
```

**Password**

```
admin123
```

---

## 📊 Dashboard

The dashboard displays:

- Total Uploaded Records
- Unique Records
- Duplicate Records Removed
- Unique Emails

---

## 📸 Screenshots

### 🔐 Login Page

<img width="1909" height="910" alt="login" src="https://github.com/user-attachments/assets/4fc12048-d643-4ef7-9e28-40f813d1fde9" />

### 📊 Dashboard

<img width="1879" height="909" alt="dashboard" src="https://github.com/user-attachments/assets/c0e1c2cc-0712-445d-9021-1133bd2e8432" />

### 📤 Upload CSV

<img width="1870" height="625" alt="upload csv" src="https://github.com/user-attachments/assets/817812e3-25ea-4543-b18d-b8df32010241" />

### 📋 Stored Records

<img width="1850" height="493" alt="stored records" src="https://github.com/user-attachments/assets/a88329a3-46ec-42d4-866c-fa0e942c33e4" />


## 🌐 Live Demo

https://codsoft-task2-e9wj.onrender.com

---

## 👨‍💻 Developed By

Goutham

CodSoft Cloud Computing Internship – Task 2
