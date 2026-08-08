from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    session,
    send_file,
    jsonify
)

import csv
import json
import os
from datetime import datetime


# ==========================================
# FLASK APPLICATION
# ==========================================

app = Flask(__name__)

app.secret_key = "goutham123"


# ==========================================
# CONFIGURATION
# ==========================================

DATA_FILE = "records.json"

UPLOAD_FOLDER = "uploads"

USERNAME = "admin"

PASSWORD = "admin123"

ALLOWED_EXTENSION = ".csv"


# ==========================================
# CREATE UPLOAD FOLDER
# ==========================================

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ==========================================
# CREATE DATABASE FILE
# ==========================================

if not os.path.exists(DATA_FILE):

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            [],
            file
        )


# ==========================================
# LOAD RECORDS
# ==========================================

def load_records():

    try:

        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


            if isinstance(data, list):

                return data


            return []


    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return []


# ==========================================
# SAVE RECORDS
# ==========================================

def save_records(records):

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================
# LOGIN CHECK
# ==========================================

def login_required():

    return "user" in session


# ==========================================
# FILE VALIDATION
# ==========================================

def allowed_file(filename):

    return (

        "." in filename

        and

        filename.lower().endswith(
            ALLOWED_EXTENSION
        )

    )


# ==========================================
# NORMALIZE CSV RECORD
# ==========================================

def normalize_record(row):

    cleaned = {}


    for key, value in row.items():

        if key is None:

            continue


        clean_key = (
            str(key)
            .strip()
            .lower()
        )


        clean_value = (
            str(value)
            .strip()
        )


        cleaned[clean_key] = clean_value


    return cleaned
# ==========================================
# DUPLICATE DETECTION
# ==========================================

def is_duplicate(record, existing_records):

    email = record.get(
        "email",
        ""
    ).strip().lower()

    phone = record.get(
        "phone",
        ""
    ).strip()


    for existing in existing_records:

        existing_email = existing.get(
            "email",
            ""
        ).strip().lower()

        existing_phone = existing.get(
            "phone",
            ""
        ).strip()


        # ==================================
        # SAME EMAIL
        # ==================================

        if email and existing_email:

            if email == existing_email:

                return True


        # ==================================
        # SAME PHONE
        # ==================================

        if phone and existing_phone:

            if phone == existing_phone:

                return True


    return False


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

def get_statistics():

    records = load_records()


    total_records = len(records)


    unique_emails = set()

    unique_phones = set()


    for record in records:

        email = record.get(
            "email",
            ""
        ).strip().lower()


        phone = record.get(
            "phone",
            ""
        ).strip()


        if email:

            unique_emails.add(
                email
            )


        if phone:

            unique_phones.add(
                phone
            )


    return {

        "total_records":
            total_records,

        "unique_records":
            total_records,

        "unique_emails":
            len(unique_emails),

        "unique_phones":
            len(unique_phones)

    }


# ==========================================
# LOGIN
# ==========================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()


        password = request.form.get(
            "password",
            ""
        ).strip()


        if (
            username == USERNAME
            and
            password == PASSWORD
        ):

            session["user"] = username

            session["duplicates"] = 0

            flash(
                "Login successful!",
                "success"
            )

            return redirect("/")


        flash(
            "Invalid username or password.",
            "danger"
        )


    return render_template(
        "login.html"
    )


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        "/login"
    )


# ==========================================
# HOME / DASHBOARD
# ==========================================

@app.route("/")
def index():

    if not login_required():

        return redirect(
            "/login"
        )


    records = load_records()

    stats = get_statistics()


    return render_template(

        "index.html",

        records=records,

        total_records=
            stats["total_records"],

        unique_records=
            stats["unique_records"],

        unique_emails=
            stats["unique_emails"],

        unique_phones=
            stats["unique_phones"],

        duplicates_removed=
            session.get(
                "duplicates",
                0
            ),

        search_query=""

    )


# ==========================================
# SAMPLE CSV
# ==========================================

