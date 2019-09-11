from django.db import models


class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='姓名')
    age=models.IntegerField(verbose_name='年龄')
    height=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高',null=True)
    birthday=models.DateField(verbose_name='生日',auto_now=True)
    def __str__(self):
        return str(self.id)
# Create your models here.
    class Meta:
        db_table='person'
        verbose_name='用户'
        verbose_name_plural=verbose_name
        # ordering=['age',]

class Publish(models.Model):
    name=models.CharField(max_length=32,verbose_name='出版社')
    address=models.CharField(max_length=32,verbose_name='地址')

    class Meta:
        db_table='publish'
        verbose_name='出版社'
        verbose_name_plural=verbose_name


class Book(models.Model):
    name=models.CharField(max_length=32,verbose_name='图书')
    publish=models.ForeignKey(to=Publish,to_field='id',on_delete=models.PROTECT)
    class Meta:
        db_table='book'
        verbose_name='图书'
        verbose_name_plural=verbose_name

    # to 设置关联表
    # to_field 关联表要关联的键名，默认为关联表中的id，可以不写
    # on_delete 当删除关联表中的数据的时候，从表做什么行为，
    # CASCADE  当关联表中数据删除的时候，外键所在表中的数据也会被删除
    # SET_NULL  当关联表中数据删除的时候，外键所在表中的外键设置为空
    # SET_DEFAULT  当关联表中数据删除的时候，外键所在表中的外键设置一个默认值
    # PROTECT 关联保护，当关联表的数据被删除的时候，报异常，
    # DO_NOTHING  当关联表中数据删除的时候，外键所在的表不做任何事情
    #  级联 操作