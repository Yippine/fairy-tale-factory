document.addEventListener("DOMContentLoaded", () => {
    adjustStoryAlignment();
    setupPageNavigation();
    setupPopupHandlers();
});

window.addEventListener("resize", adjustStoryAlignment);

function adjustStoryAlignment() {
    const storyContainer = document.querySelector(".story");
    storyContainer.style.alignItems = storyContainer.scrollHeight > storyContainer.clientHeight ? "flex-start" : "center";
}

function setupPageNavigation() {
    const urlParams = new URLSearchParams(window.location.search);
    let page = parseInt(urlParams.get("page"), 10);
    page = isNaN(page) ? 1 : Math.min(Math.max(page, 1), 20);
    document.getElementById("page").innerHTML = `<span>第 ${page} 頁</span>`;

    document.querySelectorAll(".group-12-bsJ, .group-13-Tx8").forEach((element) => {
        element.addEventListener("click", () => navigatePage(element.classList.contains("group-12-bsJ"), page));
    });
}

function navigatePage(isNext, currentPage) {
    const newPage = isNext ? Math.min(currentPage + 1, 20) : Math.max(currentPage - 1, 1);
    window.location.href = `/story/storybookdisplay?page=${newPage}`;
}

function setupPopupHandlers() {
    ["save", "home"].forEach((type) => {
        const button = document.querySelector(`#${type}_button`);
        const popup = document.querySelector(`#${type}_pop_up`);
        button.addEventListener("click", (event) => togglePopup(popup, event));
    });

    document.addEventListener("click", (event) => {
        if (!event.target.closest(".pop_up")) {
            document.querySelectorAll(".pop_up").forEach((popup) => (popup.style.display = "none"));
        }
    });

    document.getElementById("check_save_button").addEventListener("click", () => {
        document.querySelector("#save_pop_up").style.display = "none";
        showSaveSuccessfulPopup();
    });
}

function togglePopup(popup, event) {
    event.stopPropagation();
    const isVisible = popup.style.display === "flex";
    document.querySelectorAll(".pop_up").forEach((p) => (p.style.display = "none"));
    popup.style.display = isVisible ? "none" : "flex";
}

function showSaveSuccessfulPopup() {
    const saveSuccessfulPopUp = document.querySelector("#save_successful_pop_up");
    saveSuccessfulPopUp.style.display = "flex";
    setTimeout(() => {
        saveSuccessfulPopUp.style.display = "none";
    }, 1500);
}
