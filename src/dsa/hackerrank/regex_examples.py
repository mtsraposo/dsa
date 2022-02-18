import re

html = "<!-- Comments -->" \
       "<html>" \
       "<head>" \
       "<title>HTML Parser - I</title>" \
       "</head>" \
       "<body data-modal-target class='1'>" \
       "<h1>HackerRank</h1>" \
       "<br />" \
       "</body></html> "

html2 = """<meta http-equiv="refresh" content="5;url=http://example.com/" />"""

html3 = """<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/TitilliumMaps.font.js"></script><h1>Business Solutions</h1><br />
<h2>Business Insurance</h2><script type="text/javascript">
    Cufon.replace('h1, h2', { fontFamily: "TitilliumMaps26L", hover: true });
</script>"""

html4 = """<article class="hentry">
  <!-- <header>
    <h1 class="entry-title">But Will It Make You Happy?</h1>
    <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
    <p class="byline author vcard">
        By <span class="fn">Stephanie Rosenbloom</span>
    </p>
  </header> -->

  <div class="entry-content">
      <p>...article text...</p>
      <p>...article text...</p>

      <figure>
        <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
        <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
      </figure>

      <p>...article text...</p>
      <p>...article text...</p>

      <aside>
        <h2>Share this Article</h2>
        <ul>
          <li>Facebook</li>
          <li>Twitter</li>
          <li>Etc</li>
        </ul>
      </aside>

      <div class="entry-content-asset">
        <a href="photo-full.png">
          <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
        </a>
      </div>

      <p>...article text...</p>
      <p>...article text...</p>

      <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
  </div>

  <footer>
    <p>
      A version of this article appeared in print on August 8,
      2010, on page BU1 of the New York edition.
    </p>
    <div class="source-org vcard copyright">
        Copyright 2010 <span class="org fn">The New York Times Company</span>
    </div>
  </footer>
</article>"""

html_no_comments = re.sub(r'<!--.*-->', '', html4, flags=re.S)

parsed = re.findall(r'<(?P<start>[a-z1-9]+)(?=(?: [\-a-z]+(?:=[\'\"].*?[\'\"])?)*>)'
                    r'|<(?P<empty>[a-z1-9]+)(?=(?: [\-a-z]+(?:=[\'\"].*?[\'\"])?)* />)'
                    r'|(?<= )(?P<attrb>[a-z]+[\-a-z]*)=[\'\"](?P<value>.*?)[\'\"]'
                    r'(?=(?: [\-a-z]+[=]?[\'\"]?.*?[\'\"]?)*(?: /)?>)'
                    r'|(?<= )(?P<none_attrb>[a-z]+[\-a-z]*)'
                    r'(?=>|(?: [\-a-z]+[=]?[\'\"]?.*?[\'\"]?)*>)'
                    r'|</(?P<end>[a-z1-9]+)>', html4)

for p in parsed:
    print(f'Start : {p[0]}') if p[0] != '' else ''
    print(f'End   : {p[-1]}') if p[-1] != '' else ''
    print(f'Empty : {p[1]}') if p[1] != '' else ''
    print(f'-> {p[-2]} > None') if p[-2] != '' else ''
    print(f'-> {p[2]} > {p[3]}') if p[2] != '' else ''

