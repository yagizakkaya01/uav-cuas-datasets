"""ESC 491 activity diagram, compact layout with large text so it stays
readable when printed at text width. Same activities, decisions and flows as
the previous version (main, 3b25884); only the sizes and line breaks change."""
import sys
from PIL import ImageFont

FONT = "Inter, DejaVu Sans, sans-serif"
MONO = "DejaVu Sans Mono, monospace"
F_REG = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Regular.otf", 32)
INK, GREY = "#1b1f27", "#555b66"
C = {
    "blue": ("#dce9f5", "#2f6aa3"),
    "orange": ("#f9e6d6", "#b5651d"),
    "green": ("#e3f1e4", "#3d7d46"),
    "purple": ("#efe1f3", "#8a4ea0"),
    "red": ("#f6dfe1", "#b0404a"),
}
FS, LH, BW, R, GAP = 32, 39, 300, 34, 62

out = []
add = out.append


def wrap(text, width, font=F_REG):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def bh(label):
    return 26 + LH * len(wrap(label, BW - 26))


def box(cx, cy, label, color):
    lines = wrap(label, BW - 26)
    h = 26 + LH * len(lines)
    fill, stroke = C[color]
    add(f'<rect x="{cx-BW/2}" y="{cy-h/2}" width="{BW}" height="{h}" rx="20" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
    for i, t in enumerate(lines):
        y = cy + (i - (len(lines) - 1) / 2) * LH + 11
        add(f'<text x="{cx}" y="{y}" text-anchor="middle" font-family="{FONT}" font-size="{FS}" fill="{INK}">{t}</text>')
    return h / 2


def diamond(cx, cy, lines=(), lx=0, ly=0, anchor="start"):
    add(f'<polygon points="{cx},{cy-R} {cx+R},{cy} {cx},{cy+R} {cx-R},{cy}" fill="#ffffff" stroke="{INK}" stroke-width="2.6"/>')
    for i, t in enumerate(lines):
        add(f'<text x="{lx}" y="{ly+i*33}" text-anchor="{anchor}" font-family="{FONT}" font-size="29" fill="{INK}">{t}</text>')


def path(pts, label=None, lpos=None, rotate=False):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.8" marker-end="url(#a)"/>')
    if label:
        lx, ly = lpos
        rot = f' transform="rotate(-90 {lx} {ly})"' if rotate else ""
        add(f'<text x="{lx}" y="{ly}"{rot} font-family="{MONO}" font-size="26" fill="{GREY}">{label}</text>')


def bar(y, x0, x1):
    add(f'<rect x="{x0}" y="{y-6}" width="{x1-x0}" height="12" fill="{INK}"/>')


# lanes
W = 2080
lanes = [(20, 700, "Sensors", "camera (Aydan) · ESP32 receiver (Adil Mert)"),
         (700, 1040, "Visual detection", "Aydan"),
         (1040, 1380, "Fusion and risk", "Mert · Yaren"),
         (1380, 1720, "Knowledge base", "Yağız"),
         (1720, 2060, "Operator and C2", "operator · Mert")]
SW, SC, V, F, K, O = 190, 525, 870, 1210, 1550, 1890

body = []  # drawn after we know H
out_lanes_at = len(out)

# ---- flow (y computed top-down) ----
y = 175
add(f'<circle cx="{(SW+SC)/2}" cy="{y}" r="22" fill="{INK}"/>')
FORK = 250
path([((SW + SC) / 2, y + 22), ((SW + SC) / 2, FORK - 8)])
bar(FORK, 60, 680)

r1 = FORK + 50 + max(bh("Receive 2.4 GHz Wi-Fi frames (ESP32)"), bh("Capture video frame"), bh("Run YOLO detection on the frame")) / 2
hw = box(SW, r1, "Receive 2.4 GHz Wi-Fi frames (ESP32)", "blue")
hc = box(SC, r1, "Capture video frame", "blue")
hv = box(V, r1, "Run YOLO detection on the frame", "blue")
path([(SW, FORK + 6), (SW, r1 - hw)])
path([(SC, FORK + 6), (SC, r1 - hc)])
path([(SC + BW / 2, r1), (V - BW / 2, r1)])
cam_bottom = r1 + hc

d1 = r1 + hv + GAP + R
path([(V, r1 + hv), (V, d1 - R)])
diamond(V, d1, ["UAV detected?"], V + 46, d1 - 14)
path([(V - R, d1), (640, d1), (640, cam_bottom)], "[no]", (660, d1 - 12))
r2h = bh("Update track and estimate ground position (known height)") / 2
r2 = d1 + R + GAP + r2h
path([(V, d1 + R), (V, r2 - r2h)], "[yes]", (V + 14, d1 + R + 40))
box(V, r2, "Update track and estimate ground position (known height)", "blue")
d2 = r2 + r2h + GAP + R
path([(V, r2 + r2h), (V, d2 - R)])
diamond(V, d2, ["Inside geofenced", "zone?"], V + 46, d2 - 14)
path([(V - R, d2), (590, d2), (590, cam_bottom)], "[no]", (660, d2 - 12))
r3h = max(bh("Mark drone position as detected"), bh("Map position onto pilot region (scaled transformation)")) / 2
r3 = d2 + R + GAP + r3h
path([(V, d2 + R), (V, r3 - r3h)], "[yes]", (V + 14, d2 + R + 40))
hm = box(V, r3, "Mark drone position as detected", "blue")
hp = box(F, r3, "Map position onto pilot region (scaled transformation)", "orange")
path([(V + BW / 2, r3), (F - BW / 2, r3)])

# Wi-Fi branch
dw = r1 + hw + GAP + R
path([(SW, r1 + hw), (SW, dw - R)])
diamond(SW, dw, ["Drone's Wi-Fi", "signal present?"], SW + 46, dw - 14)
JOIN = r3 + hp + 90
merge = JOIN - 150
path([(SW, dw + R), (SW, merge - R)], "[confirmed]", (SW + 14, (dw + merge) / 2))
path([(SW - R, dw), (52, dw), (52, merge), (SW - R, merge)], "[not confirmed]", (44, (dw + merge) / 2 + 110), rotate=True)
diamond(SW, merge)
path([(SW, merge + R), (SW, JOIN - 8)])
add(f'<text x="{SW+16}" y="{merge+R+52}" font-family="{FONT}" font-size="27" font-style="italic" fill="{GREY}">Wi-Fi status</text>')

bar(JOIN, 60, F + BW / 2 + 20)
path([(F, r3 + hp), (F, JOIN - 8)])

r4h = bh("Fuse camera + Wi-Fi and compute threat score") / 2
r4 = JOIN + 8 + 50 + r4h
path([(F, JOIN + 8), (F, r4 - r4h)])
box(F, r4, "Fuse camera + Wi-Fi and compute threat score", "orange")
r5h = bh("Propagate risk and line of sight on the grid") / 2
r5 = r4 + r4h + GAP + r5h
path([(F, r4 + r4h), (F, r5 - r5h)])
box(F, r5, "Propagate risk and line of sight on the grid", "green")
d3 = r5 + r5h + GAP + R
path([(F, r5 + r5h), (F, d3 - R)])
diamond(F, d3, ["Above alert", "level?"], F - 46, d3 - 14, anchor="end")
hs = box(O, d3, "Update track symbol on the map", "red")
path([(F + R, d3), (O - BW / 2, d3)], "[no]", (F + 56, d3 - 12))
ff = d3 + hs + 70
path([(O, d3 + hs), (O, ff - 22)])
add(f'<circle cx="{O}" cy="{ff}" r="22" fill="#ffffff" stroke="{INK}" stroke-width="2.8"/>')
add(f'<path d="M{O-15},{ff-15} L{O+15},{ff+15} M{O-15},{ff+15} L{O+15},{ff-15}" stroke="{INK}" stroke-width="2.8"/>')

r6h = max(bh("Plan safe route for response team (A*)"), bh("Retrieve doctrine passages (RAG)")) / 2
r6 = max(d3 + R + GAP + r6h, ff + 22 + 20 + r6h)
hf6 = bh("Plan safe route for response team (A*)") / 2
path([(F, d3 + R), (F, r6 - hf6)], "[yes]", (F + 14, d3 + R + 40))
hf6 = box(F, r6, "Plan safe route for response team (A*)", "green")
hk6 = box(K, r6, "Retrieve doctrine passages (RAG)", "purple")
path([(F + BW / 2, r6), (K - BW / 2, r6)])
r7h = max(bh("Generate cited recommendation (LLM)"), bh("Show alert, MIL-STD-2525 symbol and recommendation")) / 2
r7 = r6 + r6h + GAP + r7h
hk7 = bh("Generate cited recommendation (LLM)") / 2
path([(K, r6 + hk6), (K, r7 - hk7)])
box(K, r7, "Generate cited recommendation (LLM)", "purple")
ho7 = box(O, r7, "Show alert, MIL-STD-2525 symbol and recommendation", "red")
path([(K + BW / 2, r7), (O - BW / 2, r7)])
r8h = bh("Operator reviews the recommendation") / 2
r8 = r7 + r7h + GAP + r8h
path([(O, r7 + ho7), (O, r8 - r8h)])
box(O, r8, "Operator reviews the recommendation", "orange")
d4 = r8 + r8h + GAP + R
path([(O, r8 + r8h), (O, d4 - R)])
diamond(O, d4, ["Accept?"], O + 46, d4 - 14)
r9h = max(bh("Record operator override"), bh("Log decision and response")) / 2
r9 = d4 + R + GAP + r9h
path([(O - R, d4), (K, d4), (K, r9 - r9h)], "[no]", (O - 120, d4 - 12))
path([(O, d4 + R), (O, r9 - r9h)], "[yes]", (O + 14, d4 + R + 40))
box(K, r9, "Record operator override", "orange")
box(O, r9, "Log decision and response", "orange")
path([(K + BW / 2, r9), (O - BW / 2, r9)])
end = r9 + r9h + 75
path([(O, r9 + r9h), (O, end - 25)])
add(f'<circle cx="{O}" cy="{end}" r="25" fill="#ffffff" stroke="{INK}" stroke-width="3"/>')
add(f'<circle cx="{O}" cy="{end}" r="15" fill="{INK}"/>')

# note (Sensors lane, bottom)
NF = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Regular.otf", 26)
note = wrap("Detection runs on every frame (~20 fps); route, doctrine retrieval and LLM run only "
            "when the alert level is crossed.", 600, NF) + \
       wrap("ESC 491 scope: one mock drone, daytime, one camera, one ESP32 receiver.", 600, NF)
nx, nw = 50, 630
nh = 30 + 34 * len(note)
ny = end + 25 - nh
add(f'<path d="M{nx},{ny} L{nx+nw-26},{ny} L{nx+nw},{ny+26} L{nx+nw},{ny+nh} L{nx},{ny+nh} z" fill="#f3f5f8" stroke="{GREY}" stroke-width="1.8"/>')
for i, t in enumerate(note):
    add(f'<text x="{nx+20}" y="{ny+42+i*34}" font-family="{FONT}" font-size="26" fill="#3b414c">{t}</text>')

H = int(end + 25 + 45)
TOP, BOT = 20, H - 20
lane_svg = [f'<rect x="20" y="{TOP}" width="{W-40}" height="{BOT-TOP}" fill="#fcfcfd" stroke="#d5d9e0" stroke-width="2"/>',
            f'<rect x="20" y="{TOP}" width="{W-40}" height="100" fill="#f3f5f8" stroke="#d5d9e0" stroke-width="2"/>']
for x0, x1, title, sub in lanes:
    cx = (x0 + x1) / 2
    if x0 > 20:
        lane_svg.append(f'<line x1="{x0}" y1="{TOP}" x2="{x0}" y2="{BOT}" stroke="#d5d9e0" stroke-width="2"/>')
    lane_svg.append(f'<text x="{cx}" y="68" text-anchor="middle" font-family="{FONT}" font-size="33" font-weight="600" fill="{INK}">{title}</text>')
    lane_svg.append(f'<text x="{cx}" y="104" text-anchor="middle" font-family="{MONO}" font-size="22" fill="{GREY}">{sub}</text>')

head = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<defs><marker id="a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="8" markerHeight="8" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
open(sys.argv[1], "w").write("\n".join(head + lane_svg + out + ["</svg>"]))
print(W, H)
