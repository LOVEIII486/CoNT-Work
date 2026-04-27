# pip install requests
import requests
import json

# replace the APP_KEY
APP_KEY = "####"


def completions(prompt, temperature, max_token, n_response):
    url = 'https://api.openai.com/v1/completions'

    headers = {}
    headers['Content-Type'] = "application/json"
    headers['Authorization'] = APP_KEY
    data = {}
    data['model'] = "text-davinci-003"
    data['prompt'] = prompt
    data['temperature'] = temperature
    data['max_tokens'] = max_token
    data['n'] = n_response

    x = requests.post(url, json=data, headers=headers)
    return json.loads(x.text)


def edits(prompt, instruction, max_token, n_response):
    url = 'https://api.openai.com/v1/edits'

    headers = {}
    headers['Content-Type'] = "application/json"
    headers['Authorization'] = APP_KEY
    data = {}
    data['model'] = "text-davinci-edit-001"
    data['input'] = prompt
    data['instruction'] = instruction

    data['n'] = n_response

    x = requests.post(url, json=data, headers=headers)
    return json.loads(x.text)


def classify(prompt, classes):
    class_str = ",".join(classes)
    new_prompt = f'classify this sentence into {class_str} : "{prompt}"'
    result = completions(new_prompt, 0.8, 100, 1)
    return result


def rewrite(prompt):
    new_prompt = f'Can you rephrase this sentence : "{prompt}"'
    result = completions(new_prompt, 0.8, 100, 1)
    return result


def summarize(prompt):
    new_prompt = f'Can you summarize the following content: "{prompt}"'
    result = completions(new_prompt, 0.8, 100, 1)
    return result


# res = edits("Today is Friday",'classify this sentence into "question" or "answer"', 100, 2)

"""
Normal Task, Classification Task, Rephrase Task.
Input: 
	prompt: The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.
	temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
	n: How many completions to generate for each prompt.
	max_tokens: The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096)
Output:
	Json-format Result: the text is stored in result['choices']
	
"""
# res = completions('classify this sentence into age, weight , weather: "I am 500 pounds"', 0.8, 100, 1)


res = rewrite("today is monday, I am going to swim.")
print(res)
print(res['choices'][0]['text'])

'''
{
   "id":"cmpl-6pqxOty9w1nU8ovLQUqhfnBBQmStR",
   "object":"text_completion",
   "created":1677816314,
   "model":"text-davinci-003",
   "choices":[
      {
         "text":"\n\nOn this Monday, I plan to go swimming.",
         "index":0,
         "logprobs":"None",
         "finish_reason":"stop"
      }
   ],
   "usage":{
      "prompt_tokens":19,
      "completion_tokens":12,
      "total_tokens":31
   }
}
'''
res = classify("hello world", ['Program', "travel"])
print(res['choices'][0]['text'].strip())

res = summarize(r"""
Abstract—Text data augmentation is an effective strategy for overcoming the challenge of limited sample sizes in many natural language
processing (NLP) tasks. This challenge is especially prominent in the few-shot learning scenario, where the data in the target domain
is generally much scarcer and of lowered quality. A natural and widely-used strategy to mitigate such challenges is to perform data
augmentation on the training data to better capture the data invariance and increase the sample size. However, current text data
augmentation methods either can not ensure the correct labeling of the generated data (lacking faithfulness) or can not ensure sufficient
diversity in the generated data (lacking completeness), or both. Inspired by the recent success of large language models, especially
the development of ChatGPT, which demonstrated improved language comprehension abilities, in this work, we propose a text data
augmentation approach based on ChatGPT (named ChatAug). ChatGPT is trained on data with unparalleled linguistic richness and
employs a reinforcement training process with large-scale human feedback, which endows the model with affinity to the naturalness
of human language. Our text data augmentation approach ChatAug rephrases each sentence in the training samples into multiple
conceptually similar but semantically different samples. The augmented samples can then be used in downstream model training.
Experiment results on few-shot learning text classification tasks show the superior performance of the proposed ChatAug approach over
state-of-the-art text data augmentation methods in terms of testing accuracy and distribution of the augmented samples.
""")

print(res['choices'][0]['text'])
