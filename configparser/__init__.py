"""Convenience module importing everything from backports.configparser."""

from backports.configparser import (
    RawConfigParser,
    ConfigParser,
    SectionProxy,
    Interpolation,
    BasicInterpolation,
    ExtendedInterpolation,
    LegacyInterpolation,
    NoSectionError,
    DuplicateSectionError,
    DuplicateOptionError,
    NoOptionError,
    InterpolationError,
    InterpolationMissingOptionError,
    InterpolationSyntaxError,
    InterpolationDepthError,
    ParsingError,
    MissingSectionHeaderError,
    ConverterMapping,
    DEFAULTSECT,
    MAX_INTERPOLATION_DEPTH,
)

# names missing from __all__ imported anyway for backwards compatibility.
from backports.configparser import Error, _UNSET, _default_dict, _ChainMap  # noqa: F401

__all__ = (
    "NoSectionError",
    "DuplicateOptionError",
    "DuplicateSectionError",
    "NoOptionError",
    "InterpolationError",
    "InterpolationDepthError",
    "InterpolationMissingOptionError",
    "InterpolationSyntaxError",
    "ParsingError",
    "MissingSectionHeaderError",
    "ConfigParser",
    "RawConfigParser",
    "Interpolation",
    "BasicInterpolation",
    "ExtendedInterpolation",
    "LegacyInterpolation",
    "SectionProxy",
    "ConverterMapping",
    "DEFAULTSECT",
    "MAX_INTERPOLATION_DEPTH",
)
