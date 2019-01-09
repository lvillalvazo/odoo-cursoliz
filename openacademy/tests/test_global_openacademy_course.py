# -*- encoding: utf-8 -*-

from psycopg2 import IntegrityError

from odoo.tests.common import TransactionCase
from odoo.tools.misc import mute_logger


class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global test to create openacademy course model.
    Test create course and trigger contraints.
    '''

    # Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to tests methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    # Method of class that don't is test
    def create_course(
            self, course_name, course_description, course_responsible_id):
        # create a course with parameters received
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    # Method of test starts with 'def test_*(self):'

    # Mute the error odoo.sql_db to avoid it in log
    @mute_logger('odoo.sql_db')
    def test_10_same_name_description(self):
        '''
        Test create a course with same name and description.
        To raise constraint of name different to description.
        '''
        # Error raised Expected with message expected.
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates'
                ' check constraint "openacademy_course_name_description_check"'
                ):
            # Create a course with same name and description to raise error
            self.create_course('test', 'test', None)

    @mute_logger('odoo.sql_db')
    def test_20_two_courses_same_name(self):
        '''
        Test to create two courses with same name.
        To raise constraint of unique name
        '''
        new_id = self.create_course('test1', 'test_description', None)
        print("Nuevo Id: %s", new_id)

        with self.assertRaisesRegexp(
            IntegrityError,
            'duplicate key value violates unique constraint '
            '"openacademy_course_name_unique"'
        ):
            new_id2 = self.create_course('test1', 'test description', None)
            print("Nuevo Id 2: %s ", new_id2)

        # with self.assertRaisesRegexp(
                # IntegrityError,
                # 'duplicate key value violates unique constraint "openacademy_course_name_unique"'
                # ):
                # new_id2 = self.create_course('test1', 'test_description', None)
                # print("Nuevo Id 2: %s", new_id2)

    def test_15_duplicate_course(self):
        '''
        Test to duplicate a course and check that work fine.
        '''
        course = self.env.ref('openacademy.course0')
        course_id = course.copy()
        print('Course Id: %s', course_id)
