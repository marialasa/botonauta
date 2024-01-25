import openai
import tweepy
import datetime

# Cargar las key y tokens de OpenAI & TwitterX

openai.api_key = ''
twitterx_consumer_key = ''
twitterx_consumer_secret = ''
twitterx_access_token = ''
twitterx_access_token_secret = ''

# Autenticación de la API de TwitterX

client = tweepy.Client(
    consumer_key = twitterx_consumer_key,
    consumer_secret = twitterx_consumer_secret,
    access_token = twitterx_access_token,
    access_token_secret = twitterx_access_token_secret
)

# Verificación de las credenciales de TwitterX

try:
  client.verify_credentials()
  print("Verificación correcta")
except:
  print("Error en la verificación")

# Función para generar contenido usando ChatGPT

def prompt(message):
    try:
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            temperature = 0,
            messages = [
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0]["message"]["content"]
    except Exception as e:
        print(f"Error en generación de respuesta: {e}")
        return None

# Función para postear en TwitterX

def tweet(mensaje):
    try:
        client.create_tweet(text = mensaje)
        print("Tweet publicado")
    except Exception as e:
        print(f"Error en publicación de tweet: {e}")

# Obtener ubicación y fecha actual

fecha_actual = datetime.datetime.now()
dia = fecha_actual.strftime("%d")
mes = fecha_actual.strftime("%m")
mes_letras = fecha_actual.strftime("%B")

# Generar el prompt y publicar la respuesta en TwitterX

mensaje = (
    f"Buscá un hecho político significativo que haya ocurrido un {dia}
    de {mes}, pero en un año en el pasado. Asegurate de que el hecho esté
    documentado y las fechas sean correctas. Empezá tu respuesta con:
    'Un {dia} de {mes_letras}, pero de...' y limitá tu respuesta a menos
    de 220 caracteres."
)

contenido = prompt(mensaje)
if contenido:
    tweet(contenido)