import openai

openai.api_key = "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"

def gera_texto(texto):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = texto,
        max_tokens = 150,
        n = 5,
        stop = None,
        temperature = 0.8,
)
    return response.choices[0].text.strip()

def main():
    print("\nBem-vindo ao GPT-4 Chatbotdo Projeto 3 do Curso Gratuito da Data Science Academy!")
    print("www.datascienceacademy.com.br")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")
    
    while True:
        user_message = input("\nVocê: ")
        if user_message.lower() == "sair":
            break
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"
        chatbot_response = gera_texto(gpt4_prompt)
        print(f"\nChatbot: {chatbot_response}")
if __name__ == "__main__":
    main()