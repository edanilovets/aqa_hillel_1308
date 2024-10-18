response_schema = {
    "type": "object",
    "properties": {
        "count": {"type": "integer"},
        "next": {"type": ["string", "null"], "format": "uri"},
        "previous": {"type": ["string", "null"], "format": "uri"},
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "height": {"type": "string"},
                    "mass": {"type": "string"},
                    "hair_color": {"type": "string"},
                    "skin_color": {"type": "string"},
                    "eye_color": {"type": "string"},
                    "birth_year": {"type": "string"},
                    "gender": {"type": "string"},
                    "homeworld": {"type": "string", "format": "uri"},
                    "films": {"type": "array", "items": {"type": "string", "format": "uri"}},
                    "species": {"type": "array", "items": {"type": "string", "format": "uri"}},
                    "starships": {"type": "array", "items": {"type": "string", "format": "uri"}},
                    "vehicles": {"type": "array", "items": {"type": "string", "format": "uri"}},
                    "url": {"type": "string", "format": "uri"},
                    "created": {"type": "string", "format": "date-time"},
                    "edited": {"type": "string", "format": "date-time"},
                },
                "required": [
                    "name", "height", "mass", "hair_color", "skin_color",
                    "eye_color", "birth_year", "gender", "homeworld",
                    "films", "species", "starships", "vehicles", "url",
                    "created", "edited"
                ],
            },
        },
    },
    "required": ["count", "next", "previous", "results"],
}
