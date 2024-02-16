# 專案名稱 - 貢獻指南

歡迎您參與我們專案的開發！以下是一份關於如何貢獻於專案的指南，請仔細閱讀並按照指示操作。

## 建置

### 在開始開發前，請完成以下建置步驟：

- **製作 SSH Key**：確保您的開發環境已設定好 SSH Key。
    ```bash
    # 製作 SSH Key
    # 第一道指令
    ssh-keygen-t ed25519 -C "your_email@example.com"
    # 如果第一道指令不管用，則使用第二道指令
    # ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

    # 啟動 SSH Agent
    eval `ssh-agent -s`

    # 將私鑰加入 SSH Agent
    ssh-add ~/.ssh/id_ed25519
    # ssh-add ~/.ssh/id_rsa

    # 顯示公鑰內容並手動複製
    cat id_ed25519.pub
    # cat id_rsa.pub

    # 點擊 GitHub 的個人大頭貼 → settings → SSH and GPG keys → new SSH key
    # Title：自定義鑰匙名稱
    # Key：貼上開頭為 `ssh-ed25519` 或 `ssh-rsa` 的公鑰

    # 待 GitHub 上鎖後，測試 SSH 連線
    ssh -T git@github.com
    ```

- **設定成員資訊**：在本地環境中設定您的成員資訊，以便正確歸屬提交記錄。
    ```bash
    # 設定開發者信箱
    git config --global user.email "你的 GitHub 信箱"

    # 設定開發者名稱
    git config --global user.name "你的 GitHub 名稱"
    ```
- **下載專案目錄**：使用 `git clone` 下載專案到您的本地環境。
    ```bash
    # 進入正式專案的網址
    # 正式專案：https://github.com/Yippine/fairy-tale-factory
    # 測試專案：https://github.com/Yippine/fairy-tale-factory-test

    # fork 到自己的 GitHub 專案
    # 【溫馨警告】取消勾選僅保留 main 分支

    # 指定專案存放的位置
    cd "接下來要下載專案的存放目錄"

    # 複製專案到本地端
    # Code → SSH → Copy url to clipboard
    git clone `SSH url`
    ```

- **同步分支狀態**：使用 `git fetch upstream` 來同步上游庫的分支狀態。
    ```bash
    # 進入專題目錄
    cd fairy-tale-factory/

    # 連結上游儲存庫的網址（只需做一次）
    # 正式版本的上游儲存庫
    git remote add upstream https://github.com/Yippine/fairy-tale-factory
    # 測試版本的上游儲存庫
    # git remote add upstream https://github.com/Yippine/fairy-tale-factory-test

    # 查看上游儲存庫的設定（只需做一次）
    git remote -v

    # 移除上游儲存庫的設定（重作時）
    # git remote remove upstream

    # 拉取上游儲存庫的最新變更
    git fetch upstream

    # 查看所有本地和上游的分支
    git branch -a

    # 將尚未建立在本地的上游儲存庫分支建立在本地
    git checkout -b `本地分支名稱` upstream/`上游分支名稱`
    ```

- **設定指令別名**：使用 `git config --global alias.xx` 設定您喜歡的指令別名。
    ```bash
    # 將 git ck 設定為 git checkout 的別名
    git config --global alias.ck checkout

    # 將 git br 設定為 git branch 的別名
    git config --global alias.br branch

    # 將 git cm 設定為 git commit 的別名
    git config --global alias.cm commit

    # 將 git st 設定為 git status 的別名
    git config --global alias.st status

    # 這一行設定了一個名為 'lg' 的別名，用來顯示漂亮的提交歷史圖形
    # %C(auto) 用於自動設定文字顏色
    # %h 顯示簡寫的提交哈希值
    # %cn 顯示提交者名字，
    # %s 顯示提交訊息
    # %cr 顯示相對時間
    git config --global alias.lg "log --graph --pretty=format:'%C(auto)%h %C(bold blue)%cn %C(auto)%s %C(bold green)%cr'"

    # 移除別名設定
    # git config --global --unset alias.`別名名稱`
    ```

## 開發

### 在進行開發前，請執行以下準備工作：

- **建立開發分支**：如果尚未建立開發分支，請建立一個新的開發分支。
    ```bash
    # 基於現有的版本分支建立新的開發分支
    git checkout -b `開發者名稱` `版本分支`
    ```

