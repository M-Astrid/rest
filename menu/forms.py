from django import forms

class SortingForm(forms.Form):
    for_vegan = forms.BooleanField(required=False)
    sort_field = forms.ChoiceField(choices=(( '-rating', 'Popular'),
                                   ('-id', 'New'),
                                   ('price', 'Price (lowest)'),
                                   ('-price', 'Price (highest)')),
                                   required=False)

QUANTITY_CHOICES = [(i for i in range(1, 20))]
class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)