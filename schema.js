// TODO: fix schema with definitions
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
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "path": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "workflow": {
                    "type": "string"
                },
                "assets": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "attribute": {
                                "type": "string"
                            },
                            "path": {
                                "type": "string"
                            }
                        }
                    }
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": ["id", "name", "path", "type"]
        },
        "default": []
    }
}

module.exports = schema