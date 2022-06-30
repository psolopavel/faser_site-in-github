from django import forms

from .models import Reviews, Purchase, Rating_star, Rating

class ReviewForm(forms.ModelForm):



    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        widgets = {
            'name': forms.TextInput(attrs={"class": 'name'}),
            'email': forms.EmailInput(attrs={"class": 'name'}),
            'text': forms.Textarea(attrs={"class": 'coments_print'})
        }


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ("room",)

class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=Rating_star.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)