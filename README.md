
# Project Title

A brief description of what this project does and who it's for


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


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

  