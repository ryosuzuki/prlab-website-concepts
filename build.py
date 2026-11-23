"""Build the review gallery and twenty standalone static homepages."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent / 'site'
PROJECTS = {
    'realitysketch': ('RealitySketch', 'Sketch an annotation that reacts to the object it describes.', 'An augmented sketch traces movement on a physical object.'),
    'holobots': ('HoloBots', 'Give a remote collaborator a physical presence on the table.', 'Small tabletop robots act as tangible avatars in mixed reality.'),
    'teachable-reality': ('Teachable Reality', 'Teach a physical object what a gesture should do.', 'A researcher demonstrates a gesture in front of a physical object.'),
    'roomshift': ('RoomShift', 'Move physical furniture to match a virtual room.', 'A mobile robot moves furniture within a room-scale prototype.'),
    'shapebots': ('ShapeBots', 'Compose a changing form out of small moving robots.', 'A swarm of tabletop robots extends and changes its arrangement.'),
    'cinemaworld': ('CinemaWorld', 'Bring elements of a film into the space around the viewer.', 'A project still shows a film extending into its surrounding space.'),
}
# slug | name | review category | proposition | opening scene | lead artifact | other evidence
CONCEPTS = [
('stage','The Stage','Cinematic','The room is part of the interface.','A virtual seat meets a real chair. Instead of asking you to adapt to a headset, the room changes to meet you.','roomshift','realitysketch','holobots'),
('day','A Day in 2035','Narrative','A day without a separate screen.','Imagine a morning sketch that follows a bicycle wheel, a lunch meeting where a distant hand has a place on the table, and an evening film that spills into the room.','realitysketch','holobots','cinemaworld'),
('field','The Field Guide','Editorial','Look closer at ordinary things.','A pen, a chair, a wooden block: start with something you can hold. Then ask what new behavior a person could give it.','teachable-reality','roomshift','shapebots'),
('exhibit','The Exhibition','Editorial','Six objects you can think with.','Treat each prototype as an exhibit. The point is not the technology inside it, but the action it makes possible.','shapebots','cinemaworld','holobots'),
('manifesto','The Manifesto','Editorial','People should program the world they live in.','A good interface gives someone a new action they can understand, teach, undo, and share. The action matters more than the display.','teachable-reality','realitysketch','roomshift'),
('index','Quiet Index','Reference','Interfaces beyond the screen.','Research in augmented reality, tangible interaction, and robotics at the ATLAS Institute, University of Colorado Boulder.','realitysketch','holobots','shapebots'),
('layers','The Lens','Interactive','One object. Two ways to see it.','Reveal a research image to see how a hand-drawn annotation can follow a moving object.','realitysketch','teachable-reality','cinemaworld'),
('workbench','The Workbench','Process','Start with a thing that refuses to behave.','A prototype is an argument you can put your hands on. Build the smallest version of the new action and see what survives.','shapebots','roomshift','holobots'),
('atlas','The Atlas','Reference','Navigate by what you want to do.','Start with an action instead of a technology. Follow the branches from sketching, arranging, and being together to the systems that support them.','holobots','realitysketch','roomshift'),
('cinema','Second Screen, No Screen','Cinematic','What if the film left the frame?','A scene does not have to stop at the screen. Its objects can enter the living room, making the viewer’s space part of the composition.','cinemaworld','realitysketch','roomshift'),
('letters','Letter from the Lab','Narrative','Dear future collaborator,','We are looking for ordinary moments in which software gets in the way: explaining a movement, reaching someone from afar, or making a room fit a task. Those moments are our starting points.','holobots','realitysketch','teachable-reality'),
('instructions','Instruction Manual','Process','How to teach a room a new trick.','Pick an object. Show it a gesture. Decide what the gesture should mean. Try it again and see whether the rule feels like yours.','teachable-reality','realitysketch','roomshift'),
('catalogue','Catalogue of Behaviors','Reference','Six behaviors for the physical world.','Browse prototypes by the behavior they add, rather than by the hardware they use.','shapebots','roomshift','cinemaworld'),
('conversation','Two People, One Table','Narrative','A shared space should feel shared.','One person is at a table. Another is far away. Both need more than a floating face: they need something in common they can point to and move.','holobots','roomshift','realitysketch'),
('room','The Floor Plan','Interactive','A room can respond without disappearing.','Choose a station to see the kinds of actions that could belong to a table, a seat, or a wall. This is a browser sketch, not a live system.','roomshift','holobots','cinemaworld'),
('taxonomy','The Verb Wall','Reference','Sketch. Teach. Move. Meet.','The work starts with verbs. Each verb leads to a prototype that changes the physical terms of that action.','realitysketch','teachable-reality','holobots'),
('section','Design in Section','Editorial','Between matter and meaning.','Look at an interface in cross-section: the object you touch, the signal the system reads, and the behavior you decide it should have.','realitysketch','teachable-reality','shapebots'),
('score','Interaction Score','Process','An interface is a choreography.','Watch how actions pass between people, objects, and machines. A design can give a person the next move instead of taking it away.','roomshift','shapebots','holobots'),
('rehearsal','Future Rehearsal','Interactive','Try a different version of the same moment.','Choose a scene and compare the familiar interaction with a speculative alternative grounded in a research prototype.','cinemaworld','holobots','teachable-reality'),
('observatory','The Observatory','Cinematic','Study what changes when objects can respond.','A hand turns a block, a robot changes a room, a sketch stays with a moving object. Small observed moments make the research claims visible.','shapebots','realitysketch','roomshift'),
]
LAB = 'Programmable Reality Lab'


def project_link(key):
    return f'https://ryosuzuki.org/{key}/'


def img(key, lead=False, prefix='../'):
    file = key if key in PROJECTS else 'shapebots-detail'
    alt = PROJECTS.get(key, ('', '', 'A close view of a ShapeBots prototype.'))[2]
    return f'<img src="{prefix}assets/{file}.jpg" alt="{escape(alt)}" {"fetchpriority=high" if lead else "loading=lazy"}>'


def card(key):
    name, description, _ = PROJECTS[key]
    return f'<a class="work" href="{project_link(key)}">{img(key)}<div><h3>{name}</h3><p>{description}</p></div></a>'


def strip(keys, title='Research behind the idea'):
    return f'<section class="evidence" id="research"><h2>{title}</h2><div class="works">{"".join(map(card, keys))}</div></section>'


def picture(key, lead=True):
    return f'<figure class="artifact">{img(key, lead)}<figcaption><a href="{project_link(key)}">{PROJECTS[key][0]}</a></figcaption></figure>'


def intro(head, dek, action=True):
    link = '<a class="cta" href="#research">Explore the research</a>' if action else ''
    return f'<div class="intro"><h1>{escape(head)}</h1><p>{escape(dek)}</p>{link}</div>'


def tabs(labels, panels, cls=''):
    buttons = ''.join(f'<button type="button" aria-controls="panel-{i}" aria-expanded="{str(i == 0).lower()}">{escape(label)}</button>' for i, label in enumerate(labels))
    contents = ''.join(f'<section id="panel-{i}" class="switch-panel"{"" if i == 0 else " hidden"}>{panel}</section>' for i, panel in enumerate(panels))
    return f'<div class="switch {cls}"><div class="switch-buttons">{buttons}</div>{contents}</div>'


def composition(slug, head, dek, a, b, c):
    all_keys = tuple(PROJECTS)
    I, P = intro(head, dek), picture(a)
    if slug == 'stage':
        return f'<div class="stage-intro">{I}{P}</div>'+strip((b, c))
    if slug == 'day':
        sections = zip(('08:10 / Repair','12:30 / Meet','20:20 / Watch'), (a,b,c))
        return f'<div class="story-intro">{I}</div><div class="timeline" id="research">'+''.join(f'<article><h2>{label}</h2>{card(key)}</article>' for label,key in sections)+'</div>'
    if slug == 'field':
        return f'<div class="field-opening">{I}<aside>{P}<p>Observation: a demonstration can become a rule.</p></aside></div>'+strip((a,b,c),'Specimens')
    if slug == 'exhibit':
        return f'<div class="museum-intro">{I}<div class="plinth">{P}</div></div>'+strip(all_keys,'The collection')
    if slug == 'manifesto':
        return f'<div class="broadside">{I}<ol><li>Begin with an action, not a device.</li><li>Make the rule visible.</li><li>Keep the next move with the person.</li></ol></div>'+strip((a,b,c),'How we test the idea')
    if slug == 'index':
        return f'<div class="index-intro">{I}<span>ATLAS Institute<br>University of Colorado Boulder</span></div>'+strip(all_keys,'Selected work')
    if slug == 'layers':
        compare = f'<div class="lens" data-reveal>{img(a, True)}<div class="veil"></div></div><label>Reveal the research image <input type="range" min="0" max="100" value="55"></label>'
        return f'<div class="lens-intro">{I}<div>{compare}</div></div>'+strip((a,b,c))
    if slug == 'workbench':
        notes = '<ul><li><b>Build</b> a small moving unit.</li><li><b>Arrange</b> units into a useful shape.</li><li><b>Observe</b> where control becomes hard.</li></ul>'
        return f'<div class="bench">{I}{notes}<div class="bench-media">{img("shapebots-detail",True)}{P}</div></div>'+strip((a,b,c),'Off the bench')
    if slug == 'atlas':
        return f'<div class="map-intro">{I}</div><div class="map" id="research">'+''.join(f'<div><h2>{verb}</h2>{card(key)}</div>' for verb,key in zip(('Be together','Explain motion','Rearrange space'),(a,b,c)))+'</div>'
    if slug == 'cinema':
        return f'<div class="cinema-screen">{P}{I}</div>'+strip((a,b,c),'Beyond the frame')
    if slug == 'letters':
        return f'<div class="letter">{intro(head,dek,False)}<p>If you make a new way to point, touch, teach, or share, we want to see what someone does with it when you step away.</p><a href="#research">Read the prototypes</a><p class="signature">— Programmable Reality Lab</p></div>'+strip((a,b,c),'Enclosures')
    if slug == 'instructions':
        return f'<div class="manual">{I}<ol class="steps"><li>Choose a physical object.</li><li>Demonstrate an action.</li><li>Give the action a meaning.</li><li>Test the result in place.</li></ol>{P}</div>'+strip((a,b,c),'Examples')
    if slug == 'catalogue':
        return f'<div class="catalogue-intro">{I}</div><section id="research" class="catalogue"><h2>Behavior index</h2>'+''.join(f'<details><summary>{PROJECTS[k][1]}</summary>{card(k)}</details>' for k in all_keys)+'</section>'
    if slug == 'conversation':
        return f'<div class="conversation">{I}<div class="dialogue"><p><b>Here</b> “Put it next to the block on my left.”</p><p><b>Elsewhere</b> “Let me show you.”</p></div>{P}</div>'+strip((a,b,c),'Prototypes for being together')
    if slug == 'room':
        return f'<div class="room">{intro(head,dek,False)}'+tabs(('Table','Chair','Wall'), tuple(card(k) for k in (b,a,c)), 'floorplan')+'</div>'+strip((a,b,c))
    if slug == 'taxonomy':
        return f'<div class="verbs">{I}<div id="research">'+''.join(f'<a href="{project_link(k)}"><strong>{verb}</strong><span>{PROJECTS[k][0]}</span></a>' for verb,k in zip(('Sketch','Teach','Move','Meet','Compose','Watch'),('realitysketch','teachable-reality','roomshift','holobots','shapebots','cinemaworld')))+'</div></div>'
    if slug == 'section':
        layers = (('Matter','A physical object that is already there.'),('Signal','Motion or a gesture the system can read.'),('Meaning','A rule you can decide, test, and change.'))
        return f'<div class="cross-section">{I}<div>{P}<ol>{"".join(f"<li><b>{t}</b><span>{s}</span></li>" for t,s in layers)}</ol></div></div>'+strip((a,b,c))
    if slug == 'score':
        return f'<div class="score">{I}<div class="notation"><div>Person <b>Plan</b><b>Move</b><b>Correct</b></div><div>Object <b>Stay</b><b>Respond</b><b>Settle</b></div><div>System <b>Sense</b><b>Act</b><b>Yield</b></div></div>{P}</div>'+strip((a,b,c))
    if slug == 'rehearsal':
        pairs = (('Watch','The action stops at the screen.',a),('Meet','Remote participants point through a video window.',b),('Teach','The rule is buried inside a settings menu.',c))
        panels = tuple(f'<div class="before"><h2>Before</h2><p>{before}</p></div><div class="after"><h2>What if?</h2>{card(k)}</div>' for _,before,k in pairs)
        return f'<div class="rehearsal">{intro(head,dek,False)}'+tabs(tuple(p[0] for p in pairs),panels)+'</div>'+strip((a,b,c))
    if slug == 'observatory':
        return f'<div class="observatory">{P}{I}<div class="contact-sheet">{img("shapebots-detail")}{img(b)}{img(c)}</div></div>'+strip((a,b,c),'Observation notes')
    raise ValueError(slug)


def html(title, base, body, script=False):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{escape(title)}</title>
<link rel="stylesheet" href="{base}style.css">{f'<script defer src="{base}review.js"></script>' if script else ''}</head>{body}</html>
'''


def build():
    concepts = ROOT / 'concepts'
    concepts.mkdir(exist_ok=True)
    for i, (slug, label, category, head, dek, a, b, c) in enumerate(CONCEPTS):
        next_slug = CONCEPTS[(i+1) % len(CONCEPTS)][0]
        prev_slug = CONCEPTS[(i-1) % len(CONCEPTS)][0]
        top = f'<header class="labbar"><a href="../">{LAB}</a><nav aria-label="Homepage sections"><a href="#research">Research</a><a href="https://www.colorado.edu/atlas/">ATLAS</a></nav></header>'
        review = f'<footer class="reviewbar"><a href="../">All concepts</a><span>{i+1:02d} / 20 · {label}</span><a href="{prev_slug}.html">Previous</a><a href="{next_slug}.html">Next</a></footer>'
        body = f'<body class="concept {slug}">{top}<main>{composition(slug,head,dek,a,b,c)}</main>{review}</body>'
        (concepts / f'{slug}.html').write_text(html(f'{label} | {LAB}', '../', body, True))
    entries = ''.join(f'''<article class="entry" data-category="{category}"><a href="concepts/{slug}.html">
    <div class="preview {slug}"><img src="previews/{slug}.webp" alt="" loading="lazy"></div>
    <div class="entry-top"><span>{i:02d}</span><strong>{label}</strong><span>{category}</span></div><p>{escape(head)}</p></a>
    <label class="select"><input type="checkbox" value="{slug}" data-label="{i:02d} {label}"> Shortlist</label></article>'''
    for i,(slug,label,category,head,_,a,b,c) in enumerate(CONCEPTS,1))
    gallery = f'''<body class="gallery"><header class="gallery-bar"><a href="./">{LAB}</a><a href="architecture.html">URL &amp; launch notes</a></header>
    <main><section class="gallery-heading"><h1>Twenty ways<br>into the lab.</h1><div><p>Homepage proposals for the Programmable Reality Lab. Each uses real project imagery and takes a different route from a possible future to the research behind it.</p><a href="review/">Compare the four new homepage studies</a></div></section>
    <section class="review-tools" id="concepts" aria-label="Review tools"><label>Filter <select id="filter"><option>All concepts</option>{"".join(f"<option>{c}</option>" for c in dict.fromkeys(row[2] for row in CONCEPTS))}</select></label>
    <button id="copy" type="button">Copy shortlist</button><span id="selection" role="status">No concepts shortlisted</span></section><div class="entries">{entries}</div></main>
    <footer class="gallery-bar"><span>Design review · Not the official lab website</span><a href="architecture.html">URL &amp; launch notes</a></footer></body>'''
    (ROOT / 'index.html').write_text(html(f'Homepage concepts | {LAB}', '', gallery, True))


if __name__ == '__main__':
    build()
