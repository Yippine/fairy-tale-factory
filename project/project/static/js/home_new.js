document.addEventListener("DOMContentLoaded", (event) => {
    clearSession();
    setupNavigation();
});

function clearSession() {
    sessionStorage.removeItem("select_item");
}

function setupNavigation() {
    document.querySelector("h1.header_content").addEventListener("click", () => redirectTo("/home"));
    document.getElementById("about_us_button").addEventListener("click", () => redirectTo("/aboutus"));
    document.getElementById("user_info_button").addEventListener("click", () => redirectTo("/user/userinfo1"));
    document.getElementById("collect_button").addEventListener("click", () => redirectTo("/story/mystorybooks"));
    document.getElementById("start_button").addEventListener("click", () => redirectTo("/story/createstory"));

    function redirectTo(path) {
        window.location.href = `${path}`;
    }
}
