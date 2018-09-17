from django import forms

class SortingForm(forms.Form):
    for_vegan = forms.BooleanField(required=False)
    sort_field = forms.ChoiceField(choices=(( '-ratind', 'Popular'),
                                   ('-id', 'New'),
                                   ('price', 'Price (lowest)'),
                                   ('-price', 'Price (highest)')),
                                   required=False)