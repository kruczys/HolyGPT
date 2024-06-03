function sendMessage() {
    const inputBox = document.getElementById("user_input");
    const userText = inputBox.value;
    inputBox.value = "";

    const chatBox = document.getElementById("chat");
    chatBox.innerHTML += '<p>You: ' + userText + '</p>';

    const temperature = document.getElementById("temperature").value;
    const top_k = document.getElementById("top_k").value;
    const top_p = document.getElementById("top_p").value;
    const repetition_penalty = document.getElementById("repetition_penalty").value;

    fetch("/chat", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: userText,
            temperature: temperature,
            top_k: top_k,
            top_p: top_p,
            repetition_penalty: repetition_penalty
        })
    })
        .then(response => response.json())
        .then(text => {
            chatBox.innerHTML += '<p>Bot: ' + text.message + '</p>';
            console.log(text)
        });
}

function clearChat() {
    const chatBox = document.getElementById("chat");
    chatBox.innerHTML = ""
}


