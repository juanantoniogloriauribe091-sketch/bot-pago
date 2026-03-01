import httpx

TOKEN = "8792399832:AAGP1_bL4X8KZtcPd7bTjeFkX3mUt06IcBc"
CHAT_ID = "8277553435"
MENSAJE = "Hola! 📅 Recordatorio: hoy es día 8, por favor realiza tu pago. ¡Gracias!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
httpx.post(url, data={"chat_id": CHAT_ID, "text": MENSAJE})
print("Mensaje enviado!")
