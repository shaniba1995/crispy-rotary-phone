from django import forms


class NotificationForm(forms.Form):
    email = forms.EmailField()