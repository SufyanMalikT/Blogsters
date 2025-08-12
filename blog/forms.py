from django import forms
from .models import Comment, ProfilePic
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content':forms.Textarea(attrs={'class':'block py-2 px-2 text-lg md:text-xl bg-gray-300 shadow-lg dark:bg-gray-900'})
        }


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ['img']
        widgets = {
            'img':forms.ClearableFileInput(attrs={'class': 'hidden', 'id': 'profileInput'})
        }
