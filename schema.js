const schema = {
    "library-location": {
        "type": "string",
        "default": ""
    },
    "library-shelves": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "asset-type": {
                    "type": "string"
                },
                "assets": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": ["name", "asset-type"]
        },
        "default": []
    }
}

module.exports = schema