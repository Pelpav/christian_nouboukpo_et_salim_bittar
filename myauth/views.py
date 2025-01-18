from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseForbidden
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import codecs
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    from django import forms
    from .models import Client

    class ClientCreationForm(forms.ModelForm):
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

        class Meta:
            model = Client
            fields = ('username', 'email', 'tel', 'adresse', 'numPieceID', 'typePieceID', 'photo')

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Les mots de passe ne correspondent pas")
            return password2

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

    form = ClientCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            user = form.save()
            login(request, user)
            return redirect('home')
        except IntegrityError:
            form.add_error('username', "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
            return redirect('login')
    return render(request, 'myauth/register.html', {'form': form})



def forgot_password(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            current_site = request.META["HTTP_HOST"]
            context = {"token": token, "uid": uid, "domaine": f"http://{current_site}"}
            html_text = render_to_string("myauth/forgot_password_email.html", context)
            msg = EmailMessage(
                "Récupération de compte | ISTA Eshop",
                html_text,
                "ISTA Eshop <hamidoukass@gmail.com>",
                [user.email],
            )
            msg.content_subtype = "html"
            msg.send()
            context['sent'] = True
        else:
            context['errors'] = True

    return render(request, "myauth/forgot_password.html", context)


def update_password(request, token, uid):
    try:
        user_id = urlsafe_base64_decode(uid)
        decode_uid = codecs.decode(user_id, "utf-8")
        user = User.objects.get(id=decode_uid)
    except:
        return HttpResponseForbidden(
            "Vous n'aviez pas la permission de modifier ce mot de pass. Utilisateur introuvable."
        )
    check_token = default_token_generator.check_token(user, token)
    if not check_token:
        return HttpResponseForbidden(
            "Vous n'aviez pas la permission de modifier ce mot de pass. Votre Token est invalid ou a espiré"
        )
    errors = False
    success = False
    message = ""
    if request.method == "POST":
        password = request.POST.get("password1")
        repassword = request.POST.get("password2")
        if repassword == password:
            try:
                validate_password(password, user)
                user.set_password(password)
                user.save()
                success = True
                message = "votre mot de passe a été modifié avec succès!"
            except ValidationError as e:
                errors = True
                message = str(e)
        else:
            errors = True
            message = "Les deux mot de pass ne correspondent pas"
    context = {"errors": errors, "success": success, "message": message}
    return render(request, "myauth/update_password.html", context)

