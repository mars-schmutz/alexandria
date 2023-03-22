// TODO: fix schema with definitions
const schema = {
    "definitions": {
        "material": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "thumbnail": {
                    "type": "string"
                },
                "path": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "maps": {
                    "type": "object",
                    "properties": {
                        "diffuse": {
                            "type": "string"
                        },
                        "metallic": {
                            "type": "string"
                        },
                        "specular": {
                            "type": "string"
                        },
                        "roughness": {
                            "type": "string"
                        },
                        "normal": {
                            "type": "string"
                        },
                        "bump": {
                            "type": "string"
                        },
                        "displacement": {
                            "type": "string"
                        },
                    }
                }
            }
        },
        "required": ["name", "id"]
    },
    "library-location": {
        "type": "string",
        "default": ""
    },
    "library-shelves": {
        "type": "array",
        "items": {
            "anyOf": [
                { "$ref": "#/definitions/material" },
            ]
        },
        "default": []
    }
}

module.exports = schema