@app.route("/sample")
def sample_csv():

    if not login_required():

        return redirect(
            "/login"
        )


    sample_path = os.path.join(
        UPLOAD_FOLDER,
        "sample.csv"
    )


    sample_data = [

        {
            "name": "Rahul",
            "email": "rahul@gmail.com",
            "phone": "9876543210"
        },

        {
            "name": "Priya",
            "email": "priya@gmail.com",
            "phone": "9876543211"
        },

        {
            "name": "Arjun",
            "email": "arjun@gmail.com",
            "phone": "9876543212"
        }

    ]


    with open(

        sample_path,

        "w",

        newline="",

        encoding="utf-8"

    ) as file:

        writer = csv.DictWriter(

            file,

            fieldnames=[
                "name",
                "email",
                "phone"
            ]

        )

        writer.writeheader()

        writer.writerows(
            sample_data
        )


    return send_file(

        sample_path,

        as_attachment=True,

        download_name="sample.csv"

    )
# ==========================================
# CSV UPLOAD & DEDUPLICATION
# ==========================================

@app.route(
    "/upload",
    methods=["POST"]
)
def upload_file():

    if not login_required():

        return redirect(
            "/login"
        )


    # ======================================
    # CHECK FILE
    # ======================================

    if "file" not in request.files:

        flash(
            "Please select a CSV file.",
            "danger"
        )

        return redirect("/")


    file = request.files["file"]


    if file.filename == "":

        flash(
            "No file selected.",
            "danger"
        )

        return redirect("/")


    # ======================================
    # CHECK EXTENSION
    # ======================================

    if not allowed_file(
        file.filename
    ):

        flash(
            "Only CSV files are allowed.",
            "danger"
        )

        return redirect("/")


    # ======================================
    # SAVE UPLOADED FILE
    # ======================================

    filename = (
        datetime.now()
        .strftime("%Y%m%d_%H%M%S_")
        +
        file.filename
    )


    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )


    file.save(file_path)


    # ======================================
    # LOAD EXISTING RECORDS
    # ======================================

    existing_records = load_records()

    new_records = []

    duplicates = 0


    # ======================================
    # READ CSV
    # ======================================

    try:

        with open(

            file_path,

            "r",

            newline="",

            encoding="utf-8-sig"

        ) as csv_file:


            reader = csv.DictReader(
                csv_file
            )


            if not reader.fieldnames:

                flash(
                    "CSV file is empty.",
                    "danger"
                )

                return redirect("/")


            # ==================================
            # PROCESS EVERY ROW
            # ==================================

            for row in reader:


                record = normalize_record(
                    row
                )


                # ------------------------------
                # SKIP EMPTY ROW
                # ------------------------------

                if not any(
                    value.strip()
                    for value in record.values()
                    if isinstance(
                        value,
                        str
                    )
                ):

                    continue


                # ------------------------------
                # CHECK DUPLICATE
                # ------------------------------

                records_to_check = (

                    existing_records
                    +
                    new_records

                )


                if is_duplicate(

                    record,

                    records_to_check

                ):

                    duplicates += 1

                    continue


                # ------------------------------
                # ADD NEW RECORD
                # ------------------------------

                new_records.append(
                    record
                )


    except Exception as error:

        flash(
            f"Error processing CSV: {error}",
            "danger"
        )

        return redirect("/")


    # ======================================
    # SAVE NEW RECORDS
    # ======================================

    existing_records.extend(
        new_records
    )


    save_records(
        existing_records
    )


    # ======================================
    # SAVE DUPLICATE COUNT
    # ======================================

    session["duplicates"] = duplicates


    # ======================================
    # LAST UPLOAD INFORMATION
    # ======================================

    session["last_upload"] = {

        "filename":
            file.filename,

        "time":
            datetime.now()
            .strftime(
                "%d-%m-%Y %I:%M %p"
            ),

        "added":
            len(new_records),

        "duplicates":
            duplicates

    }


    # ======================================
    # SUCCESS MESSAGE
    # ======================================

    flash(

        f"Upload completed! "
        f"{len(new_records)} new records added "
        f"and {duplicates} duplicates removed.",

        "success"

    )


    # ======================================
    # DELETE TEMPORARY UPLOAD
    # ======================================

    try:

        os.remove(
            file_path
        )

    except OSError:

        pass


    return redirect("/")


