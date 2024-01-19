from django.db import models

# 故事問題類型 StoryIssueCategory
class StoryIssueCategory(models.Model):
    issue_category_id = models.PositiveSmallIntegerField(primary_key=True)
    issue_category_name = models.CharField(max_length=10, null=False)
    parent_issue_category_id = models.PositiveSmallIntegerField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'story_issue_category'

# 封面／設計圖 CoverDesign
class CoverDesign(models.Model):
    item_id = models.PositiveSmallIntegerField()
    cover_design_id = models.PositiveSmallIntegerField()
    cover_design_prompt_desc = models.CharField(max_length=2000, null=False)
    cover_design_seed_value = models.PositiveIntegerField(null=False)
    cover_design_link = models.CharField(max_length=255, null=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'cover_design'
        unique_together = (('item_id', 'cover_design_id'),)

# 新故事行內容及圖片 NewStoryImage
class NewStoryImage(models.Model):
    new_story_id = models.PositiveIntegerField()
    line_id = models.PositiveSmallIntegerField()
    tw_line_content = models.CharField(max_length=255, null=False)
    en_line_content = models.CharField(max_length=720, null=False)
    item_id = models.PositiveSmallIntegerField()
    cover_design_id = models.PositiveSmallIntegerField()
    tw_storyboard_desc = models.CharField(max_length=1500, null=True, blank=True)
    en_storyboard_desc = models.CharField(max_length=4250, null=True, blank=True)
    line_image_link = models.CharField(max_length=255, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'new_story_image'
        unique_together = (('new_story_id', 'line_id'),)

# 故事問題 StoryIssue
class StoryIssue(models.Model):
    issue_id = models.PositiveSmallIntegerField(primary_key=True, auto_created=True)
    story_id = models.PositiveIntegerField()
    issue_category_id = models.PositiveSmallIntegerField(null=False)
    issue_title = models.CharField(max_length=50, null=False)
    issue_info = models.CharField(max_length=255, null=True, blank=True)
    report_info = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    report_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'story_issue'

# 故事統計 StoryStatistics
class StoryStatistics(models.Model):
    statistics_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    paragraph_count = models.PositiveSmallIntegerField()
    total_word_count = models.PositiveSmallIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'story_statistics'

# 故事資訊 StoryInfo
class StoryInfo(models.Model):
    story_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    beginning_statistics_id = models.PositiveIntegerField()
    middle_statistics_id = models.PositiveIntegerField()
    turning_statistics_id = models.PositiveIntegerField()
    ending_statistics_id = models.PositiveIntegerField()
    full_text_statistics_id = models.PositiveIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'story_info'

# 新故事 NewStory
class NewStory(models.Model):
    new_story_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    new_story_name = models.CharField(max_length=50, null=False)
    main_character_id = models.PositiveSmallIntegerField()
    supporting_character_id = models.PositiveSmallIntegerField()
    item_id = models.PositiveSmallIntegerField()
    tw_new_story_content = models.CharField(max_length=1500, null=False)
    en_new_story_content = models.CharField(max_length=4250, null=True, blank=True)
    user_id = models.PositiveIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    favorites = models.PositiveSmallIntegerField(default=0)
    valid_days = models.PositiveSmallIntegerField(default=1)
    expiration_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'new_story'

# 項目 Item
class Item(models.Model):
    item_id = models.PositiveSmallIntegerField(primary_key=True, auto_created=True)
    item_type = models.PositiveSmallIntegerField(null=False)
    item_name = models.CharField(max_length=50, null=False)
    item_info = models.CharField(max_length=255, null=True, blank=True)
    original_story_id = models.PositiveSmallIntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'item'

# 故事類型 StoryCategory
class StoryCategory(models.Model):
    category_id = models.PositiveSmallIntegerField(primary_key=True, auto_created=True)
    category_name = models.CharField(max_length=50, null=False)
    parent_category_id = models.PositiveSmallIntegerField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'story_category'

# 原故事 OriginalStory
class OriginalStory(models.Model):
    original_story_id = models.PositiveSmallIntegerField(primary_key=True, auto_created=True)
    original_story_category_id = models.PositiveSmallIntegerField()
    original_story_name = models.CharField(max_length=50, null=False)
    original_story_content = models.CharField(max_length=2000, null=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    disable_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'original_story'
