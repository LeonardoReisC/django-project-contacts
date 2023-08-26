from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
def create(request):
    heading = 'Create '
    site_title = f'{heading}- '

    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'site_title': site_title,
            'title': heading,
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context,
        )

    context = {
        'site_title': site_title,
        'title': heading,
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    )


def update(request, contact_id):
    heading = 'Update '
    site_title = f'{heading}- '

    form_action = reverse('contact:update', args=(contact_id,))

    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {
            'site_title': site_title,
            'title': heading,
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context,
        )

    context = {
        'site_title': site_title,
        'title': heading,
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    )