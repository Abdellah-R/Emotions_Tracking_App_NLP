import pytest
from django.urls import reverse
from django.template.loader import render_to_string
from usersapp.forms import RegistrationForm
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_home(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    expected_template = 'usersapp/home.html'  # Chemin vers le template attendu
    rendered_template = response.content.decode('utf-8')  # Convertir la réponse en chaîne de caractères

    # Charger le template attendu
    expected_rendered_template = render_to_string(expected_template)

    assert rendered_template == expected_rendered_template


def test_register_get(client):
    url = reverse('register')
    response = client.get(url)

    assert response.status_code == 200

def test_register_form_type(client):
    url = reverse('register')
    response = client.get(url)

    assert response.status_code == 200
    assert isinstance(response.context['form'], RegistrationForm)

@pytest.mark.django_db
def test_register_post(client):
    url = reverse('register')
    data = {'username': 'testuser', 
            'last_name': 'Doe', 
            'first_name': 'John', 
            'email': 'testuser@example.com', 
            'password': 'testpassword', 
            'is_patient': True
            }
    response = client.post(url, data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_invalid_form(client):
    url = reverse('register')
    data = {'username': '', 
            'last_name': '', 
            'first_name': '', 
            'email': '',
            'password': '', 
            'is_patient': True
            }
    
    response = client.post(url, data)

    assert response.status_code == 200
    assert not response.wsgi_request.user.is_authenticated

    form = response.context['form']

    assert isinstance(form, RegistrationForm)








