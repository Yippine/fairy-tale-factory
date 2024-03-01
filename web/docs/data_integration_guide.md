# 前後端資料串接與資料流指南

這份指南旨在解釋並展示如何在我們的專案中實現前後端的資料串接和資料流。

## 資料類別

我們的專案中包含了多種資料類別，涉及後端和全端範疇。

### 後端

在後端，我們操作的資料類別包括：

- **模型（Model）**：這包括資料庫表格（Database Table）和 Python 物件（Model），是我們資料儲存和處理的基礎。
- **控制器（Controller）**：業務物件（BO, Business Object）是處理業務邏輯的核心。
- **視圖（View）**：資料傳輸物件（DTO, Data Transfer Object）和視圖物件（VO, View Object）用於資料展示和傳輸。

### 全端

全端資料類別涉及：

- **DTO（Python Object）**：資料傳輸的標準格式。
- **Dictionary（Python Data Type）**：Python 中的字典類型，方便資料操作。
- **String（Python／JS String）**：字符串格式，用於資料傳輸。
- **JSON（JS Data Type）**：JavaScript 中的資料格式，廣泛用於前後端資料交換。

## 資料流

資料流的管理是前後端串接的關鍵，包括資料的傳輸和儲存。

### 傳輸

資料傳輸涉及多種轉換，如 DTO 轉 Dictionary、Dictionary 轉 String，以及 String 和 JSON 之間的轉換。這些轉換確保了資料在不同環境下的兼容性和可用性。

- **DTO → Dictionary**
    
    ```python
    class SelectItemDto:
        ...
        def to_dict(self):
            return {
                "item_id": self.item_id,
                "item_name": self.item_name,
                "cover_design_link": self.cover_design_link,
            }
    
    select_item_dto = SelectItemDto(
        item_page="example.com",
        item_page_text="example.com",
        item=ItemDTO(
            item_id="1", item_name="Main Role", cover_design_link="main_role_cover.jpg"
        ),
    )
    
    select_item_dict = select_item_dto.to_dict()
    ```
    
- **Dictionary → DTO**
    
    ```python
    class SelectItemDto:
        ...
        @staticmethod
        def from_dict(data):
            return ItemDTO(
                item_id=data.get("item_id", ""),
                item_name=data.get("item_name", ""),
                cover_design_link=data.get("cover_design_link", ""),
            )
    
    select_item_dict = {
        "item_page": "example.com",
        "item_page_text": "example.com",
        "item_id": "1",
        "item_name": "Main Role",
        "cover_design_link": "main_role_cover.jpg",
    }
    
    select_item_dto = SelectItemDto.from_dict(select_item_dict)
    ```
    
- **Dictionary → String**
    
    ```python
    import json
    
    data = get_select_item_page(request)
    json_str = json.dumps(data)
    ```
    
- **String → Dictionary**
    
    ```python
    import json
    
    json_str = request.body.decode("utf-8")
    data = json.loads(json_str)
    ```
    
- **String → JSON**
    
    ```jsx
    const select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
    ```
    
- **JSON → String**
    
    ```jsx
    sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
    ```

### 儲存

資料儲存在前端通常使用 SessionStorage，而後端則使用 Session。這允許我們在應用的不同階段和頁面之間保持資料的一致性和持久性。

- **前端 SessionStorage**
    - Setter
        
        ```jsx
        sessionStorage.setItem("select_item_page", JSON.stringify(select_item_page));
        ```
        
    - Getter
        
        ```jsx
        const select_item_page = JSON.parse(sessionStorage.getItem("select_item_page"));
        ```
        
- **後端 Session**
    - Setter
        
        ```python
        request.session["select_item_page"] = select_item_page
        ```
        
    - Getter
        
        ```python
        select_item_page = request.session.get("select_item_page", {})
        ```

### 通用

在前後端間的資料流動，涉及到從前端向後端發送資料，以及後端向前端回傳資料的過程。這包括了使用 JavaScript 和 Python 進行資料的獲取、處理和展示。

- **前端 → 後端**
    - project\story\static\js\menu\select_item.js
    
        ```jsx
        await sendDataToServer("/story/selectitem", ["select_item_page", "create_story_page"]);
        ```
    
    - project\project\static\js\ftf_common.js
    
        ```jsx
        async function sendDataToServer(redirectURL, pages, finishedCallback) {
            ...
            await fetch(endpointURL, {
                ...
                body: getSessionData(pages),
            });
            if (response.ok) {
                ...
                redirectTo(redirectURL); // 於後端 → 前端處發揮作用
            }
            ...
        
            function getSessionData(pages) {
                const data = {};
                for (const page of pages) {
                    data[page] = JSON.parse(sessionStorage.getItem(page));
                }
                return JSON.stringify(data);
            }
        }
        ```
    
    - project\story\urls.py
    
        ```python
        from utils.common_utils import handle_post_request
        
        path('setselectitempagenew/', lambda request: handle_post_request(request)),
        # 於後端 → 前端處發揮作用
        path('selectitemnew/', views.select_item, name='menu/select_item'),
        ```
    
    - project\utils\common_utils.py
    
        ```python
        import json
        from django.views.decorators.csrf import csrf_exempt
        
        @csrf_exempt
        def handle_post_request(request):
            ...
            data = json.loads(request.body.decode("utf-8"))
            for key, value in data.items():
                request.session[key] = value
            ...
        ```
    
- **後端 → 前端**
    - project\story\views.py
    
        ```python
        def select_item(request):
            select_item_page = get_select_item_page(request)
            create_story_page = get_create_story_page(request)
            return render(
                request,
                "menu/select_item.html",
                {
                    "items": items,
                    "select_item_page": json.dumps(select_item_page),
                    "create_story_page": json.dumps(create_story_page),
                },
            )
        ```
    
    - project\story\utils\dto_utils.py
    
        ```python
        from story.dto import ItemDTO, SelectItemDto, CreateStoryDto
        
        def get_select_item_page(request):
            select_item_page = request.session.get("select_item_page", {})
            if not select_item_page:
                select_item_page = SelectItemDto(item_page="", item_page_text="", item=ItemDTO()).to_dict()
                request.session["select_item_page"] = select_item_page
            return select_item_page
        ```
    
    - html access way 1
    
        ```html
        {{ select_item_page }}
        ```
    
    - html access way 2
    
        ```html
        <div id="page-data" data-select-item-page="{{ select_item_page }}" data-create-story-page="{{ create_story_page }}"></div>
        <script>
            const pageData = document.getElementById("page-data");
            var select_item_page = pageData.dataset.selectItemPage;
        </script>
        ```

## 心路歷程

在整理這份指南的過程中，我們注重了將複雜的概念簡化，並提供具體的代碼示例，以便於理解和實踐。通過這種方法，我們希望能夠提供一個清晰、易於遵循的指南，幫助開發者和使用者快速掌握專案的資料處理機制。