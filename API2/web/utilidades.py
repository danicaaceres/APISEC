import html
import bleach

def sanitize_input(user_input):
    escaped_input = html.escape(user_input)
    clean_input = bleach.clean(escaped_input)
    return clean_input

def calcular_iva (importe:int):
    return importe*0.21