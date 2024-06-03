function sendMessage(){
    const inputBox = document.getElementById("user_input");
    const userText = inputBox.value;
    inputBox.value = "";

    const chatBox = document.getElementById("chat");
    chatBox.innerHTML += '<p>You: ' + userText + '</p>';

    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({message: userText}),
        headers: {
            'content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(text => {
            chatBox.innerHTML += '<p>Bot: ' + text.message + '</p>';
            console.log(text)
    });
}

function clearChat(){
    const chatBox = document.getElementById("chat");
    chatBox.innerHTML = ""
}

