document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("create_button").addEventListener("click", () => redirectTo("/story/loading"));
    document.getElementById("go_home_button").addEventListener("click", () => redirectTo("/home"));

    ["main_role", "sup_role", "item"].forEach(function (itemType) {
        document.getElementById(itemType + "_button").addEventListener("click", function () {
            setItemType(itemType);
        });
    });

    function setItemType(itemType) {
        fetch("/story/setitemtypenew/", {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ item_type: itemType }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log("Success:", data);
                redirectTo("/story/selectitem");
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function redirectTo(path) {
        window.location.href = `${path}`;
    }
});
