import pandas as pd
import sqlite3
from django.core.management.base import BaseCommand
from datetime import date

from data.models import StateData, CountyData


class Command(BaseCommand):
    def handle(self, *args, **options):
        us_ts = pd.read_csv(
            'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
        us_ts = us_ts.drop(columns=['fips'])

        for i in us_ts.iterrows():
            CountyData.objects.create(
                cdate=i[1][0],
                county=i[1][1],
                state=i[1][2],
                cases=i[1][3],
                deaths=i[1][4]
            )
        db = r"db.sqlite3"
        conn = None

        conn = sqlite3.connect(db)
        us_ts.to_sql('usTimeSeries', conn, index=False, if_exists='replace')
        cur = conn.cursor()
        today = date.today()
        df = pd.read_sql_query(
            "SELECT * FROM usTimeSeries where date="+today.strftime("%b-%d-%Y"), conn)
        us = df.groupby(['state']).sum()

        for i in us.iterrows():
            StateData.objects.create(
                state=i[0],
                cases=i[1][0],
                deaths=i[1][1]
            )

        self.stdout.write('job complete')
