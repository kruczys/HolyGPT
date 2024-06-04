from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("./bible_model")
tokenizer = GPT2Tokenizer.from_pretrained("./bible_model")

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=200,
        num_return_sequences=1,
        temperature=0.5,
        top_k=30,
        top_p=0.99,
        repetition_penalty=1.3,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

print("Witaj! Wpisz tekst, aby otrzymać kontynuację w stylu Biblii. Wpisz 'exit', aby zakończyć.")

while True:
    user_input = input("Ty: ")
    if user_input.lower() == 'exit':
        print("Do widzenia!")
        break
    response = generate_response(user_input)
    print(f"Model: {response}")
