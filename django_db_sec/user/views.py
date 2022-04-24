from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from random import choice
from user.helperfunctions import generateFernet, encrypt, decrypt
from .models import person

# Global key
key = b"7ZGS7-c5EdesRwUUkCfHxIJyVMbAW7rT1Fk6ethFu4c="

# Submitting the username page
def submitPage(request):
    global key
    globalf = generateFernet(key)

    if request.method == "GET":
        response = render(request, "submit.html")
        return response

    if request.method == "POST":
        # Getting username
        username = request.POST.get("email")

        # Setting context for rendering
        print("Submitted = ", username)
        response = render(request, "submit.html")

        # Encrypting username and curKey and then appending curKey to username
        username = username.encode()
        username = encrypt(globalf, username)
        curObj = person(name=username)
        curObj.save(curObj)
        print("Name stored in database = ", username)

        return response


# Displaying the decrypted names
def displayPage(request):
    if request.method == "GET":
        global key
        globalf = generateFernet(key)
        curList = []
        for i in person.objects.all():
            curName = i.name[2:-1].encode()
            curName = decrypt(globalf, curName).decode()
            curList.append([str(i.id) + "\t" + curName, i.name])
        context = {
            "users": curList,
        }
        return render(request, "home.html", context)
    else:
        pass
