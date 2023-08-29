from django.shortcuts import render

bob_details = {
    "name": "bob",
    "hoppies": ["coding", "running"],
    "gender": "male"
}

alice_details = {
    "name": "alice",
    "hoppies": ["reading", "swimming"],
    "gender": "female"
}


# Create your views here.
def profile_user(request, name):
    context = {}
    if name == 'bob':
        context = bob_details
    elif name == 'alice':
        context = alice_details

    return render(request, 'profile_user.html', context)
