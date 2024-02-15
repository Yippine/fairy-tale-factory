document.addEventListener("DOMContentLoaded", (event) => {
    handleButtonClick();
    generateItemsFromData();
    addBorderEffect();
});

function handleButtonClick() {
    const actions = {
        select_button: async () => {
            if (checkSelectedItem()) setSelectedItem();
            var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
            var create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
            await sendDataToServer("/story/createstory", {
                "select_item_page": select_item_page, "create_story_page": create_story_page
            });
        },
        return_button: () => redirectTo("/story/createstory"),
    };
    Object.keys(actions).forEach((id) => {
        document.getElementById(id).addEventListener("click", actions[id]);
    });

    function checkSelectedItem() {
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        return select_item_page.item_id != null;
    }

    function setSelectedItem() {
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        var create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
        var selected_item = create_story_page[select_item_page.item_page];
        selected_item.item_id = select_item_page.item_id;
        selected_item.item_name = select_item_page.item_name;
        selected_item.cover_design_link = select_item_page.cover_design_link;
        sessionStorage.setItem("create_story_page", JSON.stringify(create_story_page));
    }
}

function generateItemsFromData() {
    const data = Array.from(document.getElementById("data-container").getElementsByClassName("item-data"));
    const itemList = document.querySelector(".item_list_container");
    data.forEach((item, index) => {
        const itemData = {
            id: item.dataset.id,
            name: item.dataset.name,
        };
        setItemName(itemData, index);
        setItemInfo();
    });
    setTimeout(() => {
        scrollToSelectedItem();
    }, 0);

    function setItemName(itemData, index) {
        const newItemName = document.createElement("div");
        newItemName.className = "item_name";
        newItemName.textContent = `${index + 1}. ${itemData.name}`;
        newItemName.dataset.id = itemData.id;
        newItemName.onclick = (event) => selectItem(event, itemData);
        itemList.appendChild(newItemName);

        function selectItem(event, itemData) {
            fetchItemInfo(event, itemData);
            toggleActiveState(event);
        }

        function fetchItemInfo(event, itemData) {
            fetch("/story/itemdetailsbydata?item_id=" + itemData.id)
                .then((response) => response.json())
                .then((data) => {
                    const nameDiv = event.target;
                    const infoDiv = nameDiv.nextElementSibling;
                    var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
                    infoDiv.textContent = data.item_info;
                    select_item_page.item_id = itemData.id;
                    select_item_page.item_name = itemData.name;
                    sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
                })
                .catch((error) => console.error("Fetch error:", error));
        }

        function toggleActiveState(event) {
            const nameDiv = event.target;
            const infoDiv = nameDiv.nextElementSibling;
            const nameDivs = Array.from(itemList.querySelectorAll(".item_name")).filter((div) => div !== nameDiv);
            nameDivs.forEach((nameDiv, index) => {
                resetItemStyles(nameDiv);
            });
            toggleItemStyles();

            function resetItemStyles(nameDiv) {
                const infoDiv = nameDiv.nextElementSibling;
                nameDiv.style.background = "linear-gradient(#ffc366, #bc7a7a)";
                nameDiv.style.color = "initial";
                nameDiv.style.webkitTextStrokeWidth = "initial";
                nameDiv.style.webkitTextStrokeColor = "initial";
                nameDiv.style.borderRadius = "1.75vw";
                nameDiv.classList.remove("active");
                infoDiv.classList.remove("active");
                infoDiv.textContent = "";
            }

            function toggleItemStyles() {
                nameDiv.classList.toggle("active");
                infoDiv.classList.toggle("active");
                if (infoDiv.classList.contains("active")) {
                    nameDiv.style.background = "linear-gradient(#bc7a7a, #ffc366)";
                    nameDiv.style.color = "#f7f1e7";
                    nameDiv.style.webkitTextStrokeWidth = "0.01vmin";
                    nameDiv.style.webkitTextStrokeColor = "#d6a982";
                    nameDiv.style.borderRadius = "1.75vw 1.75vw 0 0";
                    nameDiv.scrollIntoView({ behavior: "smooth", block: "nearest" });
                    setImgSrc();
                } else {
                    nameDiv.style.borderRadius = "1.75vw";
                }

                function setImgSrc() {
                    var itemName = getItemName(nameDiv.textContent);
                    fetch("/story/getstoryelementname?item_name=" + itemName)
                        .then((response) => response.json())
                        .then((data) => {
                            const img = document.getElementById("item_image");
                            var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
                            cover_design_link = "/static/img/story_elements/" + data.img_name;
                            img.src = cover_design_link;
                            select_item_page.cover_design_link = cover_design_link;
                            sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
                        })
                        .catch((error) => console.error("Fetch error:", error));

                    function getItemName(itemName) {
                        var regex = /\d+\.\s(.+)/;
                        var match = itemName.match(regex);
                        if (match) {
                            var formalName = match[1];
                            return formalName;
                        }
                        return "";
                    }
                }
            }
        }
    }

    function setItemInfo() {
        const newItemInfo = document.createElement("div");
        newItemInfo.className = "item_info";
        itemList.appendChild(newItemInfo);
    }

    function scrollToSelectedItem() {
        var select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        var create_story_page = JSON.parse(sessionStorage.getItem("create_story_page"));
        const selectedItemId = create_story_page[select_item_page.item_page].item_id;
        const selectedItemName = document.querySelector(`.item_name[data-id="${selectedItemId}"]`);
        if (selectedItemName) {
            // 觸發點擊以展開 item_info
            selectedItemName.click();
            // 監聽 item_info 的過渡結束事件，然後滾動到視圖中
            const selectedItemInfo = selectedItemName.nextElementSibling; // 假設 item_info 緊隨 item_name 之後
            if (selectedItemInfo && selectedItemInfo.classList.contains("item_info")) {
                selectedItemInfo.addEventListener(
                    "transitionend",
                    function () {
                        // 確保 item_info 完全展開後再滾動
                        if (selectedItemInfo.classList.contains("active")) {
                            // 調整滾動位置以完整顯示 item_name 和 item_info
                            const offsetTop = selectedItemName.offsetTop;
                            document.querySelector(".item_list_container").scrollTop = offsetTop - selectedItemName.scrollHeight;
                        }
                    },
                    { once: true }
                ); // 監聽器只觸發一次
            }
        }
    }
}

function addBorderEffect() {
    document.querySelectorAll(".item_name").forEach((item) => {
        item.addEventListener("mousedown", function () {
            this.style.borderStyle = "inset";
        });
        item.addEventListener("mouseup", function () {
            this.style.borderStyle = "outset";
        });
        item.addEventListener("mouseleave", function () {
            // 確保如果滑鼠離開時回復原樣式
            this.style.borderStyle = "outset";
        });
    });
}
