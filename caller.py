import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer
from typing import List
from django.db.models import Case, When, Value
from main_app.choices import OperationSystemChoices

# Create and check models
# Run and print your queries

def show_highest_rated_art():
    highest_rating = ArtworkGallery.objects.order_by('-rating','id').first()
    return f"{highest_rating.art_name} is the highest-rated art with a {highest_rating.rating} rating!"

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art,second_art])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop():
    highest_price = Laptop.objects.order_by('-price', '-id').first()
    return f"{highest_price.brand} is the most expensive laptop available for {highest_price.price}$!"

def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)

def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)

def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Dell", "Apple", "Acer"]).update(memory=16)

def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoices.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoices.MACOS)),
            When(brand="Lenovo", then=Value(OperationSystemChoices.CHROMEOS)),
            When(brand__in=["Dell", "Acer"], then=Value(OperationSystemChoices.LINUX)),
        )
    )

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players():
    default_value = ChessPlayer._meta.get_field('title').default
    ChessPlayer.objects.filter(title=default_value).delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)

def change_chess_games_lost():
    default_value = ChessPlayer._meta.get_field('title').default
    ChessPlayer.objects.filter(title=default_value).update(games_lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.update(game_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")

def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300,2399)).update(title="IM")

def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="FM")

def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lt=2200).update(title="regular player")

