from django.test import TestCase
from .models import StudentModel


class HomePageTests(TestCase):
    def test_student_without_uploaded_image_uses_existing_default(self):
        student = StudentModel.objects.create(std_name='Test student', course='Test course')

        response = self.client.get('/')

        self.assertContains(response, student.image.url)
        image_response = self.client.get(student.image.url)
        self.assertEqual(image_response.status_code, 200)
