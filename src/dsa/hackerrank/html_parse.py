import re


def parse_html(s):
    without_comments = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    attribute_pattern = r'(?=(?:\s+[\-a-z]+(?:=[\'\"].*?[\'\"])?)*(?: /)?>)'
    parsed = re.findall(r'<(?P<start>[a-z1-9]+)(?=(?:\s+[\-a-z]+(?:=[\'\"].*?[\'\"])?)*>)'
                        r'|<(?P<empty>[a-z1-9]+)(?=(?:\s+[\-a-z]+(?:=[\'\"].*?[\'\"])?)* />)'
                        r'|(?<= )(?P<attrb>[a-z]+[\-a-z]*)=[\'\"](?P<value>.*?)[\'\"]'
                        + attribute_pattern
                        + r'|(?<= )(?P<none_attrb>[a-z]+[\-a-z]*)'
                        + attribute_pattern
                        + r'|</(?P<end>[a-z1-9]+)>', without_comments)
    return parsed


def print_parsed(ps):
    stdout = ''
    for p in ps:
        stdout += f'Start : {p[0]}\n' if p[0] != '' else ''
        stdout += f'End   : {p[-1]}\n' if p[-1] != '' else ''
        stdout += f'Empty : {p[1]}\n' if p[1] != '' else ''
        stdout += f'-> {p[-2]} > None\n' if p[-2] != '' else ''
        stdout += f'-> {p[2]} > {p[3]}\n' if p[2] != '' else ''
    print(stdout)


if __name__ == "__main__":
    html1 = "<!-- Comments -->" \
            "<html>" \
            "<head>" \
            "<title>HTML Parser - I</title>" \
            "</head>" \
            "<body data-modal-target class='1'>" \
            "<h1>HackerRank</h1>" \
            "<br />" \
            "</body></html> "
    parsed = parse_html(html1)
    print_parsed(parsed)
