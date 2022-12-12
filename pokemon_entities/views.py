import folium

from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def choose_image_url(pokemon, request):
    pokemon_img = DEFAULT_IMAGE_URL
    if pokemon.image:
        pokemon_img = request.build_absolute_uri(pokemon.image.url)
    return pokemon_img


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    query_time = localtime()
    for pokemon_entity in PokemonEntity.objects.filter(
                                                appeared_at__lte=query_time,
                                                disappeared_at__gte=query_time,
                                                ):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            choose_image_url(pokemon_entity.pokemon, request)
            )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': choose_image_url(pokemon, request),
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    query_time = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entities.filter(
                                                pokemon=pokemon,
                                                appeared_at__lte=query_time,
                                                disappeared_at__gte=query_time,
                                                ):
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            choose_image_url(pokemon, request)
        )
    pokemon_card = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': choose_image_url(pokemon, request),
    }

    pokemon_next_evolution = pokemon.next_evolutions.all().first()
    if pokemon_next_evolution:
        pokemon_card['next_evolution'] = {
            'pokemon_id': pokemon_next_evolution.id,
            'title_ru': pokemon_next_evolution.title_ru,
            'img_url': choose_image_url(pokemon_next_evolution, request)
        }
    if pokemon.previous_evolution:
        pokemon_card['previous_evolution'] = {
            'pokemon_id': pokemon.previous_evolution.id,
            'title_ru': pokemon.previous_evolution.title_ru,
            'img_url': choose_image_url(pokemon.previous_evolution, request)
        }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_card
    })
