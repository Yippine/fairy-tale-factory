var page_item_selected = {
    item_id: null,
    item_name: null,
    cover_design_link: null,
};

document.addEventListener("DOMContentLoaded", (event) => {
    handleButtonClick();
    generateItemsFromData();
    addBorderEffect();
});

function handleButtonClick() {
    document.getElementById("select_button").addEventListener("click", () => {
        if (checkSelectedItem()) {
            setSelectedItem();
        }
        redirectTo("createstory");
    });
    document.getElementById("home_button").addEventListener("click", () => redirectTo("createstory"));

    function checkSelectedItem() {
        result = page_item_selected.item_id !== undefined && page_item_selected.item_id !== null;
        return result;
    }

    function setSelectedItem() {
        var select_item = JSON.parse(sessionStorage.getItem("select_item"));
        var item_page = select_item.item_page;
        if (!select_item.story_info) {
            select_item.story_info = {
                main_role: {
                    item_id: "",
                    item_name: "",
                    cover_design_link: "",
                },
                sup_role: {
                    item_id: "",
                    item_name: "",
                    cover_design_link: "",
                },
                item: {
                    item_id: "",
                    item_name: "",
                    cover_design_link: "",
                },
            };
        }
        var story_info = select_item.story_info;
        if (item_page && story_info.hasOwnProperty(item_page)) {
            var selected_item = story_info[item_page];
            selected_item.item_id = page_item_selected.item_id;
            selected_item.item_name = page_item_selected.item_name;
            selected_item.cover_design_link = page_item_selected.cover_design_link;
            sessionStorage.setItem("select_item", JSON.stringify(select_item));
        } else {
            console.error("Invalid item page: " + item_page);
        }
    }

    function redirectTo(path) {
        window.location.href = `/story/${path}`;
    }
}

function generateItemsFromData() {
    const dataContainer = document.getElementById("data-container");
    const itemElements = Array.from(dataContainer.getElementsByClassName("item-data"));
    const itemListContainer = document.querySelector(".item_list_container");

    itemElements.forEach((element, index) => {
        const itemId = element.getAttribute("data-id");
        const itemName = element.getAttribute("data-name");
        const itemInfo = element.getAttribute("data-info");
        const itemCount = 2;

        var newItemName = document.createElement("div");
        newItemName.id = `item_name_${itemId}`;
        newItemName.className = "item_name";
        newItemName.textContent = index + 1 + ". " + itemName;
        itemListContainer.appendChild(newItemName);

        var newItemInfo = document.createElement("div");
        newItemInfo.className = "item_info";
        itemListContainer.appendChild(newItemInfo);

        newItemName.addEventListener("click", function (event) {
            fetchItemInfo(itemId, itemName, newItemInfo);
            toggleActiveState(itemListContainer, itemElements, index, newItemName, newItemInfo, itemCount);
        });
    });

    setTimeout(() => {
        scrollToSelectedItem();
    }, 0);

    function fetchItemInfo(id, name, infoDiv) {
        fetch("/story/itemdetailsbydata?item_id=" + id)
            .then((response) => response.json())
            .then((data) => {
                infoDiv.textContent = data.item_info;
                page_item_selected.item_id = id;
                page_item_selected.item_name = name;
            })
            .catch((error) => console.error("Fetch error:", error));
    }

    function toggleActiveState(listContainer, elements, curIndex, nameDiv, infoDiv, count) {
        elements.forEach((el, idx) => {
            if (idx !== curIndex) {
                const otherNameDiv = listContainer.children[idx * count + 1];
                const otherInfoDiv = listContainer.children[(idx + 1) * count];
                otherNameDiv.style.backgroundColor = "#d6a982";
                otherNameDiv.classList.remove("active");
                otherInfoDiv.classList.remove("active");
                otherInfoDiv.textContent = "";
                listContainer.children[idx * count + 1].style.borderRadius = "1.75vw";
            }
        });
        nameDiv.classList.toggle("active");
        infoDiv.classList.toggle("active");
        if (infoDiv.classList.contains("active")) {
            nameDiv.style.backgroundColor = "#ffd295";
            nameDiv.style.borderRadius = "1.75vw 1.75vw 0 0";
            nameDiv.scrollIntoView({ behavior: "smooth", block: "nearest" });
            setImgSrc(nameDiv);
        } else {
            nameDiv.style.borderRadius = "1.75vw";
        }
    }

    function setImgSrc(nameDiv) {
        var itemName = getItemName(nameDiv.textContent);
        fetch("/story/getstoryelementname?item_name=" + itemName)
            .then((response) => response.json())
            .then((data) => {
                const imgElement = document.getElementById("item_image");
                cover_design_link = "/static/img/story_elements/" + data.img_name;
                imgElement.src = cover_design_link;
                page_item_selected.cover_design_link = cover_design_link;
            })
            .catch((error) => console.error("Fetch error:", error));
    }

    function getItemName(itemName) {
        var regex = /\d+\.\s(.+)/;
        var match = itemName.match(regex);

        if (match) {
            var formalName = match[1];
            return formalName;
        }
        return "";
    }

    function scrollToSelectedItem() {
        const selectedItemId = document.getElementById("selected_item_id").textContent;
        const selectedItemName = document.getElementById(`item_name_${selectedItemId}`);
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
