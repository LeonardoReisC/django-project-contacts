from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |  # noqa: W504
            Q(last_name__icontains=search_value) |  # noqa: W504
            Q(phone__icontains=search_value) |  # noqa: W504
            Q(email__icontains=search_value)
        ) \
        .order_by('-id')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context=context,
    )