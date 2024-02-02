const observer = new MutationObserver((mutationsList, observer) => {
    mutationsList.forEach((mutation) => {
        if (mutation.addedNodes.length > 0) {
            mutation.addedNodes.forEach((node) => {
                if (node.classList.contains("auto-group-sqvl-fMn") || node.classList.contains("auto-group-nomn-m9v")) {
                    node.addEventListener("click", function () {
                        window.location.href = "/story/itemdetails";
                    });
                } else if (node.classList.contains("group-10-cn7")) {
                    node.addEventListener("click", function () {
                        window.location.href = "/story/createstory";
                    });
                }
            });
        }
    });
});

const config = { childList: true, subtree: true };
observer.observe(document, config);

function generateItemsFromData() {
    const dataContainer = document.getElementById("data-container");
    const itemElements = Array.from(dataContainer.getElementsByClassName("item-data"));
    const itemListContainer = document.querySelector(".item_list_container");

    itemElements.forEach((element, index) => {
        const itemName = element.getAttribute("data-name");
        const itemInfo = element.getAttribute("data-info");

        var newItemName = document.createElement("div");
        newItemName.className = "item_name";
        if (index === 0) {
            newItemName.classList.add("first_item_name");
        }
        newItemName.textContent = index + 1 + ". " + itemName;
        itemListContainer.appendChild(newItemName);

        var newItemInfo = document.createElement("div");
        newItemInfo.className = "item_info";
        newItemInfo.textContent = itemInfo;
        itemListContainer.appendChild(newItemInfo);

        newItemName.addEventListener("click", function () {
            newItemInfo.classList.toggle("active");
            newItemName.style.borderRadius = newItemInfo.classList.contains("active") ? "1.75vw 1.75vw 0 0" : "1.75vw";

            itemElements.forEach((el, idx) => {
                if (idx !== index) {
                    const otherItemInfo = itemListContainer.children[(idx + 1) * 2];
                    otherItemInfo.classList.remove("active");
                    itemListContainer.children[idx * 2 + 1].style.borderRadius = "1.75vw";
                }
            });
        });
    });
}

generateItemsFromData();
