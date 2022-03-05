from django import forms
from .models import *
from .fields import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}), label='Your Name')
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label='My Name'
        self.fields['name'].initial='My Name'
        self.fields['phone'].initial='+8801'

    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w=value.split(' ')
        if len(num_of_w) > 3:
            self.add_error('name', 'Name can have maximum of 3 words')
        else:
            return value

        # widgets={
        #     'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Your Name'}),
        #     'phone': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Your phone'}),
        #     'content': forms.Textarea(attrs={'class':'form-control','placeholder': 'Say something', 'rows':5}),
        # }
        # labels={
        #     'name': 'Your Name',
        #     'phone': 'Your Phone Number',
        #     'content': 'Your Words',
        # }
        # help_texts={
        #     'name': 'Your Name',
        #     'phone': 'Your Phone Number',
        #     'content': 'Your Words',
        # }

class ContactFormTwo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id','created_at','slug', 'likes', 'views',]
        # widgets = {
        #     'class_in':forms.CheckboxSelectMultiple(attrs={
        #         'multiple':True,
        #     }),
        #     'subject':forms.CheckboxSelectMultiple(attrs={
        #         'multiple':True,
        #     })
        # }
    def __init__(self, *args, **kwargs):
        _district_set=kwargs.pop('district_set', None)
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['district'].widget=ListTextWidget(data_list=_district_set, name='district-set')

class MultiFieldsFilterForm(forms.ModelForm):
    Choice_Approach = (
        ('web_development', 'Web Development'),
        ('web_design', 'Web Design'),
        ('graphich_design', 'Graphich Design'),
        ('seo', 'Search Engine Optimization'),
        ('digital_merketing', 'Degital Merketing'),
        ('apps_development', 'App Development'),
        ('programing', 'Programing'),
        ('game_development', 'Game Development'),
        ('other', 'Other'),
    )
    Skill = (
        ('social_media_marketing', 'Social media marketing'),
        ('search_engine_optimization', 'Search Engine Optimization'),
        ('adobe_photoshop', 'Adobe Photoshop'),
        ('html', 'html'),
        ('css', 'css'),
        ('javascript', 'javascript'),
        ('wordpress', 'wordpress'),
        ('php', 'php'),
        ('python', 'python'),
        ('go', 'go'),
        ('java', 'java'),
        ('c++', 'c++'),
        ('other', 'Other'),
    )
    # Expertise = forms.ChoiceField(widget=forms.Select(choices=Choice_Approach))
    Expertise = forms.ChoiceField(choices = Choice_Approach)
    Skill = forms.ChoiceField(choices = Skill)
    class Meta:
        model = Post
        fields = ['Expertise','Skill']

class FileModelForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ['image']
