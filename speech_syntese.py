import torch
import re
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained('tinkoff-ai/ruDialoGPT-medium')
model = AutoModelWithLMHead.from_pretrained('tinkoff-ai/ruDialoGPT-medium')

def generate_answer(input_question):
    prepared_input = "@@ПЕРВЫЙ@@ " + input_question + " @@ВТОРОЙ@@ " 
    inputs = tokenizer(prepared_input, return_tensors='pt')
    generated_token_ids = model.generate(
        **inputs,
        top_k=10,
        top_p=0.95,
        num_beams=3,
        num_return_sequences=3,
        do_sample=True,
        no_repeat_ngram_size=2,
        temperature=1.2,
        repetition_penalty=1.2,
        length_penalty=1.0,
        eos_token_id=50257,
        max_new_tokens=40
    )
    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    answer = re.sub('@@ПЕРВЫЙ@@.*?@@ВТОРОЙ@@','',context_with_response[0], flags=re.DOTALL)
    return answer.replace("@@ПЕРВЫЙ@@", '').replace("@@ВТОРОЙ@@", '')
    