# HolyGPT
This project is an AI 🚀🚀🚀 chat web application based on distilgpt2 model meant to finish text inputted by user in the style of Polish Bible. User can also fiddle with model settings like temperature or top_k values. It's style was strongly inspired by the one and only TempleOS created by R.I.P Terry A. Davis. In TempleOS you can generate pseudo random "word from God", this tries to resemble that but it's less random.
# Setup

## Prerequisites
- [Docker](https://www.docker.com/)

## Instalation and usage
```sh
docker run -dp 5000:5000 kkreczko/holygpt:v1
```
After dowload and start is finished use this link to access website: (http://localhost:5000/)

# Acknowledgments
[distilgpt2 model](https://huggingface.co/distilbert/distilgpt2) - great model that works well on my not so powerful machines 🤟

[Rzymskokatolicka Parafia pw. Świętego Wawrzyńca w Mąkowarsku](http://www.makowarsko-parafia.pl/downloads/PS.pdf) - thank you for providing me with Bible 🙏🙏🙏

[Flask](https://flask.palletsprojects.com/en/3.0.x/) - awesome python web framework 📯

[Docker](https://www.docker.com/) - cool tool, always nice to work with 🐳

[Google Colab](https://colab.research.google.com/) - great application that helped me fine tune my model and accelerated whole proccess 🔥
