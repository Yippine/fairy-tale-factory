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
        setButotnEffects(itemPage);
        document.getElementById(`${itemPage}_button`).parentNode.addEventListener("click", function () {
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
        const button = document.getElementById(`${item_page}_button`);
        const create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
        const defaultText = getItemPageText(item_page);
        const text = create_story_page[item_page]?.item_name || defaultText;
        wrapTextWithSpans(text, button, "button_text");
        button.title = defaultText; // 使用 title 屬性顯示預設文字
    }

    function setButotnEffects(item_page) {
        const button = document.getElementById(`${item_page}_button`);
        const removeIcon = document.getElementById(`${item_page}_remove_icon`);
        const wrapText = button.dataset.text;
        const defaultText = button.title;
        const hasSelected = wrapText !== defaultText;
        if (hasSelected) {
            // 添加滑鼠滑過事件
            button.addEventListener('mouseenter', (event) => {
                wrapTextWithSpans(defaultText, button, "button_text");
                removeIcon.style.display = 'flex';
            });
            // 添加滑鼠離開事件
            button.addEventListener('mouseleave', (event) => {
                wrapTextWithSpans(wrapText, button, "button_text");
                removeIcon.style.display = 'none';
            });
        }
        // 為 X 圖標添加事件處理器
        removeIcon.addEventListener('click', function(event) {
            event.stopPropagation();
            button.textContent = defaultText; // 重置為預設文本
            removeIcon.style.display = 'none'; // 隱藏 X 圖標
            const create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
            var item_type = create_story_page[item_page];
            item_type.item_id = null;
            item_type.item_name = null;
            item_type.cover_design_link = null;
            sessionStorage.setItem("create_story_page", JSON.stringify(create_story_page));
        });
    }

    async function setItemPage(item_page) {
        const button = document.getElementById(`${item_page}_button`)
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        select_item_page.item_page = item_page;
        select_item_page.item_page_text = button.dataset.text;
        sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
        await sendDataToServer("/story/selectitem", { "select_item_page": select_item_page });
    }
}
