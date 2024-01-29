document.addEventListener("DOMContentLoaded", function () {
    var urlParams = new URLSearchParams(window.location.search);
    var page = parseInt(urlParams.get("page"), 10);
    if (isNaN(page) || page < 1) {
        window.location.href = "/story/storybookdisplay?page=1";
    } else if (page > 20) {
        window.location.href = "/story/storybookdisplay?page=20";
    } else {
        document.getElementById("page_no").innerHTML = "<h1>第 " + page + " 頁</h1>";
    }

    document.getElementsByClassName("group-12-bsJ")[0].addEventListener("click", function () {
        if (page < 20) {
            window.location.href = `/story/storybookdisplay?page=${page + 1}`;
        }
    });

    document.getElementsByClassName("group-13-Tx8")[0].addEventListener("click", function () {
        if (page > 1) {
            window.location.href = `/story/storybookdisplay?page=${page - 1}`;
        }
    });

    const togglePopUp = (popUpElement, otherPopUp) => {
        if (getComputedStyle(otherPopUp).display !== "none") {
            otherPopUp.style.display = "none";
        }
        popUpElement.style.display = popUpElement.style.display === "flex" ? "none" : "flex";
    };

    const saveButton = document.querySelector("#save_button");
    const homeButton = document.querySelector("#home_button");
    const savePopUp = document.querySelector("#save_pop_up");
    const homePopUp = document.querySelector("#home_pop_up");
    const saveSuccessfulPopUp = document.querySelector("#save_successful_pop_up");

    saveButton.addEventListener("click", function (event) {
        event.stopPropagation();
        togglePopUp(savePopUp, homePopUp);
    });

    homeButton.addEventListener("click", function (event) {
        event.stopPropagation();
        togglePopUp(homePopUp, savePopUp);
    });

    document.addEventListener("click", function (event) {
        if (!savePopUp.contains(event.target) && event.target !== saveButton) {
            savePopUp.style.display = "none";
        }
        if (!homePopUp.contains(event.target) && event.target !== homeButton) {
            homePopUp.style.display = "none";
        }
    });

    document.getElementById("check_home_button").addEventListener("click", function () {
        window.location.href = "/home";
    });

    document.getElementById("check_save_button").addEventListener("click", function () {
        savePopUp.style.display = "none";
        saveSuccessfulPopUp.style.display = "flex";
        setTimeout(function () {
            saveSuccessfulPopUp.style.display = "none";
        }, 1500);
    });
});
