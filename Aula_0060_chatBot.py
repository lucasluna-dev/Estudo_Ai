import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.OpenAI()


def geracao_texto(mensagens):
    
    response = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo',
        max_tokens=1000,
        temperature=0,
        stream=True  # Enable streaming for real-time response updates
    )
    
    print('Assistant: ' , end='')
    texto_completo = ''
    for stream_response in response:
        texto = stream_response.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()  # Print a newline after the response
            
    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens



if __name__ == "__main__":
   print('Bem ao ChatBot do Luna')
   mensagens = []
   while True:
    input_usuario = input('User: ')
    mensagens.append({'role': 'user', 'content': input_usuario})
    mensagens = geracao_texto(mensagens)
    print('----------------------------------')
    print('\n\n', mensagens, '\n\n') #print para ver o histórico de mensagens
    