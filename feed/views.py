from django.contrib import messages
from django.http import request
from django.views.generic import TemplateView, DetailView, FormView

# Importando o model Post de models.py
from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = "home.html"

    # Passando uma variavel para view
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['my_thing'] = 'Olá Thiago, tudo bem com vc :P'
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id') # Post é o nome do model, order_by ordena por ordem decrescente
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    # Leva a mensagem para a pagina
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, "Novo Post!") # Cria a mensagem
        return super().form_valid(form)