- **同步更新狀態**：每次開發前，請確保您的分支狀態與上游庫同步，您可以選擇使用不同的同步方式。
    - remote/upstream repository → remote repository → local repository
        ```bash
        # 到 GitHub 上的遠端儲存庫，依序點擊 sync fork 和 update branch

        # 切換到上線分支
        git checkout main

        # 從遠端儲存庫（origin）拉取上線分支的最新更改
        git pull origin main

        # 切換到版本分支
        git checkout `版本分支`

        # 將上線分支的更改合併到版本分支
        git merge main

        # 從遠端儲存庫（origin）拉取版本分支的最新更改
        git pull origin `版本分支`

        # 切換到開發分支
        git checkout `開發者名稱`

        # 將版本分支的更改合併到開發分支
        git merge `版本分支`
        ```

    - remote/upstream repository → local repository → remote repository
        ```bash
        # 從上游程式庫中取得更新
        git fetch upstream

        # 切換到上線分支
        git checkout main

        # 將上游程式庫的更新合併到上線分支
        git merge upstream/main

        # 如果版本有更新，將其推送到遠端儲存庫
        git push origin main

        # 切換到版本分支
        git checkout `版本分支`

        # 將上線分支的更改合併到版本分支
        git merge main

        # 將上游程式庫的更新合併到版本分支
        git merge upstream/`版本分支`

        # 如果版本有更新，將其推送到遠端儲存庫
        git push origin `版本分支`

        # 切換到開發分支
        git checkout `開發者名稱`

        # 將版本分支的更新合併到開發分支
        git merge `版本分支`
        ```

### 在開發過程中，請注意以下事項：

- **儲存開發進度**：在開發完成或達到一定進度時，請提交您的開發進度。
    ```bash
    # 切換到開發分支
    git checkout `開發者名稱`

    # 檢查目前的檔案異動狀態
    git status

    # 將異動的指定檔案加入到暫存區
    git add `file`
    # 將異動的所有檔案加入到暫存區
    # git add `.`

    # 將暫存區的更改正式記錄到版本歷史中，-m 後面跟的是提交訊息，用來描述這次更改的內容
    # 
    # 格式：`類型(範疇): 描述`
    # 	類型：請查看類型列表
    # 	範疇：請查看範疇列表
    # 	描述：開發人員自定義
    # 
    # 範例：
    # 	`feat(front-end): 切換頁面的動態效果`
    # 	`fix(gen img): 故事圖像無法正確顯示`
    git commit -m "類型(範疇): 描述"

    # 切換到版本分支
    git checkout `版本分支`

    # 將開發分支的異動合併到版本分支中
    git merge `開發者名稱`

    # 上傳版本分支的新記錄到遠端儲存庫
    git push origin `版本分支`
    ```

- **顯示提交記錄**：使用 `git log` 來查看提交記錄，以便了解開發歷程。
    ```bash
    # 顯示漂亮的提交歷史圖形（如果沒設定 Alias）
    git log --graph --pretty=format:'%C(auto)%h %C(bold blue)%cn %C(auto)%s %C(bold green)%cr'

    # 顯示漂亮的提交歷史圖形（如果有設定 Alias）
    git lg
    ```

### 當開發完成後，請執行以下步驟：

- **等待代碼審查**：提交代碼審查請求，等待團隊成員進行審查。
    ```bash
    # 1. 到 GitHub 的版本分支下進行 pull request

    # 2. 選擇正確的遠端和上游的儲存庫和版本分支
    # 請勿上傳至主要分支，如果不慎上傳，請關閉該次請求：
    # 【不正確】`repo: upstream, branch: main <<< repo: remote, branch: v1.0.0`
    # 【正確】`repo: upstream, branch: v1.0.0 <<< repo: remote, branch: v1.0.0`

    # 3. 等待組長通過審查中的程式碼

    # 4. 通過之後，請務必同步上游儲存庫的更新狀態
    ```

- **更改分支名稱**：根據您的角色，請更改分支名稱以反映您的貢獻。
    - 如果你是上游庫的開發者
        ```bash
        # 更改本地分支名稱
        git branch -m `舊分支名稱` `新分支名稱`

        # 推送更改到遠端儲存庫，並設定新分支跟踪遠端分支
        git push origin -u `新分支名稱`

        # 刪除遠端的舊分支
        git push origin --delete `舊分支名稱`
        ```
    
    - 如果你是 Fork 到遠端庫的開發者
        ```bash
        # 重命名本地的舊分支
        git branch -m `舊分支名稱` `新分支名稱`

        # 推送新分支到 fork 儲存庫（origin），並設定新分支跟踪遠端分支
        git push origin -u `新分支名稱`

        # 刪除 fork 儲存庫上的舊分支
        git push origin --delete `舊分支名稱`

        # 獲取上游儲存庫的最新狀態
        git fetch upstream

        # 如果本地有任何基於舊分支的工作，應該重新基於新分支
        git rebase `新分支名稱`

        # 通知所有成員合併上游的變更
        git merge upstream/`新分支名稱`
        # git rebase upstream/`新分支名稱`
        ```

## 整合測試

### 最後，請進行整合測試以確保代碼品質和功能完整性。

```bash
# 待版本分支的所有功能開發完畢後，所有成員會在版本分支中進行整合測試
# 此時不再進行功能開發，只會進行臭蟲修復
# 待所有臭蟲修復完畢後，組長會將版本分支合併回上線分支
# PM 和 TL 將會規劃下一次的主要功能開發，建立新的版本分支
# 待新的版本分支建立後，請各位成員依序執行下列動作：

# 1. 移除原有的開發分支
git branch -d `開發者名稱`

# 2. 同步上游儲存庫的分支狀態

# 3. 建立開發分支繼續下一輪的開發
```

謝謝您的貢獻！

如果您有任何問題或疑問，請隨時與我們的團隊聯繫。
