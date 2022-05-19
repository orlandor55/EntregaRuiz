from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
    CreateView, 
    UpdateView, 
    DeleteView
)

#models
from .models import PageModel
#forms
from .forms import PageForm


from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import  reverse_lazy
from django.shortcuts import redirect



class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class PageListView(ListView):
    model = PageModel
    template_name = "pages/pages.html"
    context_object_name = 'paginas'

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        return context

class PageDetailView(DetailView):
    model = PageModel
    template_name = "pages/page_detail.html"
   

@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = PageModel
    form_class = PageForm
    template_name = "pages/page_create.html"
    success_url = reverse_lazy('pages_app:page-list')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = PageModel
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages_app:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = PageModel
    success_url = reverse_lazy('pages_app:page-list')