var defaultText = "請在這裡輸入使用者的提問...";
let currentPrompt = { file_content: "", user_question: "" };

document.addEventListener("DOMContentLoaded", () => {
    restoreDefaultText();
    initializePrompt();
    initializeSearch();
    initializeClickHandlers();
    renderPrompt();
});

function clearDefaultText() {
  var textarea = document.getElementsByClassName("ask_container")[0];
  if (textarea.value == defaultText) {
    textarea.value = "";
  }
}

function restoreDefaultText() {
  var textarea = document.getElementsByClassName("ask_container")[0];
  if (textarea.value == "") {
    textarea.value = defaultText;
  }
}

function renderPrompt() {
    const promptElement = document.getElementById("prompt");
    const displayContainer = document.getElementsByClassName("display_container")[0];
    displayContainer.value = `${promptElement.innerHTML}\n\n"""${currentPrompt.file_content}${currentPrompt.user_question}"""`;
}

function initializePrompt() {
    const askContainer = document.getElementsByClassName("ask_container")[0];
    askContainer.addEventListener("input", updatePrompt);
}

function initializeSearch() {
    const searchInput = document.getElementById("search"); // 獲取搜尋輸入框
    const searchFileList = document.querySelector(".search_result_container .file_list"); // 獲取用於顯示搜尋結果的容器
    searchInput.addEventListener("input", () => {
        const searchText = searchInput.value; // 獲取用戶輸入
        if (searchText.length > 0) {
            fetch(`/searchfiles?searchText=${encodeURIComponent(searchText)}`) // 向後端發送請求
                .then(response => response.json())
                .then(data => {
                    searchFileList.innerHTML = ""; // 清空先前的搜尋結果
                    data.files.forEach(file_info => { // 遍歷後端返回的檔案列表
                        const a = document.createElement("a");
                        a.className = "search_result_link"
                        a.href = file_info.full_path
                        a.textContent = file_info.relative_path; // 設置檔案名為列表項目的內容
                        searchFileList.appendChild(a); // 將列表項目添加到容器中
                    });
                    updateCounts();
                });
        } else {
            searchFileList.innerHTML = ""; // 如果搜尋框清空，則清空搜尋結果
            updateCounts();
        }
    });
}

function initializeClickHandlers() {
    document.body.addEventListener("click", function(e) {
        if (e.target.classList.contains("search_result_link")) {
            const existingLinks = document.querySelectorAll(".selected_file_container .file_list .selected_file_link");
            let isDuplicate = false;
            existingLinks.forEach(link => {
                if (link.getAttribute("href") === e.target.getAttribute("href")) {
                    isDuplicate = true;
                }
            });
            if (!isDuplicate) {
                const newLink = e.target.cloneNode(true); // 複製點擊的元素
                newLink.classList.remove("search_result_link");
                newLink.classList.add("selected_file_link"); // 更改類別以反映它現在是「已選取的檔案」
                document.querySelector(".selected_file_container .file_list").appendChild(newLink); // 將新鏈接添加到「已選取的檔案」列表中
                updateCounts();
                updateDisplayContainer();
            }
        } else if (e.target.classList.contains("selected_file_link")) {
            e.preventDefault();
            e.target.remove(); // 從「已選取的檔案」列表中移除點擊的元素
            updateCounts();
            updateDisplayContainer();
        }
    });
}

// 更新計數的函數
function updateCounts() {
    const selectedFileList = document.querySelector(".selected_file_container .file_list");
    const searchResultList = document.querySelector(".search_result_container .file_list");
    const selectedFileCount = document.querySelector(".selected_file_container .title_container .count");
    const searchResultCount = document.querySelector(".search_result_container .title_container .count");
    const selectedCount = selectedFileList.querySelectorAll("a").length;
    const searchCount = searchResultList.querySelectorAll("a").length;
    selectedFileCount.innerHTML = selectedCount === 0 ? "" : `（${selectedCount} 筆）`;
    searchResultCount.innerHTML = searchCount === 0 ? "" : `（${searchCount} 筆）`;
}

function updateDisplayContainer() {
    const selectedFiles = document.querySelectorAll(".selected_file_container .file_list .selected_file_link");
    let displayText = '';
    // 重置 file_content 的內容
    currentPrompt.file_content = '';
    // 對於每一個已選擇的檔案，發送 AJAX 請求獲取檔案內容
    selectedFiles.forEach((fileLink, index) => {
        const filePath = fileLink.getAttribute("href");
        const fileName = fileLink.textContent;
        // 假設伺服器提供一個API '/getfilecontent' 來返回檔案內容
        fetch(`/getfilecontent?path=${encodeURIComponent(filePath)}`)
            .then(response => response.text())
            .then(content => {
                displayText += `${fileName}:\n"""${content}"""\n\n`;
                // 確保按檔案選擇順序更新 file_content
                if (index === selectedFiles.length - 1) {
                    updateFileContent(displayText);
                }
            });
    });
}

function updateFileContent(displayText) {
    currentPrompt.file_content = displayText;
    renderPrompt();
}

function updatePrompt(event) {
    currentPrompt.user_question = event.target.value;
    renderPrompt();
}
