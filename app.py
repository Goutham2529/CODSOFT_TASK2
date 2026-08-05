from flask import Flask, render_template, request, redirect, flash, session, send_file
import csv
import json
import os

app = Flask(__name__)
app.secret_key = "goutham123"

DATA_FILE = "records.json"
UPLOAD_FOLDER = "uploads"

USERNAME = "admin"
PASSWORD = "admin123"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


def load_records():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_records(records):
    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)


@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    records = load_records()

    total_records = session.get("total_records", len(records))
    unique_records = session.get("unique_records", len(records))
    duplicates_removed = session.get("duplicates_removed", 0)

    return render_template(
        "index.html",
        records=records,
        total_records=total_records,
        unique_records=unique_records,
        duplicates_removed=duplicates_removed
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username
            flash("Login Successful!")

            return redirect("/")

        flash("Invalid Username or Password!")

        return redirect("/login")

    return render_template("login.html")


@app.route("/download-sample")
def download_sample():

    sample_file = os.path.join(app.root_path, "sample.csv")

    return send_file(sample_file, as_attachment=True)


@app.route("/upload", methods=["POST"])
def upload():

    if "user" not in session:
        return redirect("/login")

    if "file" not in request.files:
        flash("Please choose a CSV file.")
        return redirect("/")

    file = request.files["file"]

    if file.filename == "":
        flash("Please choose a CSV file.")
        return redirect("/")

    if not file.filename.lower().endswith(".csv"):
        flash("Only CSV files are allowed.")
        return redirect("/")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    records = load_records()

    existing_emails = {r["email"].lower() for r in records}
    existing_phones = {r["phone"] for r in records}

    csv_emails = set()
    csv_phones = set()

    total_uploaded = 0
    duplicates_removed = 0
    unique_records = 0

    with open(filepath, "r", encoding="utf-8") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            name = row.get("Name", "").strip()
            email = row.get("Email", "").strip().lower()
            phone = row.get("Phone", "").strip()

            if not name or not email or not phone:
                continue

            total_uploaded += 1

            if (
                email in existing_emails
                or phone in existing_phones
                or email in csv_emails
                or phone in csv_phones
            ):
                duplicates_removed += 1
                continue

            records.append({
                "name": name,
                "email": email,
                "phone": phone
            })

            existing_emails.add(email)
            existing_phones.add(phone)

            csv_emails.add(email)
            csv_phones.add(phone)

            unique_records += 1

    save_records(records)

    session["total_records"] = total_uploaded
    session["unique_records"] = unique_records
    session["duplicates_removed"] = duplicates_removed

    flash(
        f"Upload Complete! "
        f"Uploaded: {total_uploaded} | "
        f"Unique: {unique_records} | "
        f"Duplicates: {duplicates_removed}"
    )

    return redirect("/")
@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully!")

    return redirect("/login")


@app.route("/delete/<email>")
def delete(email):

    if "user" not in session:
        return redirect("/login")

    records = load_records()

    records = [
        record
        for record in records
        if record["email"] != email
    ]

    save_records(records)

    flash("Record Deleted Successfully!")

    return redirect("/")


@app.route("/reset")
def reset():

    if "user" not in session:
        return redirect("/login")

    save_records([])

    session["total_records"] = 0
    session["unique_records"] = 0
    session["duplicates_removed"] = 0

    flash("All records deleted successfully!")

    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)