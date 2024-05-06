import os
from dotenv import load_dotenv
from openai import OpenAI


# .env 파일로부터 환경 변수를 불러온다.
load_dotenv()

# 환경 변수에서 API 키를 가져온다.
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트를 초기화한다.
client = OpenAI(api_key=api_key)

def gpt_call(prompt):
    """
    gpt-3.5-turbo 모델을 사용하여, prompt에 대한 응답을 생성하고 반환하는 함수입니다.
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "당신은 다양한 스포츠에 대해 누구보다 잘 이해하고 있으며, 전문적인 분석을 제공하는 스포츠 분석가입니다."
            },
            {
                "role": "user",
                "content": prompt
            },
        ]
    )

    gpt_response = completion.choices[0].message.content

    return gpt_response


while True:
    print("스포츠와 관련된 질문을 자유롭게 해주세요!")
    print("프로그램을 종료하려면 '종료'를 입력하세요.\n")

    user_prompt = input("질문: ")
    if user_prompt == "종료":
        print("프로그램을 종료합니다.")
        break

    gpt_response = gpt_call(user_prompt)

    print("User Prompt:", user_prompt)
    print("GPT Response:", gpt_response)
    print("\n")