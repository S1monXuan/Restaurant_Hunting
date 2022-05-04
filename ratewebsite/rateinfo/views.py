from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from rateinfo.forms import HolderForm, RestaurantForm, CustomerForm, TypeForm, PlaceForm, CommentForm, SectionForm
from rateinfo.models import (
    Restaurant,
    Holder,
    Type,
    Place,
    Customer,
    Comment,
    Section,
)
from rateinfo.utils import PageLinksMixin
from django.contrib.auth.forms import UserCreationForm, password_validation


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_urlpattern')
    else:
        form = UserCreationForm()
    return render(request, 'rateinfo/signup.html', {
        'form': form
    })


class RestaurantList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 4
    model = Restaurant
    permission_required = 'rateinfo.view_restaurant'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(restaurant_name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class RestaurantDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Restaurant
    permission_required = 'rateinfo.view_restaurant'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        restaurant = self.get_object()
        comment_list = restaurant.comments.all()
        context['comment_list'] = comment_list
        return context


class RestaurantCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RestaurantForm
    model = Restaurant
    permission_required = 'rateinfo.add_restaurant'


class RestaurantUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RestaurantForm
    model = Restaurant
    template_name = 'rateinfo/restaurant_form_update.html'
    permission_required = 'rateinfo.change_restaurant'


class RestaurantDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('rateinfo/restaurant_confirm_delete.html')
    permission_required = 'rateinfo.delete_restaurant'

    def get(self, request, pk):
        restaurant = get_object_or_404(
            Restaurant,
            pk=pk)
        comment = restaurant.comments.all()
        if comment.count() > 0:
            return render(
                request,
                'rateinfo/restaurant_refuse_delete.html',
                {'restaurant': restaurant,
                 'comment': comment,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/restaurant_confirm_delete.html',
                {'restaurant': restaurant}
            )


class HolderList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 15
    model = Holder
    permission_required = 'rateinfo.view_holder'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(holder_name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class HolderDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Holder
    permission_required = 'rateinfo.view_holder'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        holder = self.get_object()
        restaurant_list = holder.restaurants.all()
        context['restaurant_list'] = restaurant_list
        return context


class HolderCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = HolderForm
    model = Holder
    permission_required = 'rateinfo.add_holder'


class HolderUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = HolderForm
    model = Holder
    template_name = 'rateinfo/holder_form_update.html'
    permission_required = 'rateinfo.change_holder'


class HolderDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Holder
    success_url = reverse_lazy('rateinfo_holder_list_urlpattern')
    permission_required = 'rateinfo.delete_holder'

    def get(self, request, pk):
        holder = get_object_or_404(
            Holder,
            pk=pk)
        restaurant = holder.restaurants.all()
        if restaurant.count() > 0:
            return render(
                request,
                'rateinfo/holder_refuse_delete.html',
                {'holder': holder,
                 'restaurant': restaurant,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/holder_confirm_delete.html',
                {'holder': holder}
            )


class TypeList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 8
    model = Type
    permission_required = 'rateinfo.view_type'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(type_name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TypeForm
    model = Type
    permission_required = 'rateinfo.add_type'


class TypeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Type
    permission_required = 'rateinfo.view_type'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        type = self.get_object()
        restaurant_list = type.restaurants.all()
        context['restaurant_list'] = restaurant_list
        return context


class TypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TypeForm
    model = Type
    template_name = 'rateinfo/type_form_update.html'
    permission_required = 'rateinfo.change_type'


class TypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Type
    success_url = reverse_lazy('rateinfo_type_list_urlpattern')
    permission_required = 'rateinfo.delete_type'

    def get(self, request, pk):
        types = get_object_or_404(
            Type,
            pk=pk)
        restaurant = types.restaurants.all()
        if restaurant.count() > 0:
            return render(
                request,
                'rateinfo/type_refuse_delete.html',
                {'type': types,
                 'restaurant_list': restaurant,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/type_confirm_delete.html',
                {'type': types}
            )


class PlaceList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Place
    permission_required = 'rateinfo.view_place'

    def get_queryset(self):
        if self.request.GET.get('q'):
            street = self.request.GET.get('q')
            object_list = self.model.objects.filter(place_street__contains=street)
        elif self.request.GET.get('p'):
            place = self.request.GET.get('p')
            object_list = self.model.objects.filter(place_place__contains=place)
        else:
            object_list = self.model.objects.all()
        return object_list


class PlaceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PlaceForm
    model = Place
    permission_required = 'rateinfo.add_place'


class PlaceDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Place
    permission_required = 'rateinfo.view_place'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        place = self.get_object()
        restaurant_list = place.restaurants.all()
        context['restaurant_list'] = restaurant_list
        return context


class PlaceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PlaceForm
    model = Place
    template_name = 'rateinfo/place_form_update.html'
    permission_required = 'rateinfo.change_place'


class PlaceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Place
    success_url = reverse_lazy('rateinfo_place_list_urlpattern')
    permission_required = 'rateinfo.delete_place'

    def get(self, request, pk):
        place = get_object_or_404(
            Place,
            pk=pk)
        restaurant = place.restaurants.all()
        if restaurant.count() > 0:
            return render(
                request,
                'rateinfo/place_refuse_delete.html',
                {'place': place,
                 'restaurant': restaurant,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/place_confirm_delete.html',
                {'place': place}
            )


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Customer
    permission_required = 'rateinfo.view_customer'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(customer_name__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = 'rateinfo.view_customer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        customer = self.get_object()
        comment_list = customer.comments.all()
        context['comment_list'] = comment_list
        return context


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CustomerForm
    model = Customer
    permission_required = 'rateinfo.add_customer'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'rateinfo/customer_form_update.html'
    permission_required = 'rateinfo.change_customer'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('rateinfo_customer_list_urlpattern')
    permission_required = 'rateinfo.delete_customer'

    def get(self, request, pk):
        customer = get_object_or_404(
            Customer,
            pk=pk)
        comment = customer.comments.all()
        if comment.count() > 0:
            return render(
                request,
                'rateinfo/customer_refuse_delete.html',
                {'customer': customer,
                 'comment': comment,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/customer_confirm_delete.html',
                {'customer': customer}
            )


class CommentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Comment
    permission_required = 'rateinfo.view_comment'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(comment_text__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class CommentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Comment
    permission_required = 'rateinfo.view_comment'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        comment = self.get_object()
        return context


class CommentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    permission_required = 'rateinfo.add_comment'


class CommentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CommentForm
    model = Comment
    template_name = 'rateinfo/comment_form_update.html'
    permission_required = 'rateinfo.change_comment'


class CommentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('rateinfo_comment_list_urlpattern')
    permission_required = 'rateinfo.delete_comment'

    def get(self, request, pk):
        comment = get_object_or_404(
            Comment,
            pk=pk)
        return render(
            request,
            'rateinfo/comment_confirm_delete.html',
            {'comment': comment}
        )


class SectionList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Section
    permission_required = 'rateinfo.view_section'


class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Section
    permission_required = 'rateinfo.view_section'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        comment_list = section.comments.all()
        context['comment_list'] = comment_list
        return context


class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SectionForm
    model = Section
    permission_required = 'rateinfo.add_section'


class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'rateinfo/section_form_update.html'
    permission_required = 'rateinfo.change_section'


class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy('rateinfo_section_list_urlpattern')
    permission_required = 'rateinfo.delete_section'

    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk)
        comment = section.comments.all()
        if comment.count() > 0:
            return render(
                request,
                'rateinfo/section_refuse_delete.html',
                {'section': section,
                 'comment_list': comment,
                 }
            )
        else:
            return render(
                request,
                'rateinfo/section_confirm_delete.html',
                {'section': section}
            )
