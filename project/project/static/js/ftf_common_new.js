function redirectTo(path) {
    window.location.href = path;
}

async function sendDataToServer(redirectURL, data) {
    try {
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
            redirectTo(redirectURL);
        } else {
            throw new Error("Failed to send data to server");
        }
    } catch (error) {
        console.error(error);
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
