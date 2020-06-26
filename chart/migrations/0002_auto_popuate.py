# chart/migrations/0002_auto_popuate.py
"""
DB ??? ??? ??? ?, csv ?? ??? DB? ????? ????.
"""
import csv
import os
from django.db import migrations
from django.conf import settings

# csv ??? ?? ? ??? ??? ??
TICKET_CLASS = 0  # ??? ??
SURVIVED = 1      # ?? ??
NAME = 2          # ??
SEX = 3           # ??
AGE = 4           # ??
EMBARKED = 10     # ???

def add_passengers(apps, schema_editor):
    Passenger = apps.get_model('chart', 'Passenger')  # (app_label, model_name)
    csv_file = os.path.join(settings.BASE_DIR, 'titanic.csv')
    with open(csv_file) as dataset:                   # ?? ?? dataset
        reader = csv.reader(dataset)                    # ?? ?? dataset? ?? ??? ??
        next(reader)  # ignore first row (headers)      # __next__() ?? ??? ? ?? ??
        for entry in reader:                            # ???? ??? ?? ??
            Passenger.objects.create(                       # DB ? ??
                name=entry[NAME],
                sex='M' if entry[SEX] == 'male' else 'F',
                survived=bool(int(entry[SURVIVED])),        # int()? ????, ?? bool()? ??
                age=float(entry[AGE]) if entry[AGE] else 0.0,
                ticket_class=int(entry[TICKET_CLASS]),      # int()? ??
                embarked=entry[EMBARKED],
            )

class Migration(migrations.Migration):
    dependencies = [                            # ?? ??
        ('chart', '0001_initial'),         # app_label, preceding migration file
    ]
    operations = [                              # ??
        migrations.RunPython(add_passengers),   # add_passengers ??? ??
    ]