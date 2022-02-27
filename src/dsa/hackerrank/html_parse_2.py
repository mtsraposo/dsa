from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        comment_type = 'Multi' if '\n' in data else 'Single'
        print(f"{comment_type}-line Comment", data, sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print(f"{repr('>>>')} Data", data, sep='\n')


if __name__ == '__main__':
    html = """<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->"""

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
