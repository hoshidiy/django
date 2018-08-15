import datetime
from django.db import models
from django.utils import timezone


class Person(models.Model):
    """人"""
    name = models.CharField('氏名', max_length=50)
    
    def __str__(self):
        return str(self.name) + ' <ID:' + str(self.id) + '>'

class HayagaeriPlan(models.Model):
    """早帰り予定"""
    plan = models.CharField('早帰り予定', max_length=50)
    
    def __str__(self):
        return str(self.plan)

class HayagaeriResult(models.Model):
    """早帰り実績"""
    result = models.CharField('早帰り実績', max_length=50)
    
    def __str__(self):
        return str(self.result)

class Schedule(models.Model):
    """スケジュール"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    hayagaeri_plan = models.ForeignKey(HayagaeriPlan, on_delete=models.CASCADE)
    hayagaeri_result = models.ForeignKey(HayagaeriResult, on_delete=models.CASCADE)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return str(self.person) + ' <Sche ID:' + str(self.id) + '>' + ' <Sche Date:' + str(self.date) + '>'
