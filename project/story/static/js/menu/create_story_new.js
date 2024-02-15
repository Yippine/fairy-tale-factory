document.addEventListener("DOMContentLoaded", function () {
    initialSession();
    initialButtons();
});

function initialSession() {
    const data = document.getElementById("item-data");
    var select_item_page = data.dataset.selectItemPage;
    var create_story_page = data.dataset.createStoryPage;
    sessionStorage.setItem("select_item_page", select_item_page);
    sessionStorage.setItem("create_story_page", create_story_page);
}

function initialButtons() {
    document.getElementById("go_home_button").addEventListener("click", () => redirectTo("/home"));
    document.getElementById("create_button").addEventListener("click", loading);
    ["main_role", "sup_role", "item"].forEach(function (itemPage) {
        setButtonText(itemPage);
        document.getElementById(itemPage + "_button").parentNode.addEventListener("click", function () {
            setItemPage(itemPage);
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

    function setButtonText(item_page) {
        const button = document.getElementById(item_page + "_button");
        var create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
        var text = create_story_page[item_page].item_name;
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

    async function setItemPage(item_page) {
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        select_item_page.item_page = item_page;
        sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
        await sendDataToServer("/story/selectitem", { "select_item_page": select_item_page });
    }
}
