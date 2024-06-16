from g4f.client import Client

client = Client()

response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": "как сделать чтобы ИИ выводил значения в виде списка на сайте "



                }]
            )

print(response.choices[0].message.content)