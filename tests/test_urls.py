import pytest
from django import urls
from django.urls import reverse
from django.contrib.auth import get_user_model
from store import urls




"""@pytest.mark.parametrize('param', [

    ('index')


] )

def test_mi_url(client, param):
    url = reverse('param')
    response = client.get(url)
    assert response.status_code =='200'"""


"""@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('store:agregar'),
    ('store:modificar')
])
def test_render_views(client, param):
    if param == 'store:modificar':
        # Si es la vista 'modificar', proporcionar un valor para 'pk'
        temp_url = reverse(param, kwargs={'pk': 1})
    else:
        temp_url = reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200
"""