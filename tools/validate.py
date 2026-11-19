#!/usr/bin/env python3
"""Validation for the inference booth screen. All checks must pass before build lock.

Checks (from the build prompt):
 1. 15 scenes, data-id 1-15 in order
 2. No em dashes or en dashes anywhere in the HTML
 3. Every headline <= 7 words, every support <= 12 words
 4. Five spine headlines carry exactly one red span each; layer stack rows are
    Run, Optimize, Distribute, Gate, Deliver; mantra beats are
    Run. Optimize. Distribute. Gate. Deliver.
 5. Every src/href/url() reference resolves to an existing local file
 6. Headlines match the copy doc table EXACTLY (all 16, word for word)
 7. Credits from the copy doc appear on their scenes
 8. <img> is void (no closing tag); tag balance checked for everything else
 9. Every scene has at least one continuous (infinite) animation
 Extras: no document.write, no SMIL, mantra drift, loop math, and the v1.3
 acceptance checks V2 to V14 (curves, retired vocabulary, scene 6 labels,
 scene 13 icon, node --check).
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(ROOT, 'index.html')

EXPECTED_HEADLINES = {
    1: 'Inference worth scaling.',
    2: 'AI demand and cost are compounding.',
    3: 'The bill outgrows the budget.',
    4: 'Scarce chips, stranded capacity.',
    5: 'Inference chained to one provider.',
    6: 'Every token takes one path.',
    7: 'Run any model, any modality, any chip.',
    8: 'Optimize in the open.',
    9: 'Distribute across the whole fleet.',
    10: 'Gate every request.',
    11: 'Deliver AI as a service.',
    12: 'A trillion tokens a month.',
    13: 'Up to 70% lower token costs.',
    14: '233% ROI over three years.',
    15: 'Become an AI model provider.',
}

EXPECTED_SUPPORTS = {
    1: 'Models you own. Costs you control.',
    2: 'More users. More agents. More tokens.',
    3: 'Costs climb unpredictably as usage scales.',
    4: 'GPUs idle in one cluster, exhausted in another.',
    5: 'Their models. Their prices. Their rules.',
    6: 'One request. One path. Five layers.',
    7: 'Leading performance. Text, voice, vision.',
    8: 'New models, validated and optimized in days, every month.',
    9: '3× throughput. 2× faster first token.',
    10: 'Identity. Rate limits. Guardrails.',
    11: 'Where your data lives. Sovereign to edge.',
    12: "Powering Red Hat's Agentic SDLC.",
    13: 'Most of our traffic now runs open weight.',
    14: 'GPU utilization, from 30% to 80%.',
    15: 'Your models. Your prices. Your rules.',
}

EXPECTED_CREDITS = {
    7: 'MLPerf Inference v6.0, 2026',
    8: 'Red Hat AI validated models, 2026',
    9: 'llm-d + vLLM, 2026',
    12: 'EnMaaS, Red Hat, 2026',
    13: 'Red Hat EnMaaS pilot, 2026',
    14: 'Forrester TEI, Feb 2026',
}

SPINE_SCENES = [7, 8, 9, 10, 11]
LAYER_ROWS = ['Run', 'Optimize', 'Distribute', 'Gate', 'Deliver']

results = []


def check(name, ok, detail=''):
    results.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))


def strip_tags(s):
    # Replace tags with nothing (not a space): tag-stripping with a space can
    # insert false spaces and break word counts / exact matching.
    return re.sub(r'<[^>]+>', '', s)


def norm_ws(s):
    # HTML collapses runs of whitespace to a single space at render time.
    return re.sub(r'\s+', ' ', s).strip()


def main():
    with open(HTML_PATH, encoding='utf-8') as f:
        html = f.read()

    # ---- Check 1: 16 scenes, data-id 1-16 in order ----
    ids = [int(m) for m in re.findall(r'<div class="scene[^>]*?data-id="(\d+)"', html)]
    check('1. 15 scenes, data-id 1-15 in order', ids == list(range(1, 16)),
          f'found {ids}')

    # Split per-scene blocks
    scene_blocks = {}
    for m in re.finditer(r'<div class="scene[^>]*?data-id="(\d+)"', html):
        sid = int(m.group(1))
        start = m.start()
        nxt = re.search(r'<div class="scene[^>]*?data-id="\d+"', html[m.end():])
        end = m.end() + nxt.start() if nxt else html.find('<script>')
        scene_blocks[sid] = html[start:end]

    # ---- Check 2: no em or en dashes ----
    ems = html.count('\u2014')
    ens = html.count('\u2013')
    check('2. No em or en dashes', ems == 0 and ens == 0,
          f'{ems} em, {ens} en')

    # ---- Check 3 + 6: word limits and exact copy ----
    ok_words = True
    ok_exact = True
    details = []
    for sid in range(1, 16):
        block = scene_blocks[sid]
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', block, re.S)
        sup = re.search(r'<p class="support"[^>]*>(.*?)</p>', block, re.S)
        h1_text = norm_ws(strip_tags(h1.group(1))) if h1 else ''
        sup_text = norm_ws(strip_tags(sup.group(1))) if sup else ''
        hw = len([w for w in h1_text.split() if w])
        sw = len([w for w in sup_text.split() if w])
        if hw > 7:
            ok_words = False
            details.append(f'scene {sid} headline {hw} words')
        if sw > 12:
            ok_words = False
            details.append(f'scene {sid} support {sw} words')
        if h1_text != EXPECTED_HEADLINES[sid]:
            ok_exact = False
            details.append(f'scene {sid} headline mismatch: {h1_text!r}')
        if sup_text != EXPECTED_SUPPORTS[sid]:
            ok_exact = False
            details.append(f'scene {sid} support mismatch: {sup_text!r}')
    check('3. Headlines <= 7 words, supports <= 12 words', ok_words,
          '; '.join(details) if not ok_words else 'all within limits')
    check('6. Headlines + supports match copy doc exactly', ok_exact,
          '; '.join(details) if not ok_exact else '15 headlines and 15 supports, word for word')

    # ---- Check 4: spine red spans, layer rows, mantra ----
    ok_spine = True
    spine_detail = []
    for sid in SPINE_SCENES:
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', scene_blocks[sid], re.S)
        reds = re.findall(r'<span[^>]*color:\s*var\(--rh-red\)[^>]*>', h1.group(1)) if h1 else []
        if len(reds) != 1:
            ok_spine = False
            spine_detail.append(f'scene {sid} has {len(reds)} red spans')
    check('4a. Five spine headlines carry exactly one red span each', ok_spine,
          '; '.join(spine_detail) if not ok_spine else 'Run/Optimize/Distribute/Gate/Deliver in red')

    rows = re.findall(r'<span class="layer-label">([^<]+)</span>', html)
    check('4b. Layer stack rows', rows == LAYER_ROWS, f'found {rows}')

    # Scene 12 used to be the mantra. It is gone: Deliver cuts straight to the trillion.
    check('4c. The mantra scene is gone, markup and classes alike',
          'class="mantra"' not in html and 'beat-word' not in html
          and 'beam-node' not in html and 'node-pulse' not in html
          and 'Every token has a price' not in html and 'Five moves' not in html,
          "mantra={} beats={} nodes={}".format(
              html.count('class="mantra"'), html.count('beat-word'),
              html.count('node-pulse')))

    # ---- Check 5: local references resolve ----
    refs = []
    refs += re.findall(r'src="([^"]+)"', html)
    refs += re.findall(r'href="([^"]+)"', html)
    refs += re.findall(r'url\((?:\'|")?([^\'")]+)(?:\'|")?\)', html)
    # JS-populated icon references inside the script
    refs += re.findall(r'\./assets/icons/[A-Za-z0-9._-]+\.png', html)
    missing = []
    network = []
    for r in set(refs):
        if r.startswith('#'):
            continue  # same-document fragment (SVG use href="#env-set")
        if r.startswith(('http:', 'https:', '//', 'data:')):
            network.append(r)
            continue
        if not os.path.exists(os.path.join(ROOT, r)):
            missing.append(r)
    check('5. All src/href/url() references resolve locally',
          not missing and not network,
          f'missing={sorted(set(missing))} network={sorted(set(network))}')

    # ---- Check 7: credits appear on their scenes ----
    ok_credits = True
    credit_detail = []
    for sid, credit in EXPECTED_CREDITS.items():
        if credit not in scene_blocks[sid]:
            ok_credits = False
            credit_detail.append(f'scene {sid} missing {credit!r}')
    # and no credit text leaking onto wrong scenes
    for sid in range(1, 16):
        for other_sid, credit in EXPECTED_CREDITS.items():
            if sid != other_sid and credit in scene_blocks[sid]:
                ok_credits = False
                credit_detail.append(f'scene {sid} wrongly carries {credit!r}')
    check('7. Credits appear on their scenes (and only there)', ok_credits,
          '; '.join(credit_detail) if not ok_credits else '6 credits, correct scenes')

    # ---- Check 8: img void, tag balance ----
    closed_imgs = re.findall(r'</img>', html)
    ok_img = not closed_imgs

    class BalanceParser(HTMLParser):
        VOID = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'area', 'base', 'col',
                'embed', 'track', 'wbr'}
        def __init__(self):
            super().__init__()
            self.stack = []
            self.errors = []
        def handle_starttag(self, tag, attrs):
            if tag not in self.VOID:
                self.stack.append(tag)
        def handle_endtag(self, tag):
            if tag in self.VOID:
                return
            if not self.stack or self.stack[-1] != tag:
                self.errors.append(f'unexpected </{tag}> (stack top: {self.stack[-1] if self.stack else "empty"})')
            else:
                self.stack.pop()

    parser = BalanceParser()
    parser.feed(html)
    ok_balance = not parser.errors and not parser.stack
    check('8. <img> void and all other tags balanced',
          ok_img and ok_balance,
          f'closed_imgs={len(closed_imgs)} errors={parser.errors[:3]} unclosed={parser.stack}')

    # ---- Check 9: every scene has continuous animation ----
    # Collect every animated selector: from CSS rules with 'animation:' and
    # from keyframe-consuming classes, plus JS-generated classes.
    css = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    animated_classes = set(re.findall(r'\.([A-Za-z0-9_-]+)\s*\{[^}]*animation\s*:', css))
    animated_classes |= set(re.findall(r'\.([A-Za-z0-9_-]+)\s*,?\s*\{[^}]*animation\s*:', css))
    # classes that consume keyframes via the shared rules
    # .pill animates only under .starving, so the selector regex above cannot see it.
    for cls in ['token-drift', 'grow-dot', 'bill-col', 'churn-dot', 'idle-dot', 'flow-dot',
                'compress', 'gd-pass', 'gd-block', 'env-track', 'beat-word', 'node-pulse',
                'util-fill', 'flip-a', 'flip-b', 'pulse-soft', 'logo-in', 'canal-token',
                'station-fill', 'pill', 'cache-ring', 'cache-hold', 'bounce-dot',
                'bounce-ring', 'art-drift']:
        if re.search(r'\.' + cls + r'\b', css):
            animated_classes.add(cls)
    js_animated = ['token-drift', 'grow-dot', 'idle-dot', 'churn-dot', 'flow-dot',
                   'gd-pass', 'gd-block', 'bounce-dot', 'bounce-ring']
    static_scenes = []
    infinite_here = re.findall(r'animation[^;]*infinite', css)
    for sid in range(1, 16):
        block = scene_blocks[sid]
        has_animated_class = any(re.search(r'class="[^"]*\b' + re.escape(c) + r'\b', block)
                                 for c in animated_classes | set(js_animated))
        has_js_populated = bool(re.search(r'id="(demand-cols|gpu-field|gpu-requests|run-dots|opt-dots|fleet|affinity|gate-arrivals|tokens)"', block))
        has_js_field = 'data-dots' in block
        has_inline_anim = 'animation:' in block or 'animation-delay' in block or 'mantra-drift' in block
        if not (has_animated_class or (has_js_populated and True) or has_js_field or has_inline_anim):
            static_scenes.append(sid)
    # JS-populated containers get their animation classes from the script; verify
    # each JS init exists for each populated container
    js_inits = {
        'demand-cols': 'grow-dot', 'gpu-field': 'churn-dot', 'gpu-requests': 'bounce-dot',
        'run-dots': 'flow-dot', 'opt-dots': 'flow-dot', 'fleet': 'flow-dot',
        'affinity': 'flow-dot', 'gate-arrivals': 'gd-pass',
    }
    js_missing = []
    for container, cls in js_inits.items():
        container_in_html = f'id="{container}"' in html
        js_generates = re.search(r"getElementById\('" + container + r"'\)", html) and cls in html
        if container_in_html and not js_generates:
            js_missing.append(container)
    check('9. Every scene carries animation (markup or JS-populated)',
          not static_scenes and not js_missing and len(infinite_here) >= 15,
          f'static={static_scenes} js_missing={js_missing} infinite_rules={len(infinite_here)}')

    # ---- Extras ----
    check('X1. No document.write', 'document.write' not in html)
    check('X2. No SMIL', '<animate' not in html and 'begin=' not in html)
    check('X3. Loop math: 15 x 6.4s = 96s', 'LOOP_INTERVAL = 6400' in html and
          'TOTAL_SCENES = 15' in html)
    art13 = 'assets/gen/scene13-river.png'
    check('X4. Scene 12 is a live rate, four parts, and the still render is retired',
          all(k in scene_blocks[12] for k in
              ('s13-river', 's13-loop', 's13-lines', 's13-commit', 's13-node'))
          and 's13-art' not in html and 'scene13-river.png' not in html
          and os.path.exists(os.path.join(ROOT, art13)),
          f"parts={[k for k in ('s13-river','s13-loop','s13-lines','s13-commit','s13-node') if k in scene_blocks[12]]} "
          f"still_on_disk={os.path.exists(os.path.join(ROOT, art13))}")
    check('X5. Fonts referenced locally', all(
        os.path.exists(os.path.join(ROOT, 'fonts', f)) for f in
        ['RedHatDisplay-Medium.woff2', 'RedHatDisplay-Bold.woff2', 'RedHatText-Regular.woff2']))

    # ---- v1.3 acceptance checks, V2 to V14 ----
    def path_points(d):
        nums = [float(x) for x in re.findall(r'-?\d+(?:\.\d+)?', d)]
        return list(zip(nums[0::2], nums[1::2]))

    def first_path(block, cls_pat):
        m = re.search(cls_pat + r'[^>]*?\sd="([^"]+)"', block)
        return m.group(1) if m else None

    def vb(block):
        m = re.search(r'<svg[^>]*viewBox="([^"]+)"', block)
        return m.group(1) if m else None

    def crossing(pts, y):
        for i in range(len(pts) - 1):
            y1, y2 = pts[i][1], pts[i + 1][1]
            if (y1 - y) * (y2 - y) <= 0 and y1 != y2:
                frac = (y1 - y) / (y1 - y2)
                return pts[i][0] + frac * (pts[i + 1][0] - pts[i][0])
        return None

    d2 = first_path(scene_blocks[2], r'class="line-a')
    d3 = first_path(scene_blocks[3], r'class="line-a')
    budget_rule = re.search(r'<line class="budget-rule"[^>]*y1="([\d.]+)"[^>]*y2="([\d.]+)"', scene_blocks[3])
    rule_y = float(budget_rule.group(1)) if budget_rule else None

    check('V2. Scenes 2 and 3 share a viewBox and a byte identical cost path',
          d2 is not None and d2 == d3 and vb(scene_blocks[2]) == vb(scene_blocks[3]) == '0 0 960 300',
          f'viewBox {vb(scene_blocks[2])} vs {vb(scene_blocks[3])}, paths equal={d2 == d3}')

    pts2 = path_points(d2) if d2 else []
    if len(pts2) > 20:
        n = len(pts2) - 1
        step = max(1, n // 10)
        first_slope = abs((pts2[step][1] - pts2[0][1]) / (pts2[step][0] - pts2[0][0]))
        last_slope = abs((pts2[n][1] - pts2[n - step][1]) / (pts2[n][0] - pts2[n - step][0]))
        ratio = last_slope / first_slope if first_slope else 0
    else:
        ratio, first_slope, last_slope = 0, 0, 0
    monotone = all(pts2[i][1] >= pts2[i + 1][1] - 1e-9 for i in range(len(pts2) - 1)) if pts2 else False
    check('V3. Cost path is monotone and accelerating (last tenth >= 5x first tenth)',
          monotone and ratio >= 5,
          f'monotone={monotone} ratio={ratio:.1f}x')

    t3 = re.findall(r'<text[^>]*>(.*?)</text>', scene_blocks[3], re.S)
    t3 = [norm_ws(strip_tags(x)) for x in t3]
    no_units = not re.search(r'\d', ' '.join(t3)) and not re.search(r'class="(axis|gridline|tick)', scene_blocks[3])
    check('V4. Scene 3 has exactly two labels (budget, cost), no digits or units',
          sorted(t3) == ['budget', 'cost'] and no_units,
          f'labels={t3} no_digits_or_units={no_units}')

    x_cross = crossing(pts2, rule_y) if pts2 and rule_y is not None else None
    paths_in_3 = len(re.findall(r'<path ', scene_blocks[3]))
    check('V5. One line in scene 3 crosses the budget rule once, at x 500 to 700',
          'line-b' not in scene_blocks[3] and paths_in_3 == 1
          and x_cross is not None and 500 <= x_cross <= 700,
          f'crosses at x {x_cross if x_cross is None else round(x_cross, 1)}, '
          f'rule y {rule_y}, paths {paths_in_3}, '
          f'red line retired={"line-b" not in scene_blocks[3]}')

    for label, word in [('V6', 'router'), ('V7', 'prefill'), ('V7b', 'decode'),
                        ('V8', 'data never leaves your control')]:
        hits = len(re.findall(re.escape(word), html, re.I))
        check(f'{label}. "{word}" appears zero times', hits == 0, f'{hits} hits')

    check('V9. .reach-dot appears zero times', '.reach-dot' not in html,
          f"{html.count('.reach-dot')} hits")

    s6_texts = [norm_ws(strip_tags(x)) for x in
                re.findall(r'<text[^>]*>(.*?)</text>', scene_blocks[6], re.S)]
    check('V10. Scene 6 names exactly the five rail verbs, in order, and nothing else',
          s6_texts == LAYER_ROWS, f'found {s6_texts}')

    # Deliver must cut straight to the trillion: no scene between them, and scene 11
    # has to be the Deliver frame, so a future insert cannot quietly re-add a beat there.
    s11_text = norm_ws(strip_tags(scene_blocks[11]))
    h1_11 = re.search(r'<h1[^>]*>(.*?)</h1>', scene_blocks[11], re.S)
    h1_12 = re.search(r'<h1[^>]*>(.*?)</h1>', scene_blocks[12], re.S)
    h11 = norm_ws(strip_tags(h1_11.group(1))) if h1_11 else ''
    h12 = norm_ws(strip_tags(h1_12.group(1))) if h1_12 else ''
    check('V11. Deliver cuts straight to the trillion, with nothing in between',
          h11 == 'Deliver AI as a service.' and h12 == 'A trillion tokens a month.'
          and 'mantra' not in scene_blocks[11] and 'mantra' not in scene_blocks[12],
          f'11={h11!r} 12={h12!r}')

    check('V12. Scene 12 engine: 520 u/s lanes, three panels per cut, no randomness',
          'S13_SPEED = 520' in html
          and 'S13_CYCLE = LOOP_INTERVAL / 3' in html
          and 'Math.random' not in html
          and 'restartScene13' in html
          and 'ctrl-dot' not in html and 'ctrl-col' not in html
          and 'agentic-ai-400' not in html,
          f"speed={'S13_SPEED = 520' in html} cycle={'/ 3' in html} "
          f"random={html.count('Math.random')} restart={'restartScene13' in html}")

    net = re.findall(r'(?:src|href)="((?:https?:)?//[^"]+)"', html)
    net += re.findall(r'url\((https?:[^)]+)\)', html)
    check('V13. Every asset local, zero network, zero em and en dashes',
          not net and '\u2014' not in html and '\u2013' not in html,
          f'network={net[:3]}')

    import subprocess
    import tempfile
    scripts = '\n'.join(re.findall(r'<script>(.*?)</script>', html, re.S))
    tmp = os.path.join(tempfile.gettempdir(), 'booth-check.js')
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(scripts)
    try:
        proc = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        ok_node = proc.returncode == 0
        node_detail = (proc.stderr.strip().splitlines() or ['ok'])[0][:160]
    except FileNotFoundError:
        ok_node = False
        node_detail = 'node not found'
    # Scene 7: the dots have to ride the spokes. The v1.3 build cut a shallow diagonal
    # from (140, sy) to (780, 190), which put the top dot 73 units above its own line at
    # the node's left edge and made all five converge 180 units to the right of the box,
    # where they had already faded out. The claim is "five inputs, one runtime", so the
    # geometry is locked here: dot start equals the spoke start, dot end equals the box's
    # left edge, and every leg runs at the speed the spine speaks.
    s7 = scene_blocks[7]
    s7_geom = dict(re.findall(r'const (S7_[A-Z_]+) = (\d+);', html))
    s7_want = {'S7_START_X': '132', 'S7_NODE_LEFT': '430', 'S7_NODE_RIGHT': '600',
               'S7_MID': '190', 'S7_SPEED': '480', 'S7_OUT': '156'}
    spokes = re.findall(r'<line x1="(\d+)" y1="(\d+)" x2="(\d+)" y2="(\d+)"', s7)
    spokes_ok = bool(spokes) and all(
        x1 == '132' and x2 == '430' and y2 == '190' and y1 in ('56', '123', '190', '257', '324')
        for x1, y1, x2, y2 in spokes)
    check('V15. Scene 7 dots ride the spokes into the node at 480 u/s, one stream out',
          s7_geom == s7_want
          and spokes_ok
          and re.search(r'id="run-out"', s7) is not None
          and 'S7_NODE_LEFT - S7_START_X' in html
          and 'S7_MID - sy' in html
          and '/ S7_SPEED' in html
          and '--dx:640px' not in html,
          'geom={} spokes={} out_group={} old_diagonal={}'.format(
              s7_geom, len(spokes), bool(re.search(r'id="run-out"', s7)),
              '--dx:640px' in html))

    check('V14. Extracted script parses under node --check', ok_node, node_detail)

    fails = [r for r in results if not r[1]]
    print()
    print(f'{len(results) - len(fails)}/{len(results)} checks passed')
    if fails:
        print('FAILURES:')
        for name, _, detail in fails:
            print(f'  - {name}: {detail}')
        sys.exit(1)
    print('ALL CHECKS PASS')


if __name__ == '__main__':
    main()
