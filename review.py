"""Render the matched homepage studies without a frontend build dependency."""
from html import escape

from build import ROOT, img

STUDIES = [
    ('desk', 'A programmable desk', 'Move one instruction out of the screen.'),
    ('timing', 'The moment before help', 'Choose when an assistant should intervene.'),
    ('stage', 'The world is the interface', 'One image puts the proposition on stage.'),
    ('quiet', 'A quiet research home', 'The same material with no interactive hero.'),
]
RESEARCH = [
    ('realitysketch', 'Draw on the world', 'RealitySketch', 'A sketch can stay attached to an object as it moves.'),
    ('teachable-reality', 'Teach the world', 'Teachable Reality', 'A person demonstrates what a physical control should do.'),
    ('roomshift', 'Rearrange the world', 'RoomShift', 'Mobile robots change a room’s physical layout.'),
]
VISION = 'We invent interfaces that make the physical world a medium for thought and creation.'
PHOTO = 'teachable-reality'


def page(title, base, contents, body_class=''):
    return f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{escape(title)} | Programmable Reality Lab</title>
<link rel="stylesheet" href="{base}studies.css"></head>
<body class="{body_class}">{contents}</body></html>
'''


def modes(name, labels, descriptions, overlay):
    controls = ''.join(f'<input type="radio" name="{name}" id="{name}-{i}" {"checked" if i == 0 else ""}>'
                       for i in range(3))
    buttons = ''.join(f'<label for="{name}-{i}">{label}</label>' for i, label in enumerate(labels))
    captions = ''.join(f'<span class="mode-{i}">{description}</span>' for i, description in enumerate(descriptions))
    # The first state remains usable without JavaScript. Labels activate native radios.
    return f'''
    <fieldset class="experiment {name}">
      <legend>{'Where should the instruction appear?' if name == 'placement' else 'When should help appear?'}</legend>
      {controls}
      <div class="choices">{buttons}</div>
      <div class="scene">
        {img(PHOTO, lead=True)}
        <div class="annotation"><span>{overlay}</span></div>{('<span class="ask">Would you like a hint?</span>' if name == 'timing' else '')}
      </div>
      <p class="readout">{captions}</p>
    </fieldset>'''


def hero(slug):
    if slug == 'desk':
        demo = modes('placement', ('On screen', 'Beside the object', 'On the object'),
                     ('The instruction sits apart from the work. Move it to the desk.',
                      'The same instruction now sits next to the slider.',
                      'The same instruction points directly at the control. Choose another location to move it back.'),
                     'Slide right to grow the tree.')
        return f'''<section class="workshop"><div class="opening"><span class="kind">Interactive sketch</span>
          <h1>What if the instruction lived on the desk?</h1><p>Try putting the same instruction in three places. Notice where your eyes go.</p>
          <p class="thesis">{VISION}</p></div><div class="demo">{demo}
          <p class="source">Photo from <a href="https://ryosuzuki.org/teachable-reality/">Teachable Reality</a>. The overlay is a design illustration.</p></div></section>'''
    if slug == 'timing':
        demo = modes('timing', ('Wait', 'Ask first', 'Offer a hint'),
                     ('Nothing appears. A pause does not tell us whether someone wants help.',
                      'Ask before bringing an instruction into the workspace.',
                      'A hint appears beside the slider. Choose Wait to remove it.'),
                     'Slide right to grow the tree.')
        return f'''<section class="workshop"><div class="opening"><span class="kind">Speculative interaction</span>
          <h1>A pause is not a request for help.</h1><p>Someone stops in the middle of a task. Is this the right moment for an assistant to speak up?</p>
          <p class="thesis">{VISION}</p></div><div class="demo">{demo}
          <p class="source">Photo from <a href="https://ryosuzuki.org/teachable-reality/">Teachable Reality</a>. This is a browser sketch, not a deployed assistant.</p></div></section>'''
    if slug == 'stage':
        return f'''<section class="feature"><div class="opening"><h1>The world is<br> the interface.</h1>
          <p>{VISION}</p><a class="jump" href="#research">Explore the research</a></div>
          <figure>{img(PHOTO, lead=True)}<figcaption>Teachable Reality · Research prototype</figcaption></figure></section>'''
    return f'''<section class="quiet-opening"><div class="opening"><h1>Programmable Reality Lab</h1>
      <p>{VISION}</p><a class="jump" href="#research">Selected research</a></div>
      <figure>{img(PHOTO, lead=True)}<figcaption>Teachable Reality · Research prototype</figcaption></figure></section>'''


def research():
    cards = ''.join(f'''<article><a href="https://ryosuzuki.org/{slug}/">{img(slug)}
      <h3>{verb}</h3><p>{desc}</p><span>{title} · Research prototype</span></a></article>'''
                    for slug, verb, title, desc in RESEARCH)
    return f'<section class="research" id="research"><h2>Selected research</h2><div class="artifacts">{cards}</div></section>'


def study(slug, title):
    items = ''.join(f'<a href="{key}.html"{" aria-current=page" if key == slug else ""}>{name}</a>'
                    for key, name, _ in STUDIES)
    header = '''<header class="masthead"><a class="wordmark" href="./">Programmable Reality Lab</a>
    <nav aria-label="Lab"><a href="#research">Research</a><a href="https://www.colorado.edu/atlas/programmable-reality-lab">About the lab</a></nav></header>'''
    footer = f'''<footer class="study-footer"><a href="./">All homepage studies</a>
      <nav aria-label="Compare homepages">{items}</nav><p>Homepage prototype · Not the official lab website</p></footer>'''
    return page(title, '', f'{header}<main>{hero(slug)}{research()}</main>{footer}', slug)


def build_studies():
    folder = ROOT / 'review'
    folder.mkdir(exist_ok=True)
    for slug, title, _ in STUDIES:
        (folder / f'{slug}.html').write_text(study(slug, title), encoding='utf8')
    cards = ''.join(f'''<article><a href="{slug}.html"><img src="{slug}.webp" alt="" width="600" height="388">
      <h2>{title}</h2><p>{description}</p></a></article>''' for slug, title, description in STUDIES)
    hub = f'''<header class="masthead"><a class="wordmark" href="./">Programmable Reality Lab</a>
      <a href="../">Earlier concepts</a></header><main class="overview">
      <section class="overview-lead"><h1>Four ways to tell the same story.</h1>
      <p>Compare an interactive desk, a choice about when help arrives, a photo-led introduction, and a quiet research home. The research examples stay the same.</p></section>
      <div class="study-grid">{cards}</div>
      <section class="review-questions"><h2>As you compare</h2>
      <ol><li>After five seconds, what does the lab make possible?</li><li>Which parts are real research, and which are illustrations?</li><li>Where would you go to see the work?</li></ol></section></main>
      <footer class="study-footer"><p>Homepage prototypes · Not the official lab website</p><a href="../architecture.html">URL &amp; launch notes</a></footer>'''
    (folder / 'index.html').write_text(page('Homepage studies', '', hub, 'hub'), encoding='utf8')


if __name__ == '__main__':
    build_studies()
