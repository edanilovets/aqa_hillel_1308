from faker import Faker

faker = Faker()

pet_data_list = [
    {
        "id": 101,
        "category": {
            "id": 1,
            "name": "cats"
        },
        "name": faker.name(),
        "photoUrls": [
            "https://cat1.example"
        ],
        "tags": [
            {
                "id": 1,
                "name": "kitty"
            }
        ],
        "status": "available"
    },
    {
      "id": 102,
      "category": {
        "id": 2,
        "name": "dogs"
      },
      "name": faker.name(),
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 2,
          "name": "dogs"
        }
      ],
      "status": "pending"
    },
    {
      "id": 103,
      "category": {
        "id": 2,
        "name": "dogs"
      },
      "name": faker.name(),
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 1,
          "name": "silent"
        }
      ],
      "status": "available"
    }
]