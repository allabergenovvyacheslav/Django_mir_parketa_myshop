from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 201)]

class CartAddProductForm(forms.Form):
    """
    форма, позволяющая пользователю выбирать количество
    quantity: позволяет пользователю выбирать количество от 1 до 200. Для конвертирования входных данных в целое
    число используется поле TypedChoiceField вместе с coerce=int;
    override: позволяет указывать, должно ли количество быть прибавлено к любому существующему количеству в корзине
    для этого товара (False) или же существующее количество должно быть переопределено данным количеством (True).
    Для этого поля используется виджет HiddenInput, так как это поле не будет показываться пользователю.
    """
    quantity= forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
