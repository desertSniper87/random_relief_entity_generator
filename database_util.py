from peewee import *

mysql_db = MySQLDatabase('relief_db', user='dbuser', password='1234', host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = mysql_db

class Benefeciary(BaseModel):
    district_code  = CharField(max_length=1)
    upazila_code = CharField(max_length=1)
    name = CharField(max_length=15)
    father_or_husband = CharField(max_length=15)
    father_husband_name = CharField(max_length=15)
    dob = DateField()
    age  = CharField(max_length=2)
    gender = CharField(max_length=15)
    occupation  = CharField(max_length=127)
    nid = CharField(unique=True, max_length=17, primary_key=True)
    mobile_number = CharField(max_length=11)
    nos_family_member = CharField(max_length=1)
    social_security_current = CharField(max_length=63)
    social_security_application = CharField(max_length=15, default='ওএমএস')
    district = CharField(max_length=15)
    upazila = CharField(max_length=15)
    union = CharField(max_length=15)
    ward = CharField(max_length=15)
    village = CharField(max_length=15)
    road  = CharField(max_length=15)

def getDbObj():
    mysql_db.connect()
    mysql_db.create_tables([Benefeciary])

    return mysql_db
