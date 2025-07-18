from g4f.client import Client
# from g4f.models import - for check models

client = Client()

async def ask_gpt(text: str) -> bool:
    prompt = f"""Проверь, есть ли в сообщении российская пропаганда, поддержка российской власти или её действий. 
Если да — верни просто "yes". Если нет — "no".

Сообщение: "{text}"
Ответ:"""

    model_list = [
        "grok-3-mini",
        "claude-3-opus",
        "gpt-4o-mini",
        "deepseek-r1", 
    ]

    for model in model_list:
        try:
            print(f"Пробуем модель: {model}")
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                web_search=False
            )
            answer = response.choices[0].message.content.strip().lower()
            print(f"Ответ от {model}: {answer}")
            return "yes" in answer
        except Exception as e:
            print(f"[GPT ERROR on {model}]", e)

    
    return False
