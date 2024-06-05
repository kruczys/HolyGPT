# HolyGPT

HolyGPT is an AI 🚀🚀🚀 chat web application based on the distilgpt2 model, designed to finish text inputted by the user in the style of the Polish Bible. Users can also adjust model settings such as temperature or top_k values. The style of this project was heavily inspired by the unique TempleOS created by the late Terry A. Davis. In TempleOS, users could generate pseudo-random "word from God" messages; HolyGPT aims to emulate this, but with less randomness and more focus on the Biblical style.

## Setup

### Prerequisites
- [Docker](https://www.docker.com/)

### Installation and Usage
Note: This is an 8GB download.

1. Pull and run the Docker image:

    ```sh
    docker run -dp 5000:5000 kkreczko/holygpt:v1
    ```

2. Once the download and startup are complete, access the web application via this link: [http://localhost:5000/](http://localhost:5000/)

## Acknowledgments

- [distilgpt2 model](https://huggingface.co/distilbert/distilgpt2) - A great model that works well even on less powerful machines. 🤟
- [Rzymskokatolicka Parafia pw. Świętego Wawrzyńca w Mąkowarsku](http://www.makowarsko-parafia.pl/downloads/PS.pdf) - Thank you for providing the Bible. 🙏🙏🙏
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - An awesome Python web framework. 📯
- [Docker](https://www.docker.com/) - A cool tool that's always nice to work with. 🐳
- [Google Colab](https://colab.research.google.com/) - An excellent application that helped me fine-tune my model and accelerate the whole process. 🔥

Feel free to explore, tweak the settings, and experience the unique blend of technology and scripture with HolyGPT. Enjoy! If you have any questions and suggestions feel free to contact me: konradkreczko@gmail.com
