from django.views.generic import CreateView
from .models import Comment
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactCreate(CreateView):
    model = Comment
    form_class = ContactForm
    template_name = 'contact/contactForm.html'
    success_url = reverse_lazy("index")

    def save(self):
        data = self.cleaned_data
        post = Comment(
            name=data['title'],
            email=data['email'],
            title=data['title'],
            message=data['message']
        )
        post.save()
