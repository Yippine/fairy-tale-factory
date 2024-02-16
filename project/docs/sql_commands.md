# SQL Commands Full Guide

## 調整 Workbench 安全模式
```sql
SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;
```
- 禁用或啟用 Workbench 的安全更新模式。默認啟用以防止意外修改。

## 調整外鍵約束檢核
```sql
SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;
```
- 禁用或啟用外鍵約束檢查。在進行大規模資料更新或導入時，禁用可以提升效率。

## 基本 SELECT 查詢
```sql
SELECT column_names FROM table_name WHERE condition;
```
- 查詢資料表中符合條件的資料列。

## 插入數據
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
- 向資料表中插入數據。

## 更新數據
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```
- 更新資料表中符合條件的數據。

## 刪除數據
```sql
DELETE FROM table_name WHERE condition;
```
- 刪除資料表中符合條件的數據。

## 建立新的資料表
```sql
CREATE TABLE table_name (column1 datatype, column2 datatype, ...);
```
- 建立新的資料表，並指定列名和數據類型。

## 刪除資料表
```sql
DROP TABLE table_name;
```
- 刪除指定的資料表。

## 建立索引
```sql
CREATE INDEX index_name ON table_name (column_name);
```
- `index_name`：指定索引的名稱。
- `table_name`：指定要建立索引的表格名稱。
- `column_name`：指定要建立索引的欄位名稱。
- 建立索引可以提高資料檢索效率，尤其是在大量資料的表格中。

## 建立唯一索引
```sql
CREATE UNIQUE INDEX index_name ON table_name (column_name);
```
- 確保索引列中的數據是唯一的，防止重複值。

## 查看表格的索引
```sql
SHOW INDEX FROM table_name;
```
- 查看指定表格的所有索引資訊。

## 刪除索引
```sql
DROP INDEX index_name ON table_name;
```
- 刪除指定的索引。

## 建立視圖
```sql
CREATE VIEW view_name AS SELECT column_name FROM table_name WHERE condition;
```
- `view_name`：視圖的名稱。
- 簡化複雜的查詢，通過建立視圖來提供一個虛擬的表格。

## 刪除視圖
```sql
DROP VIEW view_name;
```
- 刪除指定的視圖。

## 建立聯合索引
```sql
CREATE INDEX index_name ON table_name (column1, column2);
```
- 在多個列上建立索引，用於優化涉及這些列的查詢性能。

## 使用前綴索引
```sql
ALTER TABLE table_name ADD INDEX index_name (column_name(10));
```
- 在指定列的前幾個字符上建立索引，適合於長文本欄位。
