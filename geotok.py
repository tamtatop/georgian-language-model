import re
_patterns = [r"(\d+)\.(\d+)\.(\d+)", r"(\w+)\.(\w+)\.", r"\'", r"\"", r"\.", r"<br \/>", r",", r"\(", r"\)", r"\!", r"\?", r"\;", r"\:", r"\s+", r"\„", r"\“"]

_replacements = [r"\1/\2/\3", r"\1;\2;", " '  ", "", " . ", " ", " , ", " ( ", " ) ", " ! ", " ? ", " ; ", " : ", " ", " \" ", " \" "]

_patterns_dict = list((re.compile(p), r) for p, r in zip(_patterns, _replacements))


def _basic_georgian_normalize(line: str):
    r"""
    Basic normalization for a line of text.
    Normalization includes
    - lowercasing
    - complete some basic text normalization for English words as follows:
        add spaces before and after '\''
        remove '\"',
        add spaces before and after '.'
        replace '<br \/>'with single space
        add spaces before and after ','
        add spaces before and after '('
        add spaces before and after ')'
        add spaces before and after '!'
        add spaces before and after '?'
        add spaces before and after ':'
        add spaces before and after ';'
        add spaces before and after '„'
        add spaces before and after '“'
        replace multiple spaces with single space

    Returns a list of tokens after splitting on whitespace.
    """

    line = line.lower()
    for pattern_re, replaced_str in _patterns_dict:
        line = pattern_re.sub(replaced_str, line)
    return line.split()