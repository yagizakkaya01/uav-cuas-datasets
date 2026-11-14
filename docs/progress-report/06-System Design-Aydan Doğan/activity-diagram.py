"""ESC 491 activity diagram: camera path and ESP32 Wi-Fi path in parallel,
joined before the threat score. Matches Section 6.2 'Processing flow'."""
import sys

W, H = 2356, 2612
out = []
add = out.append

C = {
    "blue": ("#dce9f5", "#2f6aa3"),
    "orange": ("#f9e6d6", "#b5651d"),
    "green": ("#e3f1e4", "#3d7d46"),
    "purple": ("#efe1f3", "#8a4ea0"),
    "red": ("#f6dfe1", "#b0404a"),
}
BW, BH = 344, 84
INK = "#1b1f27"
GREY = "#555b66"
FONT = "Inter, DejaVu Sans, sans-serif"
MONO = "DejaVu Sans Mono, monospace"
R = 30  # diamond half-size

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add('<defs><marker id="a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="9" markerHeight="9" '
    f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>')
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

lanes = [(30, 770, "Sensors", "camera · ESP32 receiver (Adil Mert)"),
         (770, 1170, "Visual detection", "Aydan"),
         (1170, 1570, "Fusion and risk", "Mert · Yaren"),
         (1570, 1970, "Knowledge base", "Yağız"),
         (1970, 2326, "Operator and C2", "operator · Mert")]
TOP, BOT = 30, H - 30
add(f'<rect x="30" y="{TOP}" width="{W-60}" height="{BOT-TOP}" fill="#fcfcfd" stroke="#d5d9e0" stroke-width="2"/>')
add(f'<rect x="30" y="{TOP}" width="{W-60}" height="92" fill="#f3f5f8" stroke="#d5d9e0" stroke-width="2"/>')
for x0, x1, title, sub in lanes:
    cx = (x0 + x1) / 2
    if x0 > 30:
        add(f'<line x1="{x0}" y1="{TOP}" x2="{x0}" y2="{BOT}" stroke="#d5d9e0" stroke-width="2"/>')
    add(f'<text x="{cx}" y="74" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="600" fill="{INK}">{title}</text>')
    add(f'<text x="{cx}" y="104" text-anchor="middle" font-family="{MONO}" font-size="18" fill="{GREY}">{sub}</text>')


def box(cx, cy, lines, color):
    fill, stroke = C[color]
    add(f'<rect x="{cx-BW/2}" y="{cy-BH/2}" width="{BW}" height="{BH}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2.8"/>')
    n = len(lines)
    for i, t in enumerate(lines):
        y = cy + (i - (n - 1) / 2) * 28 + 8
        add(f'<text x="{cx}" y="{y}" text-anchor="middle" font-family="{FONT}" font-size="22" fill="{INK}">{t}</text>')


def diamond(cx, cy, label_lines=(), lx=None, ly=None, anchor="start"):
    add(f'<polygon points="{cx},{cy-R} {cx+R},{cy} {cx},{cy+R} {cx-R},{cy}" fill="#ffffff" stroke="{INK}" stroke-width="2.2"/>')
    for i, t in enumerate(label_lines):
        add(f'<text x="{lx}" y="{ly+i*27}" text-anchor="{anchor}" font-family="{FONT}" font-size="21" fill="{INK}">{t}</text>')


def path(pts, label=None, lpos=None, rotate=False):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.4" marker-end="url(#a)"/>')
    if label:
        lx, ly = lpos
        rot = f' transform="rotate(-90 {lx} {ly})"' if rotate else ""
        add(f'<text x="{lx}" y="{ly}"{rot} font-family="{MONO}" font-size="19" fill="{GREY}">{label}</text>')


def bar(y, x0, x1):
    add(f'<rect x="{x0}" y="{y-5}" width="{x1-x0}" height="10" fill="{INK}"/>')


SW, SC = 215, 570          # Sensors lane: Wi-Fi column, camera column
V, F, K, O = 970, 1370, 1770, 2148
h = BH / 2

# start + fork
add(f'<circle cx="{(SW+SC)/2}" cy="165" r="19" fill="{INK}"/>')
FORK = 240
path([((SW + SC) / 2, 184), ((SW + SC) / 2, FORK - 6)])
bar(FORK, 80, 710)
path([(SC, FORK + 5), (SC, 340 - h)])
path([(SW, FORK + 5), (SW, 340 - h)])

# camera path
box(SC, 340, ["Capture video frame"], "blue")
path([(SC + BW / 2, 340), (V - BW / 2, 340)])
box(V, 340, ["Run YOLO detection", "on the frame"], "blue")
path([(V, 340 + h), (V, 480 - R)])
diamond(V, 480, ["UAV detected?"], V + 44, 466)
path([(V - R, 480), (690, 480), (690, 340 + h)], "[no]", (760, 468))
path([(V, 480 + R), (V, 620 - h)], "[yes]", (V + 14, 556))
box(V, 620, ["Update track and estimate", "ground position (known height)"], "blue")
path([(V, 620 + h), (V, 760 - R)])
diamond(V, 760, ["Inside geofenced zone?"], V + 44, 746)
path([(V - R, 760), (620, 760), (620, 340 + h)], "[no]", (760, 748))
path([(V, 760 + R), (V, 900 - h)], "[yes]", (V + 14, 836))
box(V, 900, ["Mark drone position", "as detected"], "blue")
path([(V + BW / 2, 900), (F - BW / 2, 900)])
box(F, 900, ["Map position onto pilot region", "(scaled transformation)"], "orange")

# Wi-Fi path
box(SW, 340, ["Receive 2.4 GHz Wi-Fi", "frames (ESP32)"], "blue")
path([(SW, 340 + h), (SW, 500 - R)])
diamond(SW, 500, ["Drone's Wi-Fi", "signal present?"], SW + 42, 488)
path([(SW, 500 + R), (SW, 820 - R)], "[confirmed]", (SW + 14, 640))
path([(SW - R, 500), (70, 500), (70, 820), (SW - R, 820)], "[not confirmed]", (62, 740), rotate=True)
diamond(SW, 820)  # merge node
JOIN = 1040
path([(SW, 820 + R), (SW, JOIN - 6)])
add(f'<text x="{SW+14}" y="{935}" font-family="{FONT}" font-size="20" font-style="italic" fill="{GREY}">Wi-Fi status</text>')

# join
bar(JOIN, 80, 1530)
path([(F, 900 + h), (F, JOIN - 6)])
path([(F, JOIN + 5), (F, 1150 - h)])

box(F, 1150, ["Compute threat score", "(camera + Wi-Fi)"], "orange")
path([(F, 1150 + h), (F, 1290 - h)])
box(F, 1290, ["Propagate risk and", "line of sight on the grid"], "green")
path([(F, 1290 + h), (F, 1430 - R)])
diamond(F, 1430, ["Above alert level?"], F - 44, 1416, anchor="end")
path([(F + R, 1430), (O - BW / 2, 1430)], "[no]", (F + 52, 1418))
box(O, 1430, ["Update track symbol", "on the map"], "red")
path([(O, 1430 + h), (O, 1545 - 20)])
add(f'<circle cx="{O}" cy="1545" r="19" fill="#ffffff" stroke="{INK}" stroke-width="2.4"/>')
add(f'<path d="M{O-13},{1545-13} L{O+13},{1545+13} M{O-13},{1545+13} L{O+13},{1545-13}" stroke="{INK}" stroke-width="2.4"/>')

path([(F, 1430 + R), (F, 1580 - h)], "[yes]", (F + 14, 1505))
box(F, 1580, ["Plan safe route for", "response team (A*)"], "green")
path([(F + BW / 2, 1580), (K - BW / 2, 1580)])
box(K, 1580, ["Retrieve doctrine", "passages (RAG)"], "purple")
path([(K, 1580 + h), (K, 1720 - h)])
box(K, 1720, ["Generate cited", "recommendation (LLM)"], "purple")
path([(K + BW / 2, 1720), (O - BW / 2, 1720)])
box(O, 1720, ["Show alert, MIL-STD-2525", "symbol and recommendation"], "red")
path([(O, 1720 + h), (O, 1860 - h)])
box(O, 1860, ["Operator reviews", "the recommendation"], "orange")
path([(O, 1860 + h), (O, 2000 - R)])
diamond(O, 2000, ["Accept?"], O + 44, 1988)
path([(O - R, 2000), (K, 2000), (K, 2140 - h)], "[no]", (O - 100, 1988))
path([(O, 2000 + R), (O, 2140 - h)], "[yes]", (O + 14, 2075))
box(K, 2140, ["Record operator", "override"], "orange")
path([(K + BW / 2, 2140), (O - BW / 2, 2140)])
box(O, 2140, ["Log decision", "and response"], "orange")
path([(O, 2140 + h), (O, 2270 - 22)])
add(f'<circle cx="{O}" cy="2270" r="22" fill="#ffffff" stroke="{INK}" stroke-width="2.8"/>')
add(f'<circle cx="{O}" cy="2270" r="13" fill="{INK}"/>')

# note
nx, ny, nw, nh = 50, 2440, 708, 96
add(f'<path d="M{nx},{ny} L{nx+nw-24},{ny} L{nx+nw},{ny+24} L{nx+nw},{ny+nh} L{nx},{ny+nh} z" fill="#f3f5f8" stroke="{GREY}" stroke-width="1.6"/>')
for i, t in enumerate(["The loop runs for every frame (~20 fps).",
                       "ESC 491 scope: one mock drone, daytime, one camera, one ESP32 receiver."]):
    add(f'<text x="{nx+20}" y="{ny+38+i*30}" font-family="{FONT}" font-size="18" fill="#3b414c">{t}</text>')

add("</svg>")
open(sys.argv[1], "w").write("\n".join(out))
