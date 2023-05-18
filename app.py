# The user details get print in the console.
# so you can do whatever you want to do instead
# of printing it
 
from flask import Flask, render_template, url_for, redirect, request, session
from authlib.integrations.flask_client import OAuth
import os
import secrets
import json
import requests

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!/xd5\xa2\xa0\x9fR"\xa1\xa8' 
'''
    Set SERVER_NAME to localhost as twitter callback
    url does not accept 127.0.0.1
    Tip : set callback origin(site) for facebook and twitter
    as http://domain.com (or use your domain name) as this provider
    don't accept 127.0.0.1 / localhost
'''
 
app.config['SERVER_NAME'] = 'localhost:5000'
oauth = OAuth(app)
 
@app.route('/index')
def index():
    return render_template('index.html')
 
@app.route('/google/')
def google():
   
    nonce = secrets.token_hex(16)

    # Google Oauth Config
    # Obtenha client_id e client_secret de variáveis ambientais
    # Para fins de desenvolvimento você pode colocá-lo diretamente
    # aqui dentro de aspas duplas

        #usuario2
    GOOGLE_CLIENT_ID = '523218512159-ib3d5aunbfv2lqtkfadumoi581m3irng.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
     
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
     
    # Redirecionar para google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)
 
@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    nonce = request.args.get('nonce')  # Extrair o valor do 'nonce' dos parâmetros da solicitação
    user = oauth.google.parse_id_token(token, nonce=nonce)
    print(" Google User ", user)
    user_json = json.dumps(user)
    data=user_json
    return redirect(url_for('perfil', data=data))
 

@app.route('/perfil')
def perfil():
    user_json = request.args.get('data')
    user = json.loads(user_json)
    return render_template('perfil.html', user=user)

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    # Fazendo a solicitação para obter o Access Token
    token_url = 'https://stoplight.io/mocks/highlevel/integrations/39582851/oauth/token'
    client_id = '6456685fd7d32e31b02a712d-lhslbgsb'
    client_secret = '78d26cf1-a6b1-403e-9520-fea17da72c99'

    # https://app.myclients.agency/v2/location/tqQPGR1TwyW47m4078uu

    token_payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': 'djhbjhb',
        'user_type': 'Location',
        'redirect_uri': 'https://myapp.com/oauth/callback/gohighlevel'
    }

    token_response = requests.post(token_url, data=token_payload)

    if token_response.status_code == 200:
        access_token = token_response.json().get('access_token')

        # Armazenar o access token na sessão
        session['access_token'] = access_token

        # Fazendo a solicitação GET para obter os dados do negócio
        business_url = 'https://stoplight.io/mocks/highlevel/integrations/111540399/businesses/5DP4iH6HLkQsiKESj6rh'
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token,
            'Version': '2021-04-15'
        }

        business_response = requests.get(business_url, headers=headers)

        if business_response.status_code == 200:
            business_data = business_response.json()
            print(business_data)
            return render_template('dashboard.html', business=business_data, token=access_token, name=access_token)
        else:
            return 'Erro ao obter os dados do negócio. Código de status: ' + str(business_response.status_code)
    else:
        return 'Erro ao obter o Access Token. Código de status: ' + str(token_response.status_code)




@app.route('/contatos', methods=['GET'])
def contatos():
    # Verificar se o token de acesso está presente na sessão
    if 'access_token' in session:
        access_token = session['access_token']
    else:
        # Caso não haja um token de acesso na sessão, faça a solicitação para obter um novo token
        token_url = 'https://stoplight.io/mocks/highlevel/integrations/39582851/oauth/token'
        client_id = '6456685fd7d32e31b02a712d-lhslbgsb'
        client_secret = '78d26cf1-a6b1-403e-9520-fea17da72c99'

        token_payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': 'djhbjhb',
            'user_type': 'Location',
            'redirect_uri': 'https://myapp.com/oauth/callback/gohighlevel'
        }

        token_response = requests.post(token_url, data=token_payload)

        if token_response.status_code == 200:
            access_token = token_response.json().get('access_token')
            # Armazenar o access token na sessão
            session['access_token'] = access_token
        else:
            return 'Erro ao obter o Access Token. Código de status: ' + str(token_response.status_code)

    # Fazendo a solicitação GET para obter os dados do negócio
    contact_url = 'https://stoplight.io/mocks/highlevel/integrations/39582863/contacts/ocQHyuzHvysMo5N5VsXc'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token,
        'Version': '2021-07-28'
    }

    contact_response = requests.get(contact_url, headers=headers)

    if contact_response.status_code == 200:
        contact_data = contact_response.json()
        print(contact_data)
        return render_template('contatos.html', contact=contact_data, token=access_token, name=access_token)
    else:
        return 'Erro ao obter os dados do negócio. Código de status: ' + str(contact_response.status_code)
    

if __name__ == "__main__":
    app.run(debug=True)

    