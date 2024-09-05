from transformers import AutoTokenizer, AutoModelForCausalLM

class LLM:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

llm = LLM()

def generate_text(prompt, max_length=100):
    return llm.generate_text(prompt, max_length)