# ☁️ Cloud Data Deduplication System

A premium web-based **Cloud Data Deduplication System** built using **Python Flask**.

This application allows users to upload CSV files, automatically detect duplicate records using **Email or Phone Number**, remove duplicates, and download the cleaned dataset.

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

## 🧠 Duplicate Detection

A record is considered a duplicate when **either the email address or phone number already exists**.

| Email | Phone | Result |
|---|---|---|
| Same | Different | ❌ Duplicate |
| Different | Same | ❌ Duplicate |
| Same | Same | ❌ Duplicate |
| Different | Different | ✅ New Record |

### Example

| Name | Email | Phone | Result |
|---|---|---|---|
| Rahul | rahul@gmail.com | 9876543210 | ✅ New |
| Arjun | arjun@gmail.com | 9876543210 | ❌ Duplicate |

The second record is detected as a duplicate because the phone number already exists.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome
- JSON
- CSV
- Git
- GitHub

## 📂 Project Structure

```text
cloud-data-deduplication/
│
├── app.py
├── records.json
├── requirements.txt
├── README.md
├── runtime.txt
├── sample.csv
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/
```

## 🔐 Demo Login

**Username:** `admin`

**Password:** `admin123`

> For production deployment, credentials should be stored securely using environment variables.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Goutham2529/CODSOFT_TASK2.git
```

### 2. Open the project folder

```bash
cd CODSOFT_TASK2
```

### 3. Create and activate a virtual environment (optional)

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

## 🔄 Application Workflow

```text
User Login
    ↓
Premium Dashboard
    ↓
Upload CSV
    ↓
Read CSV Records
    ↓
Normalize Data
    ↓
Check Email / Phone
    ↓
Duplicate?
   ↙     ↘
 YES      NO
  ↓        ↓
Skip     Save
  ↓        ↓
  └──→ Clean Dataset
            ↓
      Download CSV
```

## 📊 Dashboard

The premium dashboard provides:

- Total Records
- Unique Records
- Duplicates Removed
- Unique Emails
- Unique Phone Numbers
- Searchable Records
- Record Management
- CSV Export

## 🔍 Record Management

Users can:

- Search records
- Delete individual records
- Clear all records
- Export cleaned records
- Download a sample CSV
- Upload new CSV datasets

## 📸 Screenshots

Create a `screenshots` folder in the project and add the following images:

```text
screenshots/
├── login.png
├── dashboard.png
├── upload.png
├── records.png
└── duplicates.png
```

### 🔐 Premium Login Page

![Premium Login Page](screenshots/login.png)

### 📊 Premium Dashboard

![Premium Dashboard](screenshots/dashboard.png)

### 📤 CSV Upload

![CSV Upload](screenshots/upload.png)

### 🔍 Records & Search

![Records and Search](screenshots/records.png)

### 📈 Duplicate Detection

![Duplicate Detection](screenshots/duplicates.png)

## ☁️ Cloud Deployment

The Flask application can be deployed on cloud platforms such as:

- Render
- Railway
- PythonAnywhere

The project includes `requirements.txt` and `runtime.txt` for deployment support.

## 🎯 Internship Task

**Internship:** CODSOFT Cloud Computing Internship

**Task:** Cloud Data Deduplication System

**Project Type:** Web Application

**Technology:** Python Flask

## 🔮 Future Enhancements

- ☁️ Cloud database integration
- 🔐 Secure authentication
- 👥 Multiple user accounts
- 📊 Advanced analytics
- 📈 Data visualization
- 🗄️ PostgreSQL / MongoDB integration
- 🔗 Cloud storage integration
- ⚡ Background CSV processing
- 🔔 Upload notifications
- 📋 Detailed duplicate reports

## 👨‍💻 Project

**Cloud Data Deduplication System**

Developed as part of the **CODSOFT Cloud Computing Internship**.

## ⭐ Acknowledgement

This project was developed as part of the CODSOFT internship task requirements.

## 📄 License

This project is created for educational and internship purposes.
