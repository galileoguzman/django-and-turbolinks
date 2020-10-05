import random
import time
from django.views.generic.list import ListView
from .models import Article

class ArticlesView(ListView):
    model = Article
    paginate_by = 7
    context_object_name = 'articles'
    template_name = 'articles/index.html'
    ordering = ['-published_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        time.sleep(random.randint(0, 2))

        return context
