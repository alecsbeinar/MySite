from ads.models import Ad
from ads.owner import *


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
