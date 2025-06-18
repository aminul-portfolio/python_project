from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control shadow-sm border border-primary rounded-3',
                'placeholder': '📬 Help Us Improve 💬 🗣️ Your Feedback Matters',
                'rows': 3,
                'id': 'commentBox'
            })
        }