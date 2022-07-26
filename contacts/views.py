from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def contacts(request, id):
    listings = Contact.objects.all()
    if request.method==('POST'):
        name = request.POST('name')
        email = request.POST('email')
        phone = request.POST('phone')
        message = request.POST('message')
        user_id = request.POST('user_id')
        realtor_email = request.POST('realtor_email')

        if request.user.is_authenticated:
            user_id= request.user.id
            has_contacted = Contact.objects.all().filter(user_id= user_id,listing_id =id)
            if has_contacted:
                message.error(request, 'you have already made an inquirfy for this house')
                return redirect('list'+ id)

            contact = Contact(
               listings=listings,
               listing_id = id,
               name = name,
               email = email,
               phone = phone,
               message = message,
               user_id = user_id)

            contact.save()

    # Sendind email
            send_mail(
            'property listing inquiry',
            'there has been an inquiry for' + listings + 'sign into the admin panel for more info',
            'traversy.brad@gmail.com',
            [realtor_email, 'techguyinfo@gmail.com'],
            failed_silently= False
            )
    return render(request, 'list/contact.html')