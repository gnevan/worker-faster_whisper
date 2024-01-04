INPUT_VALIDATIONS = {
    'audio': {
        'type': str,
        'required': False,
        'default': None
    },
    'audio_base64': {
        'type': str,
        'required': False,
        'default': None
    },
    'model': {
        'type': str,
        'required': False,
        'default': 'base'
    },
    'transcription': {
        'type': str,
        'required': False,
        'default': 'plain_text'
    },
    'translate': {
        'type': bool,
        'required': False,
        'default': False
    },
    'language': {
        'type': str,
        'required': False,
        'default': None
    },
    'temperature': {
        'type': float,
        'required': False,
        'default': 0
    },
    'best_of': {
        'type': int,
        'required': False,
        'default': 5
    },
    'beam_size': {
        'type': int,
        'required': False,
        'default': 5
    },
    'patience': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'length_penalty': {
        'type': float,
        'required': False,
        'default': 0
    },
    'suppress_tokens': {
        'type': str,
        'required': False,
        'default': '-1'
    },
    'initial_prompt': {
        'type': str,
        'required': False,
        'default': None
    },
    'condition_on_previous_text': {
        'type': bool,
        'required': False,
        'default': True
    },
    'temperature_increment_on_fallback': {
        'type': float,
        'required': False,
        'default': 0.2
    },
    'compression_ratio_threshold': {
        'type': float,
        'required': False,
        'default': 2.4
    },
    'logprob_threshold': {
        'type': float,
        'required': False,
        'default': -1.0
    },
    'no_speech_threshold': {
        'type': float,
        'required': False,
        'default': 0.6
    },
    'enable_vad': {
        'type': bool,
        'required': False,
        'default': False
    },
    'word_timestamps': {
        'type': bool,
        'required': False,
        'default': False
    },
    'repetition_penalty': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'no_repeat_ngram_size': {
        'type': int,
        'required': False,
        'default': 0
    },
    'prompt_reset_on_temperature': {
        'type': float,
        'required': False,
        'default': 0.5
    },
    'suppress_blank': {
        'type': bool,
        'required': False,
        'default': True
    },
    'without_timestamps': {
        'type': bool,
        'required': False,
        'default': False
    },
    'max_initial_timestamp': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'prepend_punctuations': {
        'type': str,
        'required': False,
        'default': "\"'“¿([{-"
    },
    'append_punctuations': {
        'type': str,
        'required': False,
        'default': "\"'.。,，!！?？:：”)]}、"
    },
    'prefix': {
        'type': str,
        'required': False,
        'default': None
    }
}
