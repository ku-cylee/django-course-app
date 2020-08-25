from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(
        max_length=20, 
        widget=forms.PasswordInput()
    )


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput({
        'class': 'compose-title',
        'placeholder': 'Your Title Here',
    }))
    content = forms.CharField(widget=forms.Textarea({
        'id': 'editor',
    }))
