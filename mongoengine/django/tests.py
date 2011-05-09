#coding: utf-8
from django.test import TestCase
from django.conf import settings

from mongoengine import connect

class MongoTestCase(TestCase):
    """
    TestCase class that clear the collection between the tests
    """
    db_name = 'test_%s' % settings.MONGO_DATABASE_NAME
    def __init__(self, methodName='runtest'):
        self.db = connect(self.db_name)
        super(MongoTestCase, self).__init__(methodName)

    def _post_teardown(self):
        super(MongoTestCase, self)._post_teardown()
        for collection in self.db.collection_names():
            if collection == 'system.indexes':
                continue
            self.db.drop_collection(collection)

    def _fixture_setup(self):
        '''
        Overwrites this Django TestCase function to run smoothly with MongoDB.
        Without this, Django tries to create a normal database using its database dict
        '''
        pass

