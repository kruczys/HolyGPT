from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

model = GPT2LMHeadModel.from_pretrained("../bible_model")
tokenizer = GPT2Tokenizer.from_pretrained("../bible_model")

def generate_response(prompt, temp=0.5, top_k=30, top_p=0.99, repetition_penalty=1.3):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=200,
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
    user_input = data["message"]
    response = generate_response(user_input)
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)


