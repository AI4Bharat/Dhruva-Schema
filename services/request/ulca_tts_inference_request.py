from typing import List, Optional

from ..common import (
    AudioFormat,
    Gender,
    _ULCABaseInferenceRequest,
    _ULCABaseInferenceRequestConfig,
    _ULCAText,
)
from ..common.ulca_language import _ULCALanguage


class _ULCATtsInferenceRequestConfig(_ULCABaseInferenceRequestConfig):
    gender: Gender
    samplingRate: Optional[int] = 22050
    audioFormat: AudioFormat = AudioFormat("wav")
    language: _ULCALanguage


class ULCATtsInferenceRequest(_ULCABaseInferenceRequest):
    input: List[_ULCAText]
    config: _ULCATtsInferenceRequestConfig
