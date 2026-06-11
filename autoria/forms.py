from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'year',
            'price_usd',
            'mileage',
            'transmission',
            'engine',
            'body_type',
            'drive',
            'color',
            'city',
            'region',
            'plate',
            'vin',
            'generation',
            'modification',
            'description',
            'seller_name',
            'seller_phone',
            'image',
        ]
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'Наприклад, Toyota',
            }),
            'model': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'Наприклад, Camry',
            }),
            'year': forms.NumberInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '2020',
                'min': 1980,
                'max': 2026,
            }),
            'price_usd': forms.NumberInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '15000',
                'min': 100,
            }),
            'mileage': forms.NumberInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '100',
                'min': 0,
            }),
            'transmission': forms.Select(attrs={'class': 'sell-field__select'}),
            'engine': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '2.0 Бензин',
            }),
            'body_type': forms.Select(attrs={'class': 'sell-field__select'}),
            'drive': forms.Select(attrs={'class': 'sell-field__select'}),
            'color': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'Білий',
            }),
            'city': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'Київ',
            }),
            'region': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'Київська обл.',
            }),
            'plate': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'АА 1234 ВВ',
            }),
            'vin': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'JTNBF1FK5MJ012345',
                'maxlength': 17,
            }),
            'generation': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'XV70, 8 покоління',
            }),
            'modification': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '2.5 AT (209 к.с.)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'sell-field__textarea',
                'placeholder': 'Опишіть стан авто, комплектацію, історію обслуговування...',
                'rows': 5,
            }),
            'seller_name': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': "Ваше ім'я",
            }),
            'seller_phone': forms.TextInput(attrs={
                'class': 'sell-field__input',
                'placeholder': '(067) 123 45 67',
            }),
            'image': forms.URLInput(attrs={
                'class': 'sell-field__input',
                'placeholder': 'https://... (посилання на фото авто)',
            }),
        }
        labels = {
            'brand': 'Марка',
            'model': 'Модель',
            'year': 'Рік випуску',
            'price_usd': 'Ціна, $',
            'mileage': 'Пробіг, тис. км',
            'transmission': 'Коробка передач',
            'engine': 'Двигун',
            'body_type': 'Тип кузова',
            'drive': 'Привід',
            'color': 'Колір',
            'city': 'Місто',
            'region': 'Область',
            'plate': 'Номерний знак',
            'vin': 'VIN-код',
            'generation': 'Покоління',
            'modification': 'Модифікація',
            'description': 'Опис',
            'seller_name': "Ім'я продавця",
            'seller_phone': 'Телефон',
            'image': 'Посилання на фото',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        optional_fields = [
            'body_type', 'drive', 'color', 'region', 'vin',
            'generation', 'modification', 'description',
            'seller_name', 'seller_phone', 'image',
        ]
        for field_name in optional_fields:
            self.fields[field_name].required = False

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 1980 or year > 2026:
            raise forms.ValidationError('Вкажіть коректний рік випуску.')
        return year
