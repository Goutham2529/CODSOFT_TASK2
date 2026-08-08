document.addEventListener("DOMContentLoaded", function () {

    // =========================================
    // FILE ELEMENTS
    // =========================================

    const fileInput =
        document.getElementById("fileInput");

    const dropArea =
        document.getElementById("dropArea");

    const selectedFile =
        document.getElementById("selectedFile");


    // =========================================
    // FILE DISPLAY
    // =========================================

    function showSelectedFile(file) {

        if (!selectedFile || !file) {
            return;
        }

        selectedFile.innerHTML =
            '<i class="fa-solid fa-file-csv"></i> ' +
            file.name;

    }


    // =========================================
    // FILE VALIDATION
    // =========================================

    function validateFile(file) {

        if (!file) {
            return false;
        }

        const fileName =
            file.name.toLowerCase();

        if (!fileName.endsWith(".csv")) {

            alert(
                "⚠️ Please select a CSV file only."
            );

            return false;

        }

        return true;

    }


    // =========================================
    // FILE INPUT
    // =========================================

    if (fileInput) {

        fileInput.addEventListener(
            "change",
            function () {

                const file =
                    this.files[0];

                if (!validateFile(file)) {

                    this.value = "";

                    if (selectedFile) {

                        selectedFile.innerHTML =
                            "No file selected";

                    }

                    return;

                }

                showSelectedFile(file);

            }
        );

    }


    // =========================================
    // DRAG & DROP
    // =========================================

    if (dropArea) {

        [
            "dragenter",
            "dragover"
        ].forEach(function (eventName) {

            dropArea.addEventListener(
                eventName,
                function (event) {

                    event.preventDefault();

                    event.stopPropagation();

                    dropArea.classList.add(
                        "dragover"
                    );

                }
            );

        });


        [
            "dragleave",
            "drop"
        ].forEach(function (eventName) {

            dropArea.addEventListener(
                eventName,
                function (event) {

                    event.preventDefault();

                    event.stopPropagation();

                    dropArea.classList.remove(
                        "dragover"
                    );

                }
            );

        });


        dropArea.addEventListener(
            "drop",
            function (event) {

                const files =
                    event.dataTransfer.files;

                if (!files.length) {
                    return;
                }

                const file =
                    files[0];

                if (!validateFile(file)) {
                    return;
                }


                /*
                 * DataTransfer is used so the
                 * dropped file is submitted
                 * with the form.
                 */

                const dataTransfer =
                    new DataTransfer();

                dataTransfer.items.add(file);

                fileInput.files =
                    dataTransfer.files;

                showSelectedFile(file);

            }
        );

    }


    // =========================================
    // AUTO HIDE ALERTS
    // =========================================

    setTimeout(function () {

        document
            .querySelectorAll(".alert")
            .forEach(function (alert) {

                alert.style.transition =
                    "opacity .5s ease, transform .5s ease";

                alert.style.opacity = "0";

                alert.style.transform =
                    "translateY(-10px)";

                setTimeout(function () {

                    alert.remove();

                }, 500);

            });

    }, 3500);


    // =========================================
    // TABLE SEARCH
    // =========================================

    const searchInput =
        document.querySelector(
            'input[name="q"]'
        );


    if (searchInput) {

        searchInput.addEventListener(
            "input",
            function () {

                const searchValue =
                    this.value
                        .trim()
                        .toLowerCase();

                const rows =
                    document.querySelectorAll(
                        "tbody tr"
                    );


                rows.forEach(function (row) {

                    const rowText =
                        row.innerText
                            .toLowerCase();

                    if (
                        rowText.includes(
                            searchValue
                        )
                    ) {

                        row.style.display = "";

                    } else {

                        row.style.display =
                            "none";

                    }

                });

            }
        );

    }


    // =========================================
    // CARD ANIMATION
    // =========================================

    const cards =
        document.querySelectorAll(
            ".dashboard-card, .info-card"
        );


    cards.forEach(function (card, index) {

        card.style.animationDelay =
            (index * 0.08) + "s";

    });


    // =========================================
    // PREVENT DOUBLE SUBMIT
    // =========================================

    const uploadForm =
        document.querySelector(
            'form[action="/upload"]'
        );


    if (uploadForm) {

        uploadForm.addEventListener(
            "submit",
            function (event) {

                if (
                    !fileInput ||
                    !fileInput.files.length
                ) {

                    event.preventDefault();

                    alert(
                        "⚠️ Please select a CSV file first."
                    );

                    return;

                }


                const submitButton =
                    uploadForm.querySelector(
                        'button[type="submit"]'
                    );


                if (submitButton) {

                    submitButton.disabled =
                        true;

                    submitButton.innerHTML =
                        '<i class="fa-solid fa-spinner fa-spin"></i> ' +
                        'Processing CSV...';

                }

            }
        );

    }


    // =========================================
    // SMOOTH SCROLL
    // =========================================

    document
        .querySelectorAll(
            'a[href^="#"]'
        )
        .forEach(function (link) {

            link.addEventListener(
                "click",
                function (event) {

                    const target =
                        document.querySelector(
                            this.getAttribute("href")
                        );

                    if (target) {

                        event.preventDefault();

                        target.scrollIntoView({
                            behavior: "smooth"
                        });

                    }

                }
            );

        });

});