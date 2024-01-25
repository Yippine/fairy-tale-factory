# 顯示故事類型階層 v1
SELECT s1.category_id,
       s1.category_name,
       s2.category_id,
       s2.category_name
FROM   story_category s1
       LEFT JOIN story_category s2
              ON s1.parent_category_id = s2.category_id;

# 顯示故事類型階層 v2
SELECT sc1.category_id   AS Parent_ID,
       sc1.category_name AS Parent_Name,
       sc2.category_id   AS Child_ID,
       sc2.category_name AS Child_Name
FROM   story_category AS sc1
       LEFT JOIN story_category AS sc2
              ON sc1.category_id = sc2.parent_category_id
WHERE  sc1.parent_category_id IS NULL
UNION
SELECT sc3.parent_category_id,
       (SELECT category_name
        FROM   story_category
        WHERE  category_id = sc3.parent_category_id),
       sc3.category_id,
       sc3.category_name
FROM   story_category AS sc3
WHERE  sc3.parent_category_id IS NOT NULL
ORDER  BY parent_id,
          child_id;

# 依照故事名稱顯示故事類型階層
SELECT o.original_story_name,
       s.category_name,
       t.parent_category_name
FROM   original_story o
       LEFT JOIN story_category s
              ON o.original_story_category_id = s.category_id
       LEFT JOIN (SELECT s1.category_id   AS child_category_id,
                         s1.category_name AS child_category_name,
                         s2.category_id   AS parent_category_id,
                         s2.category_name AS parent_category_name
                  FROM   story_category s1
                         LEFT JOIN story_category s2
                                ON s1.parent_category_id = s2.category_id) t
              ON s.category_name = t.child_category_name;

# 依照項目名稱顯示故事類型階層
SELECT i.item_id,
       s.category_name,
       o.original_story_name,
       CASE
         WHEN i.item_type = 1 THEN '角色'
         WHEN i.item_type = 2 THEN '道具'
         ELSE '其他'
       -- 如果 item_type 不是 1 或 2，你可以自行定義返回的值
       END AS item_category,
       i.item_name
FROM   item i
       LEFT JOIN original_story o
              ON i.original_story_id = o.original_story_id
       LEFT JOIN story_category s
              ON o.original_story_category_id = s.category_id;
