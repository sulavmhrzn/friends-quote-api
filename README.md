
# Friends Quote API

Get quotes from the famous tv series Friends.


## API Reference

#### Get all quotes

```http
  GET /quotes
```

#### Get a random quotes

```http
  GET /quotes/random
```

#### Get quote

```http
  GET /quotes/character?name=${character_name}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `character_name`      | `string` | **Required**. character name to fetch |


## Run Locally

Clone the project

```bash
  git clone https://github.com/sulavmhrzn/friends-quote-api.git
```

Go to the project directory

```bash
  cd friends-quotes-api
```

Install dependencies

```bash
  pip install requirements.txt
```

Start the server

```bash
  python3 main.py
```

  
