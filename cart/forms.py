from django import forms


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quantity = kwargs.pop('quantity', 1)
        super().__init__(*args, **kwargs)
        self.fields['quantity'].choices = [(i, str(i)) for i in range(1, quantity + 1)]

    quantity = forms.TypedChoiceField(coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
