from django.db import models

class OriginalStory(models.Model):
    original_story_id = models.AutoField(primary_key=True)
    original_story_category = models.ForeignKey('StoryCategory', models.DO_NOTHING, blank=True, null=True)
    original_story_name = models.CharField(max_length=50)
    original_story_content = models.CharField(max_length=2000)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'original_story'

class StoryCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_category'

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_type = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_info = models.CharField(max_length=255, blank=True, null=True)
    original_story = models.ForeignKey('OriginalStory', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

class NewStory(models.Model):
    new_story_id = models.AutoField(primary_key=True)
    new_story_name = models.CharField(max_length=50)
    main_character = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    supporting_character = models.ForeignKey(Item, models.DO_NOTHING, related_name='newstory_supporting_character_set', blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, related_name='newstory_item_set', blank=True, null=True)
    tw_new_story_content = models.CharField(max_length=1500)
    en_new_story_content = models.CharField(max_length=4250, blank=True, null=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    favorites = models.IntegerField(blank=True, null=True)
    valid_days = models.PositiveSmallIntegerField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_story'

class StoryInfo(models.Model):
    story = models.OneToOneField(OriginalStory, models.DO_NOTHING, primary_key=True)
    beginning_statistics = models.ForeignKey('StoryStatistics', models.DO_NOTHING, blank=True, null=True)
    middle_statistics = models.ForeignKey('StoryStatistics', models.DO_NOTHING, related_name='storyinfo_middle_statistics_set', blank=True, null=True)
    turning_statistics = models.ForeignKey('StoryStatistics', models.DO_NOTHING, related_name='storyinfo_turning_statistics_set', blank=True, null=True)
    ending_statistics = models.ForeignKey('StoryStatistics', models.DO_NOTHING, related_name='storyinfo_ending_statistics_set', blank=True, null=True)
    full_text_statistics = models.ForeignKey('StoryStatistics', models.DO_NOTHING, related_name='storyinfo_full_text_statistics_set', blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_info'

class StoryStatistics(models.Model):
    statistics_id = models.AutoField(primary_key=True)
    paragraph_count = models.PositiveIntegerField(blank=True, null=True)
    total_word_count = models.PositiveSmallIntegerField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_statistics'

class StoryIssue(models.Model):
    issue_id = models.SmallAutoField(primary_key=True)
    story = models.ForeignKey(OriginalStory, models.DO_NOTHING, blank=True, null=True)
    issue_category = models.ForeignKey('StoryIssueCategory', models.DO_NOTHING)
    issue_title = models.CharField(max_length=50)
    issue_info = models.CharField(max_length=255, blank=True, null=True)
    report_info = models.CharField(max_length=255, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    report_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_issue'

class StoryIssueCategory(models.Model):
    issue_category_id = models.PositiveIntegerField(primary_key=True)
    issue_category_name = models.CharField(max_length=10)
    parent_issue_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_issue_category'

class CoverDesign(models.Model):
    item = models.OneToOneField('Item', models.DO_NOTHING, primary_key=True)  # The composite primary key (item_id, cover_design_id) found, that is not supported. The first column is selected.
    cover_design_id = models.PositiveIntegerField(unique=True)
    cover_design_prompt_desc = models.CharField(max_length=2000)
    cover_design_seed_value = models.PositiveIntegerField()
    cover_design_link = models.CharField(max_length=255)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cover_design'
        unique_together = (('item', 'cover_design_id'),)

class NewStoryImage(models.Model):
    new_story = models.OneToOneField(NewStory, models.DO_NOTHING, primary_key=True)  # The composite primary key (new_story_id, line_id) found, that is not supported. The first column is selected.
    line_id = models.PositiveIntegerField()
    tw_line_content = models.CharField(max_length=255)
    en_line_content = models.CharField(max_length=720)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    cover_design = models.ForeignKey(CoverDesign, models.DO_NOTHING, to_field='cover_design_id', blank=True, null=True)
    tw_storyboard_desc = models.CharField(max_length=1500, blank=True, null=True)
    en_storyboard_desc = models.CharField(max_length=4250, blank=True, null=True)
    line_image_link = models.CharField(max_length=255, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_story_image'
        unique_together = (('new_story', 'line_id'),)
