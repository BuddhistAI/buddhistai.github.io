#!/usr/bin/env python3
"""Collect everyone who takes part in BuddhistAI and update the contributor row.

python3 scripts/update_contributors.py            # fetch from GitHub, write contributors.json, update index.html
python3 scripts/update_contributors.py --offline  # only rebuild index.html from contributors.json

People come from four places:
  1. commit authors of every public BuddhistAI repository (skills, benchmarks, and the rest),
  2. public members of the BuddhistAI organization,
  3. authors of entries in buddhist-prompt-library: every <topic>-<language>/<entry>/CARD.md. A card with
     `github:` adds that GitHub account. A card without it adds `authors` by name, with the
     `avatar:` picture if there is one (these go in "others" in contributors.json),
  4. contributors-extra.json, for people and groups to credit by hand (for example, an author of
     imported data who has no commit here). Its "skip" list leaves out accounts that are not people.
Bots are skipped. Set GITHUB_TOKEN to avoid rate limits.
The org profile (BuddhistAI/.github) reads contributors.json from the website with its own workflow.
"""
import argparse, html, json, os, re, sys, urllib.request
from pathlib import Path

ORG = 'BuddhistAI'
ROOT = Path(__file__).resolve().parent.parent
API = 'https://api.github.com'
START, END = '<!-- contributors:start -->', '<!-- contributors:end -->'


def fetch(url):
    req = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json',
                                               'User-Agent': 'buddhistai-contributors'})
    if os.environ.get('GITHUB_TOKEN'):
        req.add_header('Authorization', f'Bearer {os.environ["GITHUB_TOKEN"]}')
    return urllib.request.urlopen(req)


def frontmatter(text):
    """The simple `key: value` lines between the first two --- lines of a CARD.md."""
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, sep, v = line.partition(':')
        if sep and not line.startswith((' ', '#')):
            v = re.sub(r'\s+#.*$', '', v).strip().strip('"\'')
            out[k.strip()] = v
    return out


LIBRARY = 'buddhist-prompt-library'  # shared, unmeasured entries (was buddhist-skills community/)


def community_cards():
    """Frontmatter of every <group>/<entry>/CARD.md in buddhist-prompt-library (main)."""
    with fetch(f'{API}/repos/{ORG}/{LIBRARY}/git/trees/main?recursive=1') as r:
        tree = json.load(r)['tree']
    cards = []
    for t in tree:
        if re.fullmatch(r'[^/.][^/]*/[^/]+/CARD\.md', t['path']) and not t['path'].startswith('templates/'):
            with fetch(f'https://raw.githubusercontent.com/{ORG}/{LIBRARY}/main/{t["path"]}') as r:
                cards.append(frontmatter(r.read().decode('utf-8')))
    return cards


def get(path):
    """All pages of a GitHub list endpoint."""
    out, url = [], f'{API}{path}{"&" if "?" in path else "?"}per_page=100'
    while url:
        req = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json',
                                                   'User-Agent': 'buddhistai-contributors'})
        if os.environ.get('GITHUB_TOKEN'):
            req.add_header('Authorization', f'Bearer {os.environ["GITHUB_TOKEN"]}')
        with urllib.request.urlopen(req) as r:
            if r.status == 204:
                return out
            out += json.load(r)
            m = re.search(r'<([^>]+)>;\s*rel="next"', r.headers.get('Link') or '')
            url = m.group(1) if m else None
    return out


SKIP = set()


def is_bot(u):
    return (u.get('type') == 'Bot' or u['login'].lower().endswith('[bot]')
            or u['login'].lower() in SKIP)


def collect():
    extra = json.loads((ROOT / 'contributors-extra.json').read_text(encoding='utf-8'))
    SKIP.update(s.lower() for s in extra.get('skip', []))
    people = {}

    def add(login, source, n=0):
        p = people.setdefault(login.lower(), {'login': login, 'contributions': 0, 'sources': []})
        p['contributions'] += n
        if source not in p['sources']:
            p['sources'].append(source)

    for repo in get(f'/orgs/{ORG}/repos?type=public'):
        if repo.get('archived') and not repo.get('size'):
            continue
        try:
            for u in get(f'/repos/{ORG}/{repo["name"]}/contributors'):
                if not is_bot(u):
                    add(u['login'], repo['name'], u.get('contributions', 0))
        except urllib.error.HTTPError as e:  # empty repositories answer 409
            print(f'{repo["name"]}: skipped ({e.code})', file=sys.stderr)
    for u in get(f'/orgs/{ORG}/public_members'):
        if not is_bot(u):
            add(u['login'], 'member')
    others = {}
    try:
        cards = community_cards()
    except (urllib.error.URLError, KeyError) as e:
        print(f'community cards: skipped ({e})', file=sys.stderr)
        cards = []
    for c in cards:
        login = c.get('github', '').lstrip('@')
        if re.fullmatch(r'[A-Za-z0-9-]{1,39}', login):
            if login.lower() not in SKIP:
                add(login, 'community')
        elif c.get('authors'):
            name = c['authors']
            o = others.setdefault(name.lower(), {'name': name, 'sources': ['community']})
            if c.get('avatar', '').startswith('https://'):
                o['avatar'] = c['avatar']
            if c.get('contact', '').startswith('https://'):
                o.setdefault('url', c['contact'])
    for e in extra['people']:
        add(e['login'], 'credited')
    people = sorted(people.values(), key=lambda p: (-p['contributions'], p['login'].lower()))
    return people, sorted(others.values(), key=lambda o: o['name'].lower())


def initials(name):
    words = [w for w in re.sub(r'\(.*?\)', '', name).split() if w[:1].isalpha()]
    return ''.join(w[0].upper() for w in words[:2]) or '?'


def avatar_html(people, others=(), indent='    '):
    rows = [f'{indent}<a href="https://github.com/{p["login"]}" title="{p["login"]}">'
            f'<img src="https://github.com/{p["login"]}.png?size=96" width="48" height="48" '
            f'alt="{p["login"]}"></a>' for p in people]
    for o in others:
        name = html.escape(o['name'])
        pic = (f'<img src="{html.escape(o["avatar"])}" width="48" height="48" alt="{name}">' if o.get('avatar')
               else f'<span class="initials" aria-label="{name}">{html.escape(initials(o["name"]))}</span>')
        url = html.escape(o.get('url') or 'https://github.com/BuddhistAI/buddhist-prompt-library')
        rows.append(f'{indent}<a href="{url}" title="{name}">{pic}</a>')
    return '\n'.join(rows)


def replace_between(text, body):
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        raise SystemExit(f'markers {START} / {END} not found')
    k = text.rfind('\n', 0, j) + 1
    return text[:i + len(START)] + '\n' + body + '\n' + text[k:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--offline', action='store_true')
    a = ap.parse_args()
    cfile = ROOT / 'contributors.json'
    if a.offline:
        data = json.loads(cfile.read_text(encoding='utf-8'))
        people, others = data['people'], data.get('others', [])
    else:
        people, others = collect()
        cfile.write_text(json.dumps({'org': ORG, 'people': people, 'others': others}, indent=2,
                                    ensure_ascii=False) + '\n', encoding='utf-8')
    page = ROOT / 'index.html'
    text = page.read_text(encoding='utf-8')
    new = replace_between(text, avatar_html(people, others))
    if new != text:
        page.write_text(new, encoding='utf-8')
    print(f'{len(people) + len(others)} contributors: '
          + ', '.join([p['login'] for p in people] + [o['name'] for o in others]))


if __name__ == '__main__':
    main()
