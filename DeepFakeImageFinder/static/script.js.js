// ===============================
// DeepFake Image Finder
// JavaScript
// ===============================

console.log("DeepFake Image Finder Loaded");

document.addEventListener("DOMContentLoaded", function () {

    const fileInput = document.querySelector("input[type='file']");
    const previewContainer = document.querySelector(".preview");

    if (fileInput) {

        fileInput.addEventListener("change", function () {

            if (this.files && this.files[0]) {

                const reader = new FileReader();

                reader.onload = function (e) {

                    if (previewContainer) {

                        previewContainer.innerHTML = `
                            <h2>Selected Image</h2>
                            <img src="${e.target.result}"
                                 style="
                                 width:300px;
                                 border-radius:10px;
                                 border:3px solid #1565C0;
                                 margin-top:15px;
                                 ">
                        `;

                    }

                };

                reader.readAsDataURL(this.files[0]);

            }

        });

    }

});

function showLoading() {

    const button = document.querySelector("button");

    if (button) {

        button.innerHTML = "Detecting...";

        button.disabled = true;

    }

}