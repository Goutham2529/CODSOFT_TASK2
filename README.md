# ☁️ Cloud Data Deduplication System

A premium web-based **Cloud Data Deduplication System** developed using **Python Flask**.

The application allows users to upload CSV files, automatically detect duplicate records using **Email or Phone Number**, remove duplicates, and download the cleaned dataset.

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
- 📱 Responsive UI
- ✨ Premium Animations
- 🩺 Application Health Check

---

## 🧠 Duplicate Detection Logic

The system considers a record as a duplicate when:

| Condition | Result |
|---|---|
| Same Email | ❌ Duplicate |
| Same Phone Number | ❌ Duplicate |
| Same Email + Same Phone | ❌ Duplicate |
| Different Email + Different Phone | ✅ New Record |

### Example

```text
Rahul   rahul@gmail.com   9876543210
Arjun   arjun@gmail.com   9876543210

The second record is detected as a duplicate because the phone number is already present.
