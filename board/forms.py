from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput({
        'class': 'compose-title',
        'placeholder': 'Your Title Here',
    }))
    content = forms.CharField(widget=forms.Textarea({
        'id': 'editor',
    }))
