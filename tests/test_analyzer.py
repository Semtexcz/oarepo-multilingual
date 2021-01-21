from flask import Flask

from oarepo_multilingual.mapping.multilingual_analysis import multilingual_analysis


def test_analyzer():
    """Test of multilingual analyzer"""
    app2 = Flask('testapp')
    app2.config = {"ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }}}}

    assert multilingual_analysis(app=app2) == {}


    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["cs","_"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }}}}


    assert multilingual_analysis(app=app2) == {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }
    }

    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["_"],"ELASTICSEARCH_LANGUAGE_ANALYSIS": {"_": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }}}}

    assert multilingual_analysis(app=app2) == {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }
    }

    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["cs", "en"],"ELASTICSEARCH_LANGUAGE_ANALYSIS": {'cs': {'czech': {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
        }
    }

    assert multilingual_analysis(app=app2) == {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }


    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
        }}

    assert multilingual_analysis(app=app2) == {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }


    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs": {"czech": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard",
        "filter": [
            "lowercase",
            "stop",
            "snowball"
        ]
    }},
        "en": {"english": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
    }
                   }

    assert multilingual_analysis(app=app2) == {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        },
            "english": {
                "type": "custom",
                "char_filter": [
                    "html_strip"
                ],
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "snowball"
                ]
            }
        }

    app2.config = {"MULTILINGUAL_SUPPORTED_LANGUAGES": ["cs", "en"], "ELASTICSEARCH_LANGUAGE_ANALYSIS": {"cs#title": {"czech#title": {
        "type": "custom",
        "char_filter": [
            "html_strip"
        ],
        "tokenizer": "standard"
    }},
        "cs": {"czech": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard",
            "filter": [
                "lowercase",
                "stop",
                "snowball"
            ]
        }}
    }
                   }

    assert multilingual_analysis(app=app2, id='title') == {"czech#title": {
            "type": "custom",
            "char_filter": [
                "html_strip"
            ],
            "tokenizer": "standard"
        }
        }