# ==========================================
# SEARCH RECORDS
# ==========================================

@app.route("/search")
def search():

    if not login_required():

        return redirect(
            "/login"
        )


    query = request.args.get(
        "q",
        ""
    ).strip().lower()


    records = load_records()


    if query:

        filtered_records = []


        for record in records:

            record_text = " ".join(

                str(value)

                for value in record.values()

            ).lower()


            if query in record_text:

                filtered_records.append(
                    record
                )


        records = filtered_records


    stats = get_statistics()


    return render_template(

        "index.html",

        records=records,

        total_records=
            stats["total_records"],

        unique_records=
            stats["unique_records"],

        unique_emails=
            stats["unique_emails"],

        unique_phones=
            stats["unique_phones"],

        duplicates_removed=
            session.get(
                "duplicates",
                0
            ),

        search_query=query

    )
# ==========================================
# DELETE SINGLE RECORD
# ==========================================

@app.route(
    "/delete/<int:index>"
)
def delete_record(index):

    if not login_required():

        return redirect(
            "/login"
        )


    records = load_records()


    if index < 0 or index >= len(records):

        flash(
            "Record not found.",
            "danger"
        )

        return redirect("/")


    deleted_record = records.pop(
        index
    )


    save_records(
        records
    )


    name = deleted_record.get(
        "name",
        "Record"
    )


    flash(
        f"{name} deleted successfully.",
        "success"
    )


    return redirect("/")


# ==========================================
# CLEAR ALL RECORDS
# ==========================================

@app.route("/reset")
def reset_records():

    if not login_required():

        return redirect(
            "/login"
        )


    save_records([])


    session["duplicates"] = 0


    session.pop(
        "last_upload",
        None
    )


    flash(
        "All records have been cleared.",
        "success"
    )


    return redirect("/")


# ==========================================
# EXPORT CLEANED CSV
# ==========================================

@app.route("/download")
def download_csv():

    if not login_required():

        return redirect(
            "/login"
        )


    records = load_records()


    if not records:

        flash(
            "No records available to export.",
            "warning"
        )

        return redirect("/")


    export_path = os.path.join(

        UPLOAD_FOLDER,

        "cleaned_records.csv"

    )


    # Collect all possible columns

    fieldnames = []

    for record in records:

        for key in record.keys():

            if key not in fieldnames:

                fieldnames.append(key)


    with open(

        export_path,

        "w",

        newline="",

        encoding="utf-8"

    ) as file:

        writer = csv.DictWriter(

            file,

            fieldnames=fieldnames

        )


        writer.writeheader()


        for record in records:

            writer.writerow(record)


    return send_file(

        export_path,

        as_attachment=True,

        download_name="cleaned_records.csv"

    )


# ==========================================
# API - DASHBOARD STATISTICS
# ==========================================

@app.route("/api/stats")
def api_stats():

    if not login_required():

        return jsonify({

            "success": False,

            "message": "Unauthorized"

        }), 401


    stats = get_statistics()


    return jsonify({

        "success": True,

        "total_records":
            stats["total_records"],

        "unique_records":
            stats["unique_records"],

        "unique_emails":
            stats["unique_emails"],

        "unique_phones":
            stats["unique_phones"],

        "duplicates_removed":
            session.get(
                "duplicates",
                0
            )

    })


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health")
def health():

    return jsonify({

        "status": "online",

        "application":
            "Cloud Data Deduplication System",

        "timestamp":
            datetime.now()
            .isoformat()

    })


# ==========================================
# APPLICATION START
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )