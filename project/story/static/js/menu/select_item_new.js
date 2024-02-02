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

function generateItems(itemCount) {
    var itemListContainer = document.querySelector(".item_list_container");
    for (var i = 1; i <= itemCount; i++) {
        var newItem = document.createElement("div");
        newItem.className = "item";
        newItem.textContent = i + ". 一二三四五六七八九一二三四五六七八九一二三四五六七八九一二三四五六七八九";
        itemListContainer.appendChild(newItem);

        var newItemInfo = document.createElement("div");
        newItemInfo.className = "item_info";
        newItemInfo.textContent = "項目 " + i + " 的相關資訊相關資訊相關資訊相關資訊相關資訊相關資訊相關資訊";
        itemListContainer.appendChild(newItemInfo);
    }

    // if (itemCount > 0) {
    //     itemListContainer.children[0].classList.add("first_item");
    //     itemListContainer.children[itemListContainer.children.length - 1].classList.add("last_item");
    // }
}

generateItems(15);
