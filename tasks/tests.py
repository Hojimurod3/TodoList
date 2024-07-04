# tasks/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(title='Task 1', description='Description 1')
        self.task2 = Task.objects.create(title='Task 2', description='Description 2')

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        response = self.client.get(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Description'}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, 'New Task')

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(f'/api/tasks/{self.task1.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.get(id=self.task1.id).title, 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 1)

    def test_mark_task_as_done(self):
        response = self.client.post(f'/api/tasks/{self.task1.id}/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.get(id=self.task1.id).done)
