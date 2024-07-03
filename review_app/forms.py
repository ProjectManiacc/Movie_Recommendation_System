from django import forms
from .models import Reviews, Moviecomments


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'review_text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Moviecomments
        fields = ['comment_text']
