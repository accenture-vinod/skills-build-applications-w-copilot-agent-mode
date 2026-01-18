from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        self.activity = Activity.objects.create(user=self.user, type='Cardio', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_user(self):
        self.assertEqual(self.activity.user.email, 'spiderman@marvel.com')

    def test_leaderboard_user(self):
        self.assertEqual(self.leaderboard.user.name, 'Spider-Man')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Web Swing')
