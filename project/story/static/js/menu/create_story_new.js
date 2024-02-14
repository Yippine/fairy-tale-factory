const defaultSelectItem = {
    item_page: "",
    story_info: {
        main_role: { item_id: "", item_name: "", cover_design_link: "" },
        sup_role: { item_id: "", item_name: "", cover_design_link: "" },
        item: { item_id: "", item_name: "", cover_design_link: "" },
    },
};

document.addEventListener("DOMContentLoaded", function () {
    const selectItem = JSON.parse(sessionStorage.getItem("select_item")) || defaultSelectItem;
    console.log(`selectItem:`, selectItem);

    document.getElementById("create_button").addEventListener("click", loading);
    document.getElementById("go_home_button").addEventListener("click", () => redirectTo("/home"));

    ["main_role", "sup_role", "item"].forEach(function (itemPage) {
        setButtonText(selectItem, itemPage);
        document.getElementById(itemPage + "_button").parentNode.addEventListener("click", function () {
            setItemPage(itemPage);
        });
    });
});

function loading() {
    const popupMessageContainer = document.getElementById("popup_container_without_button");
    const popupMessage = document.getElementById("popup_message_without_button");
    popupMessageContainer.style.display = "flex";
    var loadingTime = 1; // 加載時間為 1 秒
    setTimeout(function () {
        popupMessage.textContent = "即將為你呈現";
        setTimeout(function () {
            window.location.href = "/story/storybookdisplay?page=1"; // 跳轉到 storybook_display.html 的第一頁
        }, 1000); // 延遲 1 秒後跳轉
    }, loadingTime * 1000);
}

function redirectTo(path) {
    window.location.href = `${path}`;
}

function setButtonText(select_item, item_page) {
    const button = document.getElementById(item_page + "_button");
    var text = select_item.story_info[item_page].item_name;
    if (!text) {
        switch (button.id) {
            case "main_role_button":
                text = "請選擇主角";
                break;
            case "sup_role_button":
                text = "請選擇配角";
                break;
            case "item_button":
                text = "請選擇道具";
                break;
            default:
                text = "";
        }
    }
    const chars = text.split("");
    chars.forEach((char) => {
        const span = document.createElement("span");
        span.className = "button_text";
        span.innerText = char;
        button.appendChild(span);
    });
}

function setItemPage(item_page) {
    const select_item = JSON.parse(sessionStorage.getItem("select_item")) || defaultSelectItem;
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
}
