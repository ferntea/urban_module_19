from django.core.management.base import BaseCommand
from task1.models import Game

class Command(BaseCommand):
    help = 'Populate the database with video games'

    def handle(self, *args, **kwargs):
        games = [
            {"title": "Adventure Quest", "cost": 29.99, "size": 1.5, "description": "An epic adventure!", "age_limited": 0},
            {"title": "Mystery Dungeon", "cost": 19.99, "size": 2.0, "description": "Solve the mystery!", "age_limited": 1},
            {"title": "Battle Royale", "cost": 39.99, "size": 3.0, "description": "Survive the battle!", "age_limited": 1},
            {"title": "Space Explorer", "cost": 49.99, "size": 2.5, "description": "Explore the universe!", "age_limited": 0},
            {"title": "Zombie Survival", "cost": 34.99, "size": 4.0, "description": "Survive the zombie apocalypse!", "age_limited": 1},
            {"title": "Racing Challenge", "cost": 24.99, "size": 1.2, "description": "Race against the clock!", "age_limited": 0},
            {"title": "Fantasy World", "cost": 44.99, "size": 3.5, "description": "Enter a world of magic!", "age_limited": 1},
            {"title": "Puzzle Master", "cost": 14.99, "size": 1.0, "description": "Solve challenging puzzles!", "age_limited": 0},
            {"title": "Sports Manager", "cost": 29.99, "size": 2.0, "description": "Manage your own team!", "age_limited": 0},
        ]

        for game_data in games:
            game, created = Game.objects.update_or_create(
                title=game_data["title"],
                defaults={
                    "cost": game_data["cost"],
                    "size": game_data["size"],
                    "description": game_data["description"],
                    "age_limited": game_data["age_limited"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Game "{game.title}" created.'))
            else:
                self.stdout.write(self.style.WARNING(f'Game "{game.title}" updated.'))
