from generic.views import *
from publish.models import ArtWork

class LandingPage(TemplateView):
    template_name = 'index.html'


class Home(LoginRequiredMixin, ListView):
    queryset = ArtWork.objects.filter(publish=True).order_by('-created')
    template_name = 'home.html'
