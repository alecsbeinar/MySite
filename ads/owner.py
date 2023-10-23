from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
    pass


class OwnerDetailView(DetailView):
    pass


class OwnerCreateView(LoginRequiredMixin, CreateView):
    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
