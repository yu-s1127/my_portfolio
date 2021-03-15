from django.db import models


class Title(models.Model):
    """
    Top page用のタイトル
    """
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField(
        'サブタイトル',
        max_length=100,
        null=True,
        blank=True)


class Profile(models.Model):
    """
    About my profile
    """
    name = models.CharField('名前', max_length=100)
    job = models.CharField('仕事', max_length=100, null=True, blank=True)
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField(
        'twitter',
        max_length=100,
        null=True,
        blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    About my skills
    """
    name = models.CharField('スキル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name


class Experience(models.Model):
    """
    About my experience
    """
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation
