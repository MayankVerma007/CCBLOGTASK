from .models import CommentModel
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'email', 'comment')
'''class CommentForm(forms.Form):
    your_name =forms.CharField(max_length=100)
    comment_text =forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"'''