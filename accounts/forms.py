from django import forms



class ConnexionForm(forms.Form):
	username = forms.CharField(max_length=250,
	    						widget =forms.TextInput(attrs={"class": "form-control input-sm", "placeholder":"Username"}),
		                       )
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control input-sm", "placeholder":"Password"}))

	def __init__(self, request, *args, **kwargs):
		self.request = request
		super(ConnexionForm, self).__init__(*args, **kwargs)