from django.shortcuts import get_object_or_404
from .models import FoodCard

def view_cart(request):
    cart = request.session.get("cart", {})
    if not cart:
        return {"groupped_items": {},
            "totals": {"proteins": 0, "carbs": 0, "fats": 0}}
    totals = {
        'proteins':0,
        'carbs':0,
        'fats': 0
    }
    groupped_items = {}
    for cardpk, quantity in cart.items():
        card = get_object_or_404(FoodCard, pk=int(cardpk))
        if card.category not in groupped_items:
            groupped_items[card.category] = {}
        groupped_items[card.category][card.title] = [quantity, card.image]
        totals['proteins'] += card.proteins * quantity
        totals['carbs'] += card.carbohydrates * quantity
        totals['fats'] += card.fats * quantity 
    return {
        "groupped_items": groupped_items,
        "totals": totals
    }