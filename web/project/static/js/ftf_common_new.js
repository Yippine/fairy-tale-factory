function redirectTo(path) {
    window.location.href = path;
}

async function sendDataToServer(redirectURL, pages, finishedCallback) {
    try {
        ensureCSRFToken(); // 確保 csrftoken 存在
        const endpointURL = transformRoute(redirectURL);
        const response = await fetch(endpointURL, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Content-Type": "application/json",
            },
            body: getSessionData(pages),
        });
        if (response.ok) {
            if (finishedCallback && typeof finishedCallback === "function") {
                finishedCallback(); // 執行完成後的回調函式
            } else {
                redirectTo(redirectURL);
            }
        } else {
            throw new Error("Failed to send data to server");
        }
    } catch (error) {
        console.error(error);
    }

    function ensureCSRFToken() {
        if (!getCookie("csrftoken")) {
            // 假設 token 值，實際應用中需要更安全的生成方式
            document.cookie = "csrftoken=fake_token_value; path=/";
        }
    }

    function transformRoute(originalRoute) {
        const parts = originalRoute.split("/");
        const lastPart = parts.pop();
        const newLastPart = `set${lastPart}pagenew/`;
        const newRoute = `${parts.join("/")}/${newLastPart}`;
        return newRoute;
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

    function getSessionData(pages) {
        const data = {};
        for (const page of pages) {
            data[page] = JSON.parse(sessionStorage.getItem(page));
        }
        return JSON.stringify(data);
    }
}

function wrapTextWithSpans(text, element, className = "") {
    if (!element) {
        console.error("Element not found.");
        return;
    }
    const chars = text.split("");
    element.dataset.wrapText = text;
    while (element.firstChild) {
        element.removeChild(element.firstChild);
    }
    chars.forEach((char) => {
        const span = document.createElement("span");
        if (className) {
            span.className = className;
        }
        span.innerText = char;
        element.appendChild(span);
    });
}

function getItemPageText(itemPage) {
    let text;
    switch (itemPage) {
        case "main_role":
            text = "請選擇主角";
            break;
        case "sup_role":
            text = "請選擇配角";
            break;
        case "item":
            text = "請選擇道具";
            break;
        default:
            text = "請選擇？？";
    }
    return text;
}

function typewriterEffect(selector, millisecond, finishedCallback, typingCallback) {
    const elements = document.querySelectorAll(selector);
    let index = 0;
    if (elements.length > 0) {
        prepareNext(elements[index]); // 從第一個元素開始
    }

    function prepareNext(element) {
        const text = element.textContent;
        element.textContent = ""; // 清空元素的文字，準備逐字顯示
        element.style.display = "block";
        typeWriter(text, element);
    }

    function typeWriter(text, element, i = 0) {
        if (i < text.length) {
            element.innerHTML += text.charAt(i++);
            if (typingCallback && typeof typingCallback === 'function') {
                typingCallback(); // 執行打字時的回調函式
            }
            setTimeout(() => {
                typeWriter(text, element, i);
            }, millisecond); // 調整速度
        } else if (index < elements.length - 1) {
            prepareNext(elements[++index]);
        } else {
            if (finishedCallback && typeof finishedCallback === 'function') {
                finishedCallback(); // 執行完成後的回調函式
            }
        }
    }
}

function showCommonMessage(buttonId) {
    const popupMessageContainer = document.getElementById(buttonId);
    popupMessageContainer.style.display = "flex";
    // 設置計時器，3 秒後自動關閉錯誤訊息
    const timeout = setTimeout(() => {
        closePopupAndRedirect();
    }, 3000);
    // 處理點擊非 .popup_container 區域讓錯誤訊息消失的功能
    document.addEventListener("click", function outsideClick(event) {
        if (event.target.id === buttonId && !event.target.closest('.popup_content')) {
            closePopupAndRedirect();
            document.removeEventListener("click", outsideClick); // 移除此事件監聽器以避免多次觸發
        }
    });

    function closePopupAndRedirect() {
        const popupMessageContainer = document.getElementById(buttonId);
        popupMessageContainer.style.display = "none";
        clearTimeout(timeout); // 清除計時器以避免再次自動關閉
    }
}

function showFTFMessage(button, millisecond) {
    button.style.display = "flex";
    // 設置計時器，3 秒後自動關閉錯誤訊息
    if (millisecond) {
        const timeout = setTimeout(() => {
            closePopupAndRedirect();
        }, millisecond);
    }
    // 處理點擊非 .popup_container 區域讓錯誤訊息消失的功能
    document.addEventListener("click", function outsideClick(event) {
        if (event.target.id === button.id && !event.target.closest('.popup_content')) {
            closePopupAndRedirect();
            document.removeEventListener("click", outsideClick); // 移除此事件監聽器以避免多次觸發
        }
    });

    function closePopupAndRedirect() {
        button.style.display = "none";
        clearTimeout(timeout); // 清除計時器以避免再次自動關閉
    }
}
