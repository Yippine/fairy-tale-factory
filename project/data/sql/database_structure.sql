-- CREATE DATABASE 建立資料庫
CREATE DATABASE IF NOT EXISTS fairy_tale_factory;
USE fairy_tale_factory;

-- CREATE TABLE 建立表格

-- 故事問題類型 story_issue_category
CREATE TABLE IF NOT EXISTS story_issue_category (
    issue_category_id TINYINT UNSIGNED PRIMARY KEY,
    issue_category_name VARCHAR(10) NOT NULL,
    parent_issue_category_id TINYINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 封面／設計圖 cover_design
CREATE TABLE IF NOT EXISTS cover_design (
    item_id TINYINT UNSIGNED,
	-- 封面圖從 0 開始
	-- 設計圖從 1 開始
	-- 動畫圖從 10 開始
    cover_design_id TINYINT UNSIGNED,
    cover_design_positive_prompt VARCHAR(1000) NOT NULL,
    cover_design_negative_prompt VARCHAR(1000),
    cover_design_seed_value INT UNSIGNED NOT NULL,
    cover_design_link VARCHAR(255) NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP,
    PRIMARY KEY (item_id, cover_design_id)
);

-- 新故事行內容及圖片 new_story_image
CREATE TABLE IF NOT EXISTS new_story_image (
    new_story_id MEDIUMINT UNSIGNED,
    line_id TINYINT UNSIGNED,
    tw_line_content VARCHAR(255) NOT NULL,
    en_line_content VARCHAR(720) NOT NULL,
    item_id TINYINT UNSIGNED,
    cover_design_id TINYINT UNSIGNED,
    tw_storyboard_desc VARCHAR(1500),
    en_storyboard_desc VARCHAR(4250),
    line_image_link VARCHAR(255),
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (new_story_id, line_id)
);

-- 指令 prompt（Deprecated）
CREATE TABLE IF NOT EXISTS prompt (
    prompt_id TINYINT UNSIGNED PRIMARY KEY,
    prompt_name VARCHAR(50) NOT NULL,
    version_code TINYINT UNSIGNED,
    version_desc VARCHAR(255),
    prompt_content VARCHAR(2000) NOT NULL,
    developer_id MEDIUMINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 故事問題 story_issue
CREATE TABLE IF NOT EXISTS story_issue (
    issue_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    story_id MEDIUMINT UNSIGNED,
    issue_category_id TINYINT UNSIGNED NOT NULL,
    issue_title VARCHAR(50) NOT NULL,
    issue_info VARCHAR(255),
    report_info VARCHAR(255),
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    report_time TIMESTAMP
);

-- 故事統計 story_statistics
CREATE TABLE IF NOT EXISTS story_statistics (
    statistics_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    paragraph_count TINYINT UNSIGNED,
    total_word_count SMALLINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 故事資訊 story_info
CREATE TABLE IF NOT EXISTS story_info (
    story_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    beginning_statistics_id MEDIUMINT UNSIGNED,
    middle_statistics_id MEDIUMINT UNSIGNED,
    turning_statistics_id MEDIUMINT UNSIGNED,
    ending_statistics_id MEDIUMINT UNSIGNED,
    full_text_statistics_id MEDIUMINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 新故事 new_story
CREATE TABLE IF NOT EXISTS new_story (
    new_story_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    new_story_name VARCHAR(50) NOT NULL,
    main_character_id TINYINT UNSIGNED,
    supporting_character_id TINYINT UNSIGNED,
    item_id TINYINT UNSIGNED,
    tw_new_story_content VARCHAR(1500) NOT NULL,
    en_new_story_content VARCHAR(4250),
    user_id MEDIUMINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- 0 - N
	-- 1 - Y
    favorites TINYINT DEFAULT 0 CHECK (favorites IN (0, 1)),
    valid_days SMALLINT UNSIGNED DEFAULT 1,
    expiration_time TIMESTAMP
);

-- 項目 item
CREATE TABLE IF NOT EXISTS item (
    item_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	-- 1 - 角色
	-- 2 - 道具
    item_type TINYINT NOT NULL CHECK (item_type IN (1, 2)),
    item_name VARCHAR(50) NOT NULL,
    item_info VARCHAR(255),
    original_story_id MEDIUMINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 故事類型 story_category
CREATE TABLE IF NOT EXISTS story_category (
    category_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    parent_category_id TINYINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 原故事 original_story
CREATE TABLE IF NOT EXISTS original_story (
    original_story_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    original_story_category_id TINYINT UNSIGNED,
    original_story_name VARCHAR(50) NOT NULL,
    original_story_content VARCHAR(2000) NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 使用者 user
CREATE TABLE IF NOT EXISTS user (
    user_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	-- 0 - 開發人員
	-- 1 - 一般用戶
    user_type TINYINT DEFAULT 1 CHECK (user_type IN (0, 1)),
    user_name VARCHAR(50) NOT NULL,
    user_nick_name VARCHAR(50),
    user_password VARCHAR(16) NOT NULL CHECK (LENGTH(user_password) >= 8),
    user_email VARCHAR(255),
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);

-- 金鑰費用 api_key_cost
CREATE TABLE IF NOT EXISTS api_key_cost (
    key_id TINYINT UNSIGNED,
    user_id MEDIUMINT UNSIGNED,
    usd_key_cost DECIMAL(5, 2) NOT NULL,
    twd_key_cost SMALLINT UNSIGNED,
	-- Tokens 數
	-- 圖片數
    unit ENUM('Tokens', 'Images') NOT NULL,
    quantity SMALLINT UNSIGNED NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    PRIMARY KEY (key_id, user_id)
);

-- 金鑰 api_key
CREATE TABLE IF NOT EXISTS api_key (
    key_id TINYINT UNSIGNED PRIMARY KEY,
    key_name VARCHAR(50) NOT NULL,
    key_password VARCHAR(255) NOT NULL,
    developer_id MEDIUMINT UNSIGNED,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    disable_time TIMESTAMP
);



-- ALTER TABLE ADD FOREIGN KEY 新增外鍵約束

-- 使用者 user
ALTER TABLE new_story ADD CONSTRAINT fk_new_story_user_id FOREIGN KEY (user_id) REFERENCES user(user_id);
ALTER TABLE prompt ADD CONSTRAINT fk_prompt_developer_id FOREIGN KEY (developer_id) REFERENCES user(user_id);
ALTER TABLE api_key ADD CONSTRAINT fk_api_key_developer_id FOREIGN KEY (developer_id) REFERENCES user(user_id);
ALTER TABLE api_key_cost ADD CONSTRAINT fk_api_key_cost_user_id FOREIGN KEY (user_id) REFERENCES user(user_id);

-- 原故事 original_story
ALTER TABLE item ADD CONSTRAINT fk_item_original_story_id FOREIGN KEY (original_story_id) REFERENCES original_story(original_story_id);
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_original_story_id FOREIGN KEY (story_id) REFERENCES original_story(original_story_id);
ALTER TABLE story_issue ADD CONSTRAINT fk_story_issue_original_story_id FOREIGN KEY (story_id) REFERENCES original_story(original_story_id);

-- 故事類型 story_category
ALTER TABLE original_story ADD CONSTRAINT fk_original_story_category_id FOREIGN KEY (original_story_category_id) REFERENCES story_category(category_id);
ALTER TABLE story_category ADD CONSTRAINT fk_story_category_parent_id FOREIGN KEY (parent_category_id) REFERENCES story_category(category_id);

-- 項目 item
ALTER TABLE new_story ADD CONSTRAINT fk_new_story_item_id FOREIGN KEY (item_id) REFERENCES item(item_id);
ALTER TABLE new_story ADD CONSTRAINT fk_new_story_supporting_character_id FOREIGN KEY (supporting_character_id) REFERENCES item(item_id);
ALTER TABLE new_story ADD CONSTRAINT fk_new_story_main_character_id FOREIGN KEY (main_character_id) REFERENCES item(item_id);
ALTER TABLE cover_design ADD CONSTRAINT fk_cover_design_item_id FOREIGN KEY (item_id) REFERENCES item(item_id);
ALTER TABLE new_story_image ADD CONSTRAINT fk_new_story_image_item_id FOREIGN KEY (item_id) REFERENCES item(item_id);

-- 新故事 new_story
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_new_story_id FOREIGN KEY (story_id) REFERENCES new_story(new_story_id);
ALTER TABLE story_issue ADD CONSTRAINT fk_story_issue_new_story_id FOREIGN KEY (story_id) REFERENCES new_story(new_story_id);
ALTER TABLE new_story_image ADD CONSTRAINT fk_new_story_image_story_id FOREIGN KEY (new_story_id) REFERENCES new_story(new_story_id);

-- 故事統計 story_statistics
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_beginning_statistics_id FOREIGN KEY (beginning_statistics_id) REFERENCES story_statistics(statistics_id);
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_middle_statistics_id FOREIGN KEY (middle_statistics_id) REFERENCES story_statistics(statistics_id);
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_turning_statistics_id FOREIGN KEY (turning_statistics_id) REFERENCES story_statistics(statistics_id);
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_ending_statistics_id FOREIGN KEY (ending_statistics_id) REFERENCES story_statistics(statistics_id);
ALTER TABLE story_info ADD CONSTRAINT fk_story_info_full_text_statistics_id FOREIGN KEY (full_text_statistics_id) REFERENCES story_statistics(statistics_id);

-- 故事問題類型 story_issue_category
ALTER TABLE story_issue ADD CONSTRAINT fk_story_issue_issue_category_id FOREIGN KEY (issue_category_id) REFERENCES story_issue_category(issue_category_id);
ALTER TABLE story_issue_category ADD CONSTRAINT fk_story_issue_category_parent_issue_category_id FOREIGN KEY (parent_issue_category_id) REFERENCES story_issue_category(issue_category_id);

-- 封面／設計圖 cover_design
ALTER TABLE new_story_image ADD CONSTRAINT fk_new_story_image_cover_design_id FOREIGN KEY (item_id, cover_design_id) REFERENCES cover_design(item_id, cover_design_id);

-- 金鑰 api_key
ALTER TABLE api_key_cost ADD CONSTRAINT fk_api_key_cost_key_id FOREIGN KEY (key_id) REFERENCES api_key(key_id);
