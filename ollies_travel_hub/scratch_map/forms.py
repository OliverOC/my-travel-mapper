from django import forms
from django.core import validators
from .models import Trip


class AddTrip(forms.ModelForm):
    # country = forms.CharField(label='Country')
    # year = forms.IntegerField(label='Year')
    # note = forms.CharField(widget=forms.Textarea, label='Note')
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Trip
        # exclude = [""]
        # fields = ("","")
        fields = "__all__"





# BELOW DOES NOT CONNECT TO MODEL AS IT IS FORMS.FORM NOT FORMS.MODELFORM

#
# def check_for_country(value):
#     # NEED TO UNPACK
#     countries_choice_list = [('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bangladesh', 'Bangladesh'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('East Timor', 'East Timor'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Southern and Antarctic Lands', 'French Southern and Antarctic Lands'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea Bissau', 'Guinea Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Ivory Coast', 'Ivory Coast'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Mauritania', 'Mauritania'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Korea', 'North Korea'), ('Northern Cyprus', 'Northern Cyprus'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Republic of Serbia', 'Republic of Serbia'), ('Republic of the Congo', 'Republic of the Congo'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Sierra Leone', 'Sierra Leone'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('Somaliland', 'Somaliland'), ('South Africa', 'South Africa'), ('South Korea', 'South Korea'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Thailand', 'Thailand'), ('The Bahamas', 'The Bahamas'), ('Togo', 'Togo'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United Republic of Tanzania', 'United Republic of Tanzania'), ('United States of America', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('West Bank', 'West Bank'), ('Western Sahara', 'Western Sahara'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')]
#     if value.lower() not in countries_choice_list:
#         raise forms.ValidationError("COUNTRY NOT RECOGNISED!")


# class AddTrip(forms.Form):
#     # country = forms.CharField(validators=[check_for_country], label='Country')
#     country = forms.CharField(label='Country')
#     year = forms.IntegerField(label='Year')
#     note = forms.CharField(widget=forms.Textarea, label='Note')
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("MAKE SURE EMAILS MATCH")
