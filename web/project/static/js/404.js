document.addEventListener("DOMContentLoaded", function () {
    setupNavigation();
    handleTypewriterEffect();
    handleObserveEffect();
});

function setupNavigation() {
    document.getElementById("go_home_button").addEventListener("click", () => redirectTo("/home"));
}

function handleTypewriterEffect() {
    const containerId = "article_container";
    const container = document.querySelector(`.${containerId}`); // 獲取容器
    // 呼叫打字機效果函式
    typewriterEffect(`.${containerId} h1, .${containerId} p, .${containerId} span`,12.5,() => {
        const spaceContainer = document.querySelector(".space_container");
        spaceContainer.style.display = "flex";
        scrollToBottom(container); // 每次打印字符後滾動
    }, () => {
        scrollToBottom(container); // 每次打印字符後滾動
    });
    
    // 滾動到元素底部的函式
    function scrollToBottom(element) {
        element.scrollTop = element.scrollHeight;
    }
}

function handleObserveEffect() {
    // 選擇要監視的元素
    const backgroundContainer = document.querySelector(".background_container");
    const articleContainer = document.querySelector(".article_container");
    const spaceContainer = document.querySelector(".space_container");
    const homeButton = document.querySelector(".go_home_button");
    // 定義 IntersectionObserver 的回呼函式
    const intersectionCallback = (entries, observer) => {
        entries.forEach((entry) => {
            // 如果 space_container 進入了視窗可見區域
            if (entry.isIntersecting) {
                articleContainer.style.backgroundColor = "initial";
                articleContainer.style.backdropFilter = "initial";
                homeButton.style.display = "flex";
            } else {
                articleContainer.style.backgroundColor = "rgba(69, 69, 69, 0.4)";
                articleContainer.style.backdropFilter = "blur(0.2rem)";
                homeButton.style.display = "none";
            }
        });
    };
    // 建立 IntersectionObserver 實例，指定回呼函式和根容器（可選）
    const observer = new IntersectionObserver(intersectionCallback, {
        // 根容器為 background_container，這樣 space_container 進入 background_container 可見區域時會觸發回調
        root: backgroundContainer,
    });
    // 開始觀察 space_container
    observer.observe(spaceContainer);
}
