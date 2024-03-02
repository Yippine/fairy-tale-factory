document.addEventListener("DOMContentLoaded", () => {
    adjustStoryAlignment();
    initialSession();
    iniitalArticle();
    setupPopupHandlers();
});

window.addEventListener("resize", adjustStoryAlignment);

function adjustStoryAlignment() {
    const storyContainer = document.querySelector(".story");
    storyContainer.style.alignItems = storyContainer.scrollHeight > storyContainer.clientHeight ? "flex-start" : "center";
}

function initialSession() {
    const pageData = document.querySelector(".page-data");
    const storybookDisplayPage = JSON.parse(pageData.dataset.storybookDisplayPage);
    sessionStorage.setItem("storybook_display_page", JSON.stringify(storybookDisplayPage));
}

function iniitalArticle() {
    const title = document.querySelector(".title");
    const pageDiv = document.getElementById("page");
    const spanElement = document.createElement("span");
    const story = document.querySelector(".story");
    const image = document.querySelector(".image_container img");
    const storybookDisplayPage = JSON.parse(sessionStorage.getItem("storybook_display_page"));
    title.textContent = storybookDisplayPage.story_name;
    displayArticle();
    setupNavigationButtons();

    function displayArticle() {
        const storybookDisplayPage = JSON.parse(sessionStorage.getItem("storybook_display_page"));
        const curPage = storybookDisplayPage.cur_page;
        const maxPage = storybookDisplayPage.max_page;
        const articleList = JSON.parse(storybookDisplayPage.article_list);
        const article = articleList[curPage - 1];
        pageDiv.innerHTML = `<span>第 ${curPage} 頁 / 共 ${maxPage} 頁</span>`;
        spanElement.textContent = article.line_content;
        story.innerHTML = "";
        story.appendChild(spanElement);
        image.src = article.line_image_link;
    }

    function setupNavigationButtons() {
        const prevPage = document.querySelector(".navigation_button.prev");
        const nextPage = document.querySelector(".navigation_button.next");
        prevPage.style.display = "none";
        prevPage.addEventListener("click", () => navigatePage(false));
        nextPage.addEventListener("click", () => navigatePage(true));
        document.addEventListener("keydown", (event) => {
            if (event.key === "ArrowLeft" && prevPage.style.display != "none") {
                navigatePage(false);
            } else if (event.key === "ArrowRight" && nextPage.style.display != "none") {
                navigatePage(true);
            }
        });
    
        function navigatePage(isNext) {
            const storybookDisplayPage = JSON.parse(sessionStorage.getItem("storybook_display_page"));
            const startPage = 1;
            const curPage = storybookDisplayPage.cur_page;
            const maxPage = storybookDisplayPage.max_page;
            const newPage = isNext ? Math.min(curPage + 1, maxPage) : Math.max(curPage - 1, startPage);
            prevPage.style.display = "block";
            nextPage.style.display = "block";
            if (newPage === startPage) {
                prevPage.style.display = "none";
            } else if (newPage === maxPage) {
                nextPage.style.display = "none";
            }
            if (newPage !== curPage) {
                storybookDisplayPage.cur_page = newPage;
                sessionStorage.setItem("storybook_display_page", JSON.stringify(storybookDisplayPage));
                displayArticle();
            }
        }
    }
}

function setupPopupHandlers() {
    const homeButton = document.querySelector(".go_home_button");
    const saveButton = document.querySelector(".save_story_button");
    const popupButtonContainer = document.getElementById("popup_container_with_button");
    const popupButtonMessage = document.getElementById("popup_message_with_button");
    const popupButtonConfirm = document.getElementById("popup_confirm_with_button");
    const popupButtonCancel = document.getElementById("popup_cancel_with_button");
    const popupMessageContainer = document.getElementById("popup_container_without_button");

    homeButton.addEventListener("click", () => togglePopup("確認是否回到首頁？"));
    saveButton.addEventListener("click", () => togglePopup("確認是否放入珍藏？"));

    popupButtonConfirm.addEventListener("click", () => {
        if (popupButtonMessage.innerText === "確認是否放入珍藏？") {
            showMessage();
        } else {
            window.location.href = "/home"; // 假定回到首頁的路徑
        }
    });

    popupButtonCancel.addEventListener("click", () => {
        popupButtonContainer.style.display = "none";
    });

    popupButtonContainer.addEventListener("click", (e) => {
        if (e.target === popupButtonContainer) {
            popupButtonContainer.style.display = "none";
        }
    });

    function togglePopup(message) {
        popupButtonMessage.innerText = message;
        popupButtonContainer.style.display = popupButtonContainer.style.display === "flex" ? "none" : "flex";
    }

    function showMessage() {
        popupButtonContainer.style.display = "none";
        popupMessageContainer.style.display = "flex";
        setTimeout(() => {
            popupMessageContainer.style.display = "none";
        }, 1500);
    }
}
