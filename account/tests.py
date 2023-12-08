from django.test import TestCase

# Create your tests here.
# from django.contrib.auth import get_user_model
# from .models import UserProfile

# class UserCreateViewTest(TestCase):
#     def test_create_user(self):
#         data = {
#             "username": "johndoe@2023",
#             "email": "johndoe@example.com",
#             "first_name":"Jhone",
#             "last_name":"Doe",
#             "password1": "$@L(4RJw64lk",
#             "password2": "$@L(4RJw64lk",
#         }
#         response = self.client.post(reverse("user-create"), data=data)
#         self.assertEqual(response.status_code, 302)  # redirect
#         self.assertEqual(User.objects.count(), 1)
#         user = User.objects.get(username="johndoe@2023")
#         self.assertEqual(user.email, data["email"])
#         self.assertTrue(user.check_password(data["password1"]))
#         profile = UserProfile.objects.get(user="johndoe@2023")
