# Programmable Reality Lab homepage concepts

Twenty standalone homepage proposals and a review gallery. This is a design draft, not the official lab website. Only public research examples and media are included. The review controls store choices in the visitor's browser; no feedback is transmitted.

## Preview

Run `python3 build.py` to regenerate the gallery and concept HTML, then `python3 -m http.server --directory site` and open localhost:8000. The site has no build-time dependencies other than Python 3. The reviewed desktop thumbnails in `site/previews/` are checked in; update the corresponding thumbnail when a concept changes.

- `build.py`: concept copy, markup, and public research references.
- `site/style.css`: layout and visual direction.
- `site/review.js`: shortlist and optional demo interactions.
- `site/architecture.html`: domain, URL structure, migration sequence, and public image credits.

Deployment uses GitHub Pages from the separate review repository and does not claim the lab’s custom domain. The production repository and DNS are out of scope.

## Matched homepage studies

Run `python3 review.py` to regenerate the four studies and their comparison page in `site/review/`. The three evidence projects and lead photograph are deliberately held constant. The desk and timing studies use native radio inputs and CSS; JavaScript is not required. The earlier twenty concepts remain available as layout explorations.
