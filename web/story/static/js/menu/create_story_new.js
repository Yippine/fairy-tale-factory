document.addEventListener("DOMContentLoaded", function () {
    initialSession();
    initialButtons();
});

function initialSession() {
    const pageData = document.getElementById("page-data");
    var select_item_page = pageData.dataset.selectItemPage;
    var create_story_page = pageData.dataset.createStoryPage;
    sessionStorage.setItem("select_item_page", select_item_page);
    sessionStorage.setItem("create_story_page", create_story_page);
}

function initialButtons() {
    const goHomeButton = document.getElementById("go_home_button");
    const createButton = document.getElementById("create_button");
    const showCommandButton = document.getElementById("show_command_button");
    const popupCommandRemoveIco = document.getElementById("popup_command_remove_icon"); /* X按鈕 */
    goHomeButton.addEventListener("click", () => redirectTo("/home"));
    createButton.addEventListener("click", () => checkItems());
    showCommandButton.addEventListener("click", () => showCommand());
    ["main_role", "sup_role", "item"].forEach(function (itemPage) {
        setButtonText(itemPage);
        setButotnEffects(itemPage);
        document.getElementById(`${itemPage}_button`).parentNode.addEventListener("click", function () {
            setItemPage(itemPage);
        });
    });
    function closePopupCommandContainer() {
        const popupMessageContainer = document.getElementById("popup_command_container");
        popupMessageContainer.style.display = "none";
        clearTimeout(timeout); // 清除計時器以避免再次自動關閉
    }
    popupCommandRemoveIco.addEventListener("click", () => closePopupCommandContainer());

    function checkItems() {
        const itemButtonContainers = Array.from(document.querySelectorAll(".item_button_container"));
        const popupMessageContainer = document.getElementById("popup_container_without_button");
        const popupLoadingContainer = document.getElementById("popup_loading_container");
        const loadingEarth = document.getElementById("loading_earth");
        const popupMessage = document.getElementById("popup_message_without_button");
        const popupLoadingMessage = document.getElementById("popup_loading_message");
        const errorMessage = checkErrorMessage();
        if (errorMessage) {
            showErrorMessage();
        } else {
            loading();
        }

        function checkErrorMessage() {
            const create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
            const mainRole = create_story_page.main_role;
            const supRole = create_story_page.sup_role;
            // 檢查是否選擇主角
            if (!mainRole || !mainRole.item_id) {
                return "請至少選擇一位主角！";
            }
            // 檢查主角、配角是否相同
            if (mainRole.item_id === supRole.item_id) {
                return "主角、配角不得重複！";
            }
            if (mainRole.item_name && supRole.item_name) {
                // 移除角色名稱中的括號
                mainRole.item_name = removeParentheses(mainRole.item_name);
                supRole.item_name = removeParentheses(supRole.item_name);
                // 檢查主角、配角是否為同一人物
                if (mainRole.item_name === supRole.item_name) {
                    return "角色不得為同一人！";
                }
            }

            function removeParentheses(s) {
                return s.includes("（") ? s.substring(0, s.indexOf("（")) : s;
            }
        }

        function showErrorMessage() {
            popupMessage.textContent = errorMessage;
            loadingEarth.style.display = "none";
            itemButtonContainers.forEach((element) => {
                element.style.opacity = "1";
            });
            showFTFMessage(popupMessageContainer, 3000);
        }

        function loading() {
            popupLoadingMessage.textContent = "高效生成中...";
            loadingEarth.style.display = "flex";
            itemButtonContainers.forEach((element) => {
                element.style.opacity = "0";
            });
            popupLoadingContainer.style.display = "flex";
            var loadingTime = 1; // 加載時間為 1 秒
            setTimeout(function () {
                popupLoadingMessage.textContent = "即將為你呈現";
                setTimeout(function () {
                    window.location.href = "/story/storybookdisplay?page=1"; // 跳轉到 storybook_display.html 的第一頁
                }, 1000); // 延遲 1 秒後跳轉
            }, loadingTime * 1000);
        }
    }

    function showCommand() {
        const popupCommandContainer = document.getElementById("popup_command_container");
        const popupMessage = document.getElementById("popup_command_message");
        const itemButtonContainers = Array.from(document.querySelectorAll(".item_button_container"));
        const popupMessageContainer = document.getElementById("popup_container_without_button");
        const loadingEarth = document.getElementById("loading_earth");
        const popupErrorMessage = document.getElementById("popup_message_without_button");
        getTextCommand().then((text_command) => {
            if (text_command) {
                showTextCommand();
            } else {
                showErrorMessage();
            }

            function showTextCommand() {
                popupMessage.textContent = text_command;
                showFTFMessage(popupCommandContainer);
            }

            function showErrorMessage() {
                const errorMessage = "非常抱歉，但是系統找不到您需要的資訊！";
                popupErrorMessage.textContent = errorMessage;
                loadingEarth.style.display = "none";
                itemButtonContainers.forEach((element) => {
                    element.style.opacity = "1";
                });
                showFTFMessage(popupMessageContainer, 3000);
            }
        });

        async function getTextCommand() {
            const redirectURL = "/story/fetchtextcommand";
            try {
                await sendDataToServer(redirectURL, ["create_story_page"], () => {});
                const response = await fetch(redirectURL); // 向後端發送請求
                const data = await response.json();
                return data.text_command;
            } catch (error) {
                console.error("Fetch error:", error);
                return null; // 在這裡可以處理錯誤或返回一個預設值
            }
        }
    }

    function setButtonText(item_page) {
        const button = document.getElementById(`${item_page}_button`);
        const create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
        const defaultText = getItemPageText(item_page);
        const text = create_story_page[item_page]?.item_name || defaultText;
        wrapTextWithSpans(text, button, "button_text");
        button.dataset.defaultText = defaultText;
        button.title = button.dataset.wrapText; // 使用 title 屬性顯示預設文字
    }

    function setButotnEffects(item_page) {
        const button = document.getElementById(`${item_page}_button`);
        const removeIcon = document.getElementById(`${item_page}_remove_icon`);
        const wrapText = button.dataset.wrapText;
        const defaultText = button.dataset.defaultText;
        const hasSelected = wrapText !== defaultText;
        const removeText = `是否移除${wrapText}？`;
        removeIcon.title = removeText;
        removeIcon.addEventListener("mouseenter", enterRemoveIcon); // 當滑鼠懸浮在移除圖標上時
        removeIcon.addEventListener("mouseleave", leaveRemoveIcon); // 當滑鼠移開移除圖標時
        if (hasSelected) {
            button.addEventListener("mouseenter", enterButton); // 添加滑鼠滑過事件
            button.addEventListener("mouseleave", leaveButton); // 添加滑鼠離開事件
        }
        removeIcon.addEventListener("click", clickRemoveIcon); // 為移除圖標添加點擊事件處理器

        function enterRemoveIcon(event) {
            event.stopPropagation(); // 阻止事件冒泡
            button.textContent = removeText; // 顯示移除提示
        }

        function leaveRemoveIcon(event) {
            if (event.relatedTarget !== button) {
                wrapTextWithSpans(wrapText, button, "button_text"); // 恢復到選擇過的項目名稱
                removeIcon.style.display = "none";
            }
        }

        function enterButton(event) {
            wrapTextWithSpans(defaultText, button, "button_text");
            removeIcon.style.display = "flex";
        }

        function leaveButton(event) {
            if (event.relatedTarget !== removeIcon) {
                wrapTextWithSpans(wrapText, button, "button_text");
                removeIcon.style.display = "none";
            }
        }

        function clickRemoveIcon(event) {
            event.stopPropagation(); // 阻止事件冒泡
            removeIcon.removeEventListener("mouseenter", enterRemoveIcon);
            button.removeEventListener("mouseenter", enterButton);
            button.removeEventListener("mouseleave", leaveButton);
            wrapTextWithSpans(defaultText, button, "button_text"); // 重置為預設文本
            removeIcon.style.display = "none"; // 隱藏移除圖標
            // 更新 sessionStorage 中的資料
            const create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
            var item_type = create_story_page[item_page];
            item_type.item_id = null;
            item_type.item_name = null;
            item_type.cover_design_link = null;
            sessionStorage.setItem("create_story_page", JSON.stringify(create_story_page));
        }
    }

    async function setItemPage(item_page) {
        const button = document.getElementById(`${item_page}_button`);
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        select_item_page.item_page = item_page;
        select_item_page.item_page_text = button.dataset.wrapText;
        sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
        await sendDataToServer("/story/selectitem", ["select_item_page", "create_story_page"]);
    }
}
