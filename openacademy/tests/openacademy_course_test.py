# -*- encoding: utf-8 -*-

from odoo.tests.common import TransactionCase
'''
Global test to openacademy course model.
Test create course and trigger contraints.
'''

class GlobalTestOpenAcademyCourse(TransactionCase):

    #Method seudo-constructor of test setUp
    def setUp(self):
        # Define global variables to tests methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.variable = 'hello world'
        self.course = self.env['openacademy.course']

    #Method of class that don't is test
    def create_course(
        self, course_name, course_description, course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    #Method of test starts with 'def test_*(self):'
    def test_01_same_name_description(self):
        '''
        Test create a course with same name and description.
        To test contraint of name different to description.
        '''
        self.create_course('test', 'test', None)
