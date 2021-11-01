from generic.views import *
from .models import *
from .forms import *


class ArtworkUpload(LoginRequiredMixin, CreateView):
    model = ArtWork
    success_url = reverse_lazy('')
    template_name = ''


class ArtworkDetails(DetailView):
    model = ArtWork
    template_name = 'artwork-details.html'


class UserArtworkList(UserChildView):
    child_model = ArtWork
    template_name = 'user-artwork-list.html'



class ArtworkManagement(UserFormsetView):
    model = User
    formSet = inlineformset_factory(User, ArtWork, form=ArtworkForm)
    meta = {'subject': 'Artwork Management'}
