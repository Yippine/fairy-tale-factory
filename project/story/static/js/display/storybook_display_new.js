const maxPage = 20;

document.addEventListener("DOMContentLoaded", () => {
    adjustStoryAlignment();
    const urlParams = new URLSearchParams(window.location.search);
    let page = parseInt(urlParams.get("page"), 10);
    initializePageNavigation(page);
    setupNavigationButtons(page);
    // setupPopupHandlers();
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

    document.addEventListener('keydown', (event) => {
        if (event.key === "ArrowLeft" && prevPage.style.display != "none") {
            navigatePage(false, page);
        } else if (event.key === "ArrowRight" && nextPage.style.display != "none") {
            navigatePage(true, page);
        }
    });
}

function navigatePage(isNext, currentPage) {
    const newPage = isNext ? Math.min(currentPage + 1, maxPage) : Math.max(currentPage - 1, 1);
    window.location.href = `/story/storybookdisplay?page=${newPage}`;
}

function setupPopupHandlers() {
    ["save_story", "go_home"].forEach((type) => {
        const button = document.querySelector(`#${type}_button`);
        const popup = document.querySelector(`#${type}_pop_up`);
        button.addEventListener("click", (event) => togglePopup(popup, event));
    });

    document.addEventListener("click", (event) => {
        if (!event.target.closest(".pop_up")) {
            document.querySelectorAll(".pop_up").forEach((popup) => (popup.style.display = "none"));
        }
    });

    document.getElementById("confirm_button").addEventListener("click", () => {
        document.querySelector("#save_pop_up").style.display = "none";
        showSaveSuccessPopup();
    });
}

function togglePopup(popup, event) {
    event.stopPropagation();
    const isVisible = popup.style.display === "flex";
    document.querySelectorAll(".pop_up").forEach((p) => (p.style.display = "none"));
    popup.style.display = isVisible ? "none" : "flex";
}

function showSaveSuccessPopup() {
    const saveSuccessPopup = document.querySelector("#save_success_pop_up");
    saveSuccessPopup.style.display = "flex";
    setTimeout(() => {
        saveSuccessPopup.style.display = "none";
    }, 1500);
}
