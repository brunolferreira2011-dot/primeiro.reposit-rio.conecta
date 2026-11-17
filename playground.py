import os
import requests

CHAVE = os.environ["AI_GATEWAY_API_KEY"]
URL = "https://ai-gateway.vercel.sh/v1/chat/completions"
MODELO = "google/gemini-3.5-flash-lite"

print("=== Meu playground de IA ===")
sistema = input("Instrução de sistema (quem a IA deve ser): ")
temperatura = float(input("Temperatura (de 0 a 1): ") or 0.7)

while True:
 pergunta = input("\nVocê (ou 'sair'): ")
 if pergunta.lower() == "sair":
 break
 resposta = requests.post(
 URL,
 headers={"Authorization": f"Bearer {CHAVE}"},
 json={
 "model": MODELO,
 "temperature": temperatura,
 "messages": [
 {"role": "system", "content": sistema},
 {"role": "user", "content": pergunta},
 ],
 },
 timeout=60,
 )
 resposta.raise_for_status()
 print("IA:", resposta.json()["choices"][0]["message"]["content"])
