# FAKE NEWS DETECTOR API

This project is a Flask API for a model to detect if a news is fake or real

## Run with virtualenv

### Create virtualenv

```bash
virtualenv .env
source .env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run API

```bash
python api.py 6000
```

## Run with docker-compose

```bash
docker-compose up -d
```

By default the API maps port 6000

## Example Request

```json
[
  {
    "title": "German chancellor warns 'to be prepared for a long war'",
    "text": "German Chancellor Olaf Scholz said Friday that it is 'wise to be prepared for a long war' in Ukraine, adding that Kyiv's allies will remain together for the duration.'I think it is wise to be prepared for a long war and it is wise to give Putin the message that we are ready to just stay all the time together with Ukraine, and that we will constantly support the country,' Scholz told CNN’s Christiane Amanpour at Germany’s annual Munich Security Conference.'The really important decision we should take all together is saying that we are willing to do it as long as necessary, and that we will do our best,' the chancellor said.Scholz, while avoiding committing to an end target date for the war, said the unity among Ukrainian allies has surprised Putin.'I'm absolutely sure that Putin never expected that there would be that united Europe, and that there would be that united world. He never thought that the transatlantic partnership would work that good,' he said.Scholz singled out the United States for their continuous and vital support.'We just do it together with our friends and partners, and especially with the United States,' Scholz said, adding that he really appreciates his government's 'strong alliance' with the US.On arming Ukraine: Amanpour asked Scholz about the deployment of more German-made Leopard 2 tanks on the ground in Ukraine.Scholz said more would be deployed 'very soon,' together with trained soldiers, but he warned that many of Ukraine’s partners aren’t able to deliver the most modern models of the fighting vehicles.'I learned many are not able to deliver the most modern things...but in the ones they are delivering we will give the support as well,' Scholz said. 'And as you know, there is also a big number of older tanks which we will deliver.'Confronted on concerns over dwindling ammunition stockpiles, Scholz stressed the need for a 'permanent production of the most important weapons,' including ammunition.German Defense Minister Boris Pistorius was also present at Friday's meetings, saying the Munich conference is 'more important than ever,' given the Russian invasion.'From the beginning, the security conference has always been a place of understanding and dialogue. What is new is that this is now taking place at the same time as a war of aggression is being waged on European soil by Russia against Ukraine,' Pistorius said. 'That raises the stakes for the conference even higher.'"
  }
]
```

The body needs to have this format
