☁️ Cloud Data Deduplication System

A premium web-based Cloud Data Deduplication System built using Python Flask.

This application allows users to upload CSV files, automatically detect duplicate records using Email or Phone Number, remove duplicates, and download the cleaned dataset.

🚀 Features
📤 CSV File Upload
🔍 Automatic Duplicate Detection
📧 Email-based Duplicate Detection
📱 Phone Number-based Duplicate Detection
📊 Premium Dashboard
🔎 Search Records
🗑️ Delete Individual Records
🧹 Clear All Records
📥 Download Cleaned CSV
📄 Download Sample CSV
🔐 Login Authentication
📈 Record Statistics
🖱️ Drag & Drop CSV Upload
📱 Responsive Design
✨ Premium Animations
🩺 Application Health Check
🧠 Duplicate Detection

The system identifies a record as a duplicate when either the email address or phone number already exists.

Email	Phone	Result
Same	Different	❌ Duplicate
Different	Same	❌ Duplicate
Same	Same	❌ Duplicate
Different	Different	✅ New Record
Example

Rahul — rahul@gmail.com — 9876543210

Arjun — arjun@gmail.com — 9876543210

The second record is detected as a duplicate because the phone number already exists.

🛠️ Technologies Used
Python
Flask
HTML5
CSS3
JavaScript
Bootstrap 5
Font Awesome
JSON
CSV
Git
GitHub
📂 Project Structure

cloud-data-deduplication/

├── app.py
├── records.json
├── requirements.txt
├── README.md
│
├── templates/
│ ├── index.html
│ └── login.html
│
├── static/
│ ├── style.css
│ └── script.js
│
└── uploads/

🔐 Demo Login

Username: admin

Password: admin123

▶️ How to Run
1. Clone the repository

git clone https://github.com/Goutham2529/CODSOFT_TASK2.git

2. Open the project folder

cd CODSOFT_TASK2

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open in browser

http://127.0.0.1:5000

🔄 Application Workflow

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
↓
Skip Duplicate / Save New Record
↓
Clean Dataset
↓
Download CSV

📊 Dashboard

The dashboard provides:

Total Records
Unique Records
Duplicates Removed
Unique Emails
Searchable Records
Record Management
🔍 Record Management

Users can:

Search records
Delete individual records
Clear all records
Export cleaned records
Download sample CSV files
🔮 Future Enhancements
☁️ Cloud database integration
🔐 Secure authentication
👥 Multiple user accounts
📊 Advanced analytics
📈 Data visualization
🗄️ PostgreSQL / MongoDB integration
🔗 Cloud storage integration
⚡ Background CSV processing
🎯 Internship Task

Internship: CODSOFT Cloud Computing Internship

Task: Cloud Data Deduplication System

Project Type: Web Application

Technology: Python Flask

👨‍💻 Project

Cloud Data Deduplication System

Developed as part of the CODSOFT Cloud Computing Internship.

⭐ Acknowledgement

This project was developed as part of the CODSOFT internship task requirements.

📄 License

This project is created for educational and internship purposes.
