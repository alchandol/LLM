from openai import OpenAI

client = OpenAI(api_key='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')

def get_response(role, examples, prompt):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": f""" {role} """
    },
    {
      "role": "user",
      "content": f""" {examples[0]} """
    },
    {
      "role": "assistant",
      "content": f""" {examples[1]} """
    },
    {
      "role": "user",
      "content": f""" {examples[2]} """
    },
    {
      "role": "assistant",
      "content": f""" {examples[3]} """
    },
    {
      "role": "user",
      "content": f""" {examples[4]} """
    },
    {
      "role": "assistant",
      "content": f""" {examples[5]} """
    },
    {
      "role": "user",
      "content": f""" {examples[6]} """
    },
    {
      "role": "assistant",
      "content": f""" {examples[7]} """
    },
     {
      "role": "user",
      "content": f"""{prompt} """
    }
    ],
      temperature=.25,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
  return response.choices[0].message.content
 

# prompt
Role = """You are a feedback analyzing assistant.  For the feedback provided, you are to come up with two scores.  
A workplace appropriateness score called 'AS' that ranges from 1 to 10 on how appropriate the feedback is for professional setting.
A feedback score called 'FS' that ranges from 1 to 10 on overall score of the feedback itself.
Beside each scores, you are to provide a short rationale for your scoring.  
The feedback to analyze will be input in format like, 'Feedback: <text>'"""



# Add Few Shots Examples

Example1A = "Bob is a cool attorney to work with.  He is alright when assisting clients and pretty knowledgeable when it comes to his area of expertise."
Example1B = """AS: 10. This feedback is appropriate for a professional workplace setting. It does not contain any inappropriate language or derogatory remarks.

FS:  8. This feedback is generally positive, stating that Bob is cool to work with, assists clients adequately, and has good knowledge in his area of expertise. However, the tone is somewhat neutral and does not convey a high level of enthusiasm or excitement.
"""

Example2A = """Bob is an ass. I hate everything about him and I wish he would leave the firm."""
Example2B = """AS: 2. This feedback contains derogatory language and expresses a strong negative sentiment towards Bob. It is not appropriate for a professional workplace setting.

FS: 2. The feedback is highly negative, expressing hatred towards Bob and a desire for him to leave the firm. The tone is filled with frustration and dissatisfaction.
"""


Example3A = """Bob is freaking amazing.  He is a goddamn angel when it comes to saving my ass when shit hits the fan."""
Example3B = """AS: 4. This feedback contains inappropriate language and profanity, which is not suitable for a professional workplace setting.

FS: 9. The feedback is highly positive, praising Bob for his exceptional abilities in resolving difficult situations. The use of strong language and emphasis conveys a high level of enthusiasm and satisfaction.
"""


Example4A = """Bob is a colleague that I do not want to work with going forward.  While Bob is recognized as a high performing attorney within his practice area, the projects that I ran with him proved to be very difficult and emotional.   Though I appreciate his time, I would like to work with someone else.
"""
Example4B = """AS: 10. This feedback is appropriate for a professional workplace setting. It does not contain any inappropriate language or derogatory remarks.

FS:  7. The reviewer acknowledges Bob's high performance but expresses difficulty and emotional challenges while working with him. The overall tone is neutral and suggests a preference to work with someone else.
"""


Exmps = [Example1A,Example1B,Example2A,Example2B,Example3A,Example3B,Example4A,Example4B]


def main():

	feed = input("Enter feedback: ")

	while feed != 'done!':

		print(get_response(Role, Exmps, feed))

		feed = input("Enter feedback: ")

main()