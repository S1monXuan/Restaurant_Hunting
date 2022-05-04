from django import forms
from rateinfo.models import Holder, Restaurant, Customer, Type, Place, Comment, Section


class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = '__all__'

    def clean_holder_name(self):
        return self.cleaned_data['holder_name'].strip()

    def clean_holder_phone(self):
        return self.cleaned_data['holder_phone'].strip()


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def clean_restaurant_name(self):
        return self.cleaned_data['restaurant_name'].strip()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_customer_name(self):
        return self.cleaned_data['customer_name'].strip()

    def clean_customer_mail(self):
        return self.cleaned_data['customer_mail'].strip()


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    def clean_type_name(self):
        return self.cleaned_data['type_name'].strip()


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

    def clean_place_city(self):
        return self.cleaned_data['place_city'].strip()

    def clean_place_state(self):
        return self.cleaned_data['place_state'].strip()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_comment_text(self):
        return self.cleaned_data['comment_text'].strip()

    def clean_comment_level(self):
        return self.cleaned_data['comment_level']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
