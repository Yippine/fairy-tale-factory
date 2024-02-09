const default_select_item = {
    item_page: "",
    story_info: {
        main_role: { item_id: "", item_name: "", cover_design_link: "" },
        sup_role: { item_id: "", item_name: "", cover_design_link: "" },
        item: { item_id: "", item_name: "", cover_design_link: "" },
    },
};

document.addEventListener("DOMContentLoaded", function () {
    setButtonText();
    document.getElementById("create_button").addEventListener("click", () => redirectTo("/story/loading"));
    document.getElementById("go_home_button").addEventListener("click", () => redirectTo("/home"));
    ["main_role", "sup_role", "item"].forEach(function (itemPage) {
        document.getElementById(itemPage + "_button").addEventListener("click", function () {
            setItemPage(itemPage);
        });
    });
});

function setButtonText() {
    const buttons = {
        main_role: document.getElementById("main_role_button_text"),
        sup_role: document.getElementById("sup_role_button_text"),
        item: document.getElementById("item_button_text"),
    };
    const select_item = JSON.parse(sessionStorage.getItem("select_item")) || default_select_item;
    console.log(`select_item:`, select_item);
    const setButtonText = (button, name) => {
        button.innerHTML =
            name ? name :
            button.id === buttons.main_role.id ? "主角" :
            button.id === buttons.sup_role.id ? "配角" :
            button.id === buttons.item.id ? "道具" :
            "";
    };
    setButtonText(buttons.main_role, select_item.story_info.main_role.item_name);
    setButtonText(buttons.sup_role, select_item.story_info.sup_role.item_name);
    setButtonText(buttons.item, select_item.story_info.item.item_name);
}

function setItemPage(item_page) {
    const select_item = JSON.parse(sessionStorage.getItem("select_item")) || default_select_item;
    select_item.item_page = item_page;
    sessionStorage.setItem("select_item", JSON.stringify(select_item));

    fetch("/story/setselectitemnew/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ select_item: select_item }),
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
