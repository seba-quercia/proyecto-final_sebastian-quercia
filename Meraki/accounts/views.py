from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from .models import Message
from .forms import MessageForm, ProfileUpdateForm, UserUpdateForm, CustomUserCreationForm, CustomPasswordChangeForm

# Registro de usuario
       
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

# Configuración de la cuenta
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

#Vista de configuracion de la cuenta
class AccountSettingsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/account_settings.html'
    form_class = ProfileUpdateForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        profile_form = form_class(instance=self.request.user.profile)
        user_form = UserUpdateForm(instance=self.request.user)
        password_form = CustomPasswordChangeForm(user=self.request.user)
        return {
            'profile_form': profile_form,
            'user_form': user_form,
            'password_form': password_form,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_form())
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, request.user)
            return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(user_form=user_form, password_form=password_form, profile_form=profile_form))

    def get_success_url(self):
        return reverse_lazy('account_settings')

    
# Login de usuario
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('inicio')

# Logout de usuario
class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

# Vistas para los mensajes
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from .models import Message

class MessageView(LoginRequiredMixin, FormView):
    form_class = MessageForm
    template_name = 'accounts/messages.html'

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('messages')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Verificar si se está mostrando el detalle de un mensaje
        message_id = self.kwargs.get('message_id')
        if message_id:
            message = get_object_or_404(Message, id=message_id, recipient=self.request.user)
            context['message_detail'] = message
        else:
            context['received_messages'] = self.request.user.received_messages.all()
        return context

