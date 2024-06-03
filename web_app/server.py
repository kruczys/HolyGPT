from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

model = GPT2LMHeadModel.from_pretrained("../bible_model")
tokenizer = GPT2Tokenizer.from_pretrained("../bible_model")

def generate_response(prompt, max_tokens=100, temp=0.5, top_k=30, top_p=0.99, repetition_penalty=1.3):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_tokens,
        num_return_sequences=1,
        temperature=temp,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def response():
    data = request.get_json()
    user_input = data['message']
    temp = float(data.get('temperature', 0.5))
    top_k = int(data.get('top_k', 30))
    top_p = float(data.get('top_p', 0.99))
    repetition_penalty = float(data.get('repetition_penalty', 1.3))
    max_tokens = int(data.get('max_tokens', 100))
    response_text = generate_response(user_input, max_tokens, temp, top_k, top_p, repetition_penalty)
    print(max_tokens, temp, top_k, top_p, repetition_penalty)
    return jsonify({"message": response_text})

if __name__ == "__main__":
    app.run(port=5000, debug=True)


