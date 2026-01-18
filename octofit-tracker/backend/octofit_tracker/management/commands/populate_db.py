from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workout1 = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        workout2 = Workout.objects.create(name='Gadget Training', description='Using superhero gadgets')
        workout1.suggested_for.set([users[0], users[1]])
        workout2.suggested_for.set([users[2], users[3]])

        # Create activities
        Activity.objects.create(user=users[0], type='Cardio', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Strength', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Agility', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Endurance', duration=40, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
