from django import forms


ROOM_CHOICES = (
    ('twn', 'ツイン'),
    ('dbl', 'ダブル'),
    ('sgl', 'シングル'),
    )
    

class SearchForm(forms.Form):
    checkin = forms.DateField(
        label="チェックイン",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'}),
        input_formats=["%Y-%m-%d"]
        )
    checkout = forms.DateField(
        label="チェックアウト",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
        )
    headcount = forms.IntegerField(
        max_value=2,
        min_value=1,
        label="人数",
        required=True
        )


class ReserveForm(forms.Form):
    '''checkin = forms.DateField(
        label="チェックイン",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), \
        input_formats=["%Y-%m-%d"]
        )
    checkout = forms.DateField(
        label="チェックアウト",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), \
        input_formats=["%Y-%m-%d"]
        )'''
    headcount = forms.IntegerField(
        max_value=2,
        min_value=1,
        label="人数",
        required=True
        )
    #room_type = forms.ChoiceField(label="部屋タイプ", choices=ROOM_CHOICES)
    name = forms.CharField(
        label="名前",
        max_length=40,
        required=True
    )
    email = forms.EmailField(
        label="メール",
        required=True
    )
    
