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
            body: JSON.stringify(data),
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
