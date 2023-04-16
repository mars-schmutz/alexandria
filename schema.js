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
        "render": {
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
                "settings": {
                    "type": "string"
                }
            }
        },
        "proc_mat": {
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
                "settings": {
                    "type": "string"
                }
            }
        },
        "compositor": {
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
                "settings": {
                    "type": "string"
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
                { "$ref": "#/definitions/render" },
                { "$ref": "#/definitions/proc_mat" },
                { "$ref": "#/definitions/compositor" }
            ]
        },
        "default": []
    }
}

module.exports = schema