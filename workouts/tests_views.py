from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Workout, Fitness, Sport, Level, UserProfile
from exercises.models import Exercise, Bodypart
from django.contrib.messages import get_messages

class WorkoutViewsTests(TestCase):
    
    def setUp(self):
        """Set up user, workout and other required data."""
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.fitness = Fitness.objects.create(name='Strength')
        self.sport = Sport.objects.create(name='Football')
        self.level = Level.objects.create(name='Beginner')
        self.workout = Workout.objects.create(
            name='Test Workout',
            fitness=self.fitness,
            sport=self.sport,
            level=self.level,
            description='Test description'
        )
        self.exercise = Exercise.objects.create(name='Push-up', description='Test exercise')
        self.bodypart = Bodypart.objects.create(name='Chest')
        self.workout.exercises.add(self.exercise)

    def test_all_workouts_view(self):
        """Test all workouts view."""
        response = self.client.get(reverse('workouts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')

    def test_workout_details_view(self):
        """Test workout details view."""
        response = self.client.get(reverse('workout_details', args=[self.workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')
        self.assertContains(response, 'Test exercise')

    def test_create_workout_view(self):
        """Test create workout view."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('create_workout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Workout')

    def test_save_workout_view(self):
        """Test save workout functionality."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('save_workout', args=[self.workout.id]), {'next': reverse('workouts')})
        self.assertRedirects(response, reverse('workouts'))
        self.user_profile.refresh_from_db()
        self.assertIn(self.workout, self.user_profile.saved_workouts.all())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Workout saved successfully!")

    def test_update_workout_view(self):
        """Test update workout view."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('update_workout', args=[self.workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update Workout')
        
        # Test POST request for updating
        response = self.client.post(reverse('update_workout', args=[self.workout.id]), {
            'name': 'Updated Workout',
            'fitness': self.fitness.id,
            'sport': self.sport.id,
            'level': self.level.id,
            'description': 'Updated description'
        })
        self.workout.refresh_from_db()
        self.assertEqual(self.workout.name, 'Updated Workout')
        self.assertRedirects(response, reverse('workout_details', args=[self.workout.id]))

    def test_delete_workout_view(self):
        """Test delete workout view."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('delete_workout', args=[self.workout.id]))
        self.assertRedirects(response, reverse('profile'))
        with self.assertRaises(Workout.DoesNotExist):
            Workout.objects.get(id=self.workout.id)

    def test_track_workout_selector_view(self):
        """Test track workout selector view."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('track_workout_selector', args=[self.workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Track Workout')

    def test_reset_workout_view(self):
        """Test reset workout functionality."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('reset_workout'))
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': True})
        self.assertEqual(self.client.session.get('new_workout'), {})

    def test_update_workout_session_view(self):
        """Test update workout session functionality."""
        self.client.login(username='testuser', password='password')
        data = {'new_workout': {'1': {'exercise_id': self.exercise.id, 'sets': 3, 'reps': 10, 'day': 1, 'week': 1}}}
        response = self.client.post(reverse('update_workout_session'), data=json.dumps(data), content_type='application/json')
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'status': 'success', 'message': 'Workout data saved to session'})
        self.assertEqual(self.client.session.get('new_workout'), data['new_workout'])

