const maxPage = 20;

document.addEventListener("DOMContentLoaded", () => {
    adjustStoryAlignment();
    const urlParams = new URLSearchParams(window.location.search);
    let page = parseInt(urlParams.get("page"), 10);
    initializePageNavigation(page);
    setupNavigationButtons(page);
    setupPopupHandlers();
});

window.addEventListener("resize", adjustStoryAlignment);

function adjustStoryAlignment() {
    const storyContainer = document.querySelector(".story");
    storyContainer.style.alignItems = storyContainer.scrollHeight > storyContainer.clientHeight ? "flex-start" : "center";
}

function initializePageNavigation(pagePar) {
    let page = isNaN(pagePar) ? 1 : Math.min(Math.max(pagePar, 1), maxPage);
    if (page !== pagePar) {
        window.location.href = `/story/storybookdisplay?page=${page}`;
    }
    document.getElementById("page").innerHTML = `<span>第 ${page} 頁 / 共 ${maxPage} 頁</span>`;
}

function setupNavigationButtons(page) {
    const prevPage = document.querySelector(".navigation_button.prev");
    const nextPage = document.querySelector(".navigation_button.next");
    if (page === 1) {
        prevPage.style.display = "none";
    } else if (page === maxPage) {
        nextPage.style.display = "none";
    }
    prevPage.addEventListener("click", () => navigatePage(false, page));
    nextPage.addEventListener("click", () => navigatePage(true, page));

    document.addEventListener("keydown", (event) => {
        if (event.key === "ArrowLeft" && prevPage.style.display != "none") {
            navigatePage(false, page);
        } else if (event.key === "ArrowRight" && nextPage.style.display != "none") {
            navigatePage(true, page);
        }
    });

    function navigatePage(isNext, currentPage) {
        const newPage = isNext ? Math.min(currentPage + 1, maxPage) : Math.max(currentPage - 1, 1);
        window.location.href = `/story/storybookdisplay?page=${newPage}`;
    }
}

function setupPopupHandlers() {
    const homeButton = document.querySelector(".go_home_button");
    const saveButton = document.querySelector(".save_story_button");
    const popupContainer = document.getElementById("popup_container");
    const popupMessage = document.getElementById("popup_message");
    const popupConfirm = document.getElementById("popup_confirm");
    const popupCancel = document.getElementById("popup_cancel");
    const popupButtonContainer = document.querySelector(".popup_button_container");
    const ftfPinkButton = document.querySelector(".ftf_pink_button");

    homeButton.addEventListener("click", () => togglePopup("確認是否回到首頁？"));
    saveButton.addEventListener("click", () => togglePopup("確認是否放入珍藏？"));

    popupConfirm.addEventListener("click", () => {
        if (popupMessage.innerText === "確認是否放入珍藏？") {
            showMessage("珍藏成功！");
        } else {
            window.location.href = "/home"; // 假定回到首頁的路徑
        }
    });

    popupCancel.addEventListener("click", () => {
        popupContainer.style.display = "none";
    });

    popupContainer.addEventListener("click", (e) => {
        if (e.target === popupContainer) {
            popupContainer.style.display = "none";
        }
    });

    function togglePopup(message) {
        popupMessage.innerText = message;
        popupContainer.style.display = popupContainer.style.display === "none" ? "flex" : "none";
    }

    function showMessage(message) {
        ftfPinkButton.style.paddingBottom = "4.5vmin";
        popupMessage.innerText = message;
        popupButtonContainer.style.display = "none";
        setTimeout(() => {
            popupContainer.style.display = "none";
            ftfPinkButton.style.paddingBottom = "3.25vmin";
            popupButtonContainer.style.display = "flex";
        }, 1500);
    }
}
