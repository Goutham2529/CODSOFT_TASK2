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

    total_records = len(records)
    unique_records = len(records)
    duplicates_removed = session.get("duplicates", 0)

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


@app.route("/logout")
def logout():

    session.pop("user", None)

    flash("Logged Out Successfully!")

    return redirect("/login")


@app.route("/download-sample")
def download_sample():

    sample_file = os.path.join(app.root_path, "sample.csv")

    return send_file(
        sample_file,
        as_attachment=True
    )


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

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    records = load_records()

    existing_emails = set()

    existing_phones = set()

    for record in records:

        existing_emails.add(
            record["email"].lower()
        )

        existing_phones.add(
            record["phone"]
        )

    csv_emails = set()

    csv_phones = set()

    duplicates = 0

    new_records = 0

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            name = row.get("Name", "").strip()
            email = row.get("Email", "").strip().lower()
            phone = row.get("Phone", "").strip()

            if not name or not email or not phone:
                continue

            if (
                email in existing_emails
                or phone in existing_phones
                or email in csv_emails
                or phone in csv_phones
            ):

                duplicates += 1
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

            new_records += 1

    save_records(records)

    session["duplicates"] = duplicates

    flash(
        f"Upload Complete! "
        f"Saved: {new_records} | "
        f"Duplicates Removed: {duplicates}"
    )

    return redirect("/")


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

    flash("All records deleted successfully!")

    return redirect("/")


if __name__ == "__main__":

    app.run(debug=True)

