from faker import Faker

faker = Faker()

pet_data_list = [
    {
        "id": 101,
        "name": "Fluffy",
        "category": {"id": 1, "name": "Cats"},
        "photoUrls": ["https://example.com/cat1.jpg"],
        "tags": [{"id": 1, "name": "cute"}],
        "status": "available"
    },
    # {
    #     "id": 102,
    #     "name": "Barky",
    #     "category": {"id": 2, "name": "Dogs"},
    #     "photoUrls": ["https://example.com/dog1.jpg"],
    #     "tags": [{"id": 2, "name": "friendly"}],
    #     "status": "available"
    # },
    # {
    #     "id": 103,
    #     "name": "Goldy",
    #     "category": {"id": 3, "name": "Fish"},
    #     "photoUrls": ["https://example.com/fish1.jpg"],
    #     "tags": [{"id": 3, "name": "silent"}],
    #     "status": "sold"
    # },
]
