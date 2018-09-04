# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class DivarScrapyGetlastpostdatePipeline(object):
    def open_spider(self, spider):
        hostname = '***'
        username = '***'  # the username when you create the database
        password = '***'  # change to your password
        database = '***'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute('''
            DO
                $do$
                BEGIN
                IF Not Exists(select * from last_lastpostdate where category={1}) THEN
                   insert into last_lastpostdate values ({0},{1},'{2}',{3});
                ELSE 
                   UPDATE last_lastpostdate
                    SET lastpostdate = '{0}'
                    WHERE category='{1}';
                END IF;
                END
                $do$ 

            '''.format(item['lastpostdate'],
                       item['category'],
                       item['originsite'],
                       item['updatetime']))
        self.connection.commit()
        return item
