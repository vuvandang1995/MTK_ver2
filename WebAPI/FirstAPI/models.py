from django.db import models


class Users(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    receive_email = models.IntegerField(default=1)
    status = models.IntegerField(default=0)
    created = models.DateTimeField()
    noti_noti = models.IntegerField(default=0)
    noti_chat = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'users'


class Topics(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    description = models.TextField()
    departmentid = models.ForeignKey('Departments', models.SET_NULL, null=True, db_column='departmentid')

    class Meta:
        managed = True
        db_table = 'topics'


class Departments(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = 'departments'


class Agents(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    receive_email = models.IntegerField(default=1)
    password = models.CharField(max_length=255)
    admin = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    noti_noti = models.IntegerField(default=0)
    noti_chat = models.IntegerField(default=0)
    departmentid = models.ForeignKey('Departments', models.SET_NULL, null=True, db_column='departmentid')

    class Meta:
        managed = True
        db_table = 'agents'


class TopicAgent(models.Model):
    agentid = models.ForeignKey('Agents', models.CASCADE, db_column='agentid')
    topicid = models.ForeignKey('Topics', models.CASCADE, db_column='topicid')

    class Meta:
        managed = True
        db_table = 'topic_agent'


class Tickets(models.Model):
    title = models.CharField(max_length=255)
    chat = models.CharField(max_length=30, null=True)
    content = models.TextField()
    sender = models.ForeignKey('Users', models.CASCADE, db_column='sender')
    topicid = models.ForeignKey('Topics', models.DO_NOTHING, db_column='topicid')
    status = models.IntegerField(default=0)
    datestart = models.DateTimeField()
    dateend = models.DateTimeField()
    attach = models.FileField(null=True, blank=True, upload_to='photos')

    class Meta:
        managed = True
        db_table = 'tickets'
