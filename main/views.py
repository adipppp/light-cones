from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'On the Fall of an Aeon',
        'amount': 1,
        'rarity': 5,
        'path': 'Destruction',
        'description': '''
            It began with a flash of light.
            One by one, they fell as the threat of expiration loomed over them.
            They had to stop self-replicating and rushed to embrace each other, trying to offer the right to reproduce in exchange for a possibility of survival.
            They held hands in a show of unprecedented unity.
            …But the Paths met an abrupt end, and they were headed to a true death.
            '''
    }

    return render(request, "main.html", context)