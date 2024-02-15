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
