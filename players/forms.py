from django import forms
from . import models


class AddPlayer(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['full_name',
                  'short_name',
                  'slug',
                  'list_pic',
                  'details_pic',
                  'birth_date',
                  'nationality',
                  'position',
                  'shirt_num',
                  'facebook_link',
                  'instagram_link',
                  'twitter_link',
                  'bio_headline',
                  'player_bio'
                  ]
        widgets = {
            'birth_date': forms.SelectDateWidget(attrs={'class': 'form-select'},
                                                 years=[year for year in range(1980, 2006)]),
            'position': forms.Select(attrs={'class': 'form-select'}),
            'shirt_num': forms.TextInput(attrs={'class': 'form-control'})
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['header', 'body']

        widgets = {
            'header': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '1000', 'rows': 6})
        }
