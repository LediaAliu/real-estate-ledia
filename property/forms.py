from django import forms
from .models import Category


class SearchForm(forms.Form):
    location = forms.CharField(
        max_length=20,
        min_length=3,
        required=False,
        label="Location",
        widget=forms.TextInput(attrs={"placeholder": "Type your location", "type": "text"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(),
        required=False,
        empty_label="Category",
    )
    look_for = forms.ChoiceField(
        choices=[
            (None, "Look for"),
            ("FS", "For Sale"),
            ("FR", "For Rent"),
        ],
        required=False,
    )

    sort_by = forms.ChoiceField(
        choices=[("pub_date", "Date"), ("title", "Name"), ("price", "Price")],
        required=False,
        widget=forms.Select(),
    )
    paginate_by = forms.ChoiceField(
        choices=[("6", "6"), ("12", "12"), ("18", "18"), ("24", "24")],
        required=False,
        widget=forms.Select(),
    )
