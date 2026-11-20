#!/usr/bin/env python3
"""News image: Friday 20 November 2026.

Draws one editorial infographic summing up the day's world news with Pillow
only, no network, fully deterministic: fixed layout, fixed seed, no clocks.

Stories (all verified against Reuters / AP / CNN / BBC reporting of the day):
  - Trump, Xi and Putin hold the first three-way summit in Shenzhen and sign
    a four-point "peace declaration" (UN reform, fuel supply, court immunity,
    nuclear-risk dialogue). The text does not mention Ukraine.
  - Russia launches a massive overnight missile and drone attack on Ukraine:
    110+ missiles, about 400 drones, 8 killed, 28+ injured, three Kyiv
    bridges damaged; Poland scrambles jets and checks possible debris.
  - The International Court of Justice rules Myanmar committed genocide
    against the Rohingya (9-6) - the first time a state is held responsible.
  - Anthropic's Nasdaq debut: priced $83, opened $111.50, closed $97.17
    (+17%), briefly valued near $2 trillion - the biggest IPO in history.
  - Markets slide: S&P 500 -2.0%, Nasdaq -2.3%, Nikkei -4.8%, SoftBank -14%.
  - A Houthi missile damages Riyadh's PIF Tower, the city's tallest
    skyscraper: windows blown out across 7-8 floors, no injuries.
  - GTA 6 launch day: an estimated $2.36bn from about 24.6m copies
    (Sensor Tower estimate; Take-Two has not confirmed figures).
  - Young people strike across 25+ European countries over living costs
    and militarisation; Italy holds a general strike.
  - Also: the US and Venezuela sign a deal restoring military ties.

Output: /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png), 1024x1024 PNG.
"""

import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

# --- palette: warm paper, dark ink, signal colours -------------------------
PAPER = (247, 243, 236)
PAPER2 = (255, 255, 255)
INK = (22, 19, 14)
INK_SOFT = (74, 68, 58)
GREY = (140, 132, 120)
LINE = (201, 192, 176)
RED = (178, 34, 24)
RED_DARK = (132, 22, 14)
NAVY = (24, 38, 66)
NAVY_DARK = (14, 22, 40)
GOLD = (176, 132, 42)
GOLD_SOFT = (232, 204, 130)
TEAL = (14, 96, 96)
BLUE = (28, 84, 160)
SKY = (214, 230, 244)
NIGHT = (16, 24, 48)
ORANGE = (214, 110, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = "DejaVuSerif-Bold.ttf"
F_SANS = "DejaVuSans.ttf"
F_SANS_B = "DejaVuSans-Bold.ttf"

random.seed(20261120)


# --- text helpers ----------------------------------------------------------
def wrap(text, fnt, max_w):
    """Greedy word wrap by pixel width. Returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading=None, align="left", max_w=None):
    """Draw a list of already-wrapped lines. Returns the y after the block."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in lines:
        w = fnt.getlength(line)
        lx = x
        if align == "center" and max_w is not None:
            lx = x + (max_w - w) / 2
        elif align == "right" and max_w is not None:
            lx = x + max_w - w
        draw.text((lx, y), line, font=fnt, fill=fill)
        y += leading
    return y


def para(draw, x, y, text, fnt, fill, max_w, leading=None):
    return text_block(draw, x, y, wrap(text, fnt, max_w), fnt, fill, leading, "left", max_w)


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text, color=RED, size=17):
    f = font(F_SANS_B, size)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return f


def star_points(cx, cy, r_out, r_in, points=5, rot=-90):
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180.0 / points)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def rounded_card(draw, box, fill=PAPER2, outline=LINE, width=1, radius=10):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def flag_usa(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=(150, 150, 150))
    stripe = h / 13.0
    for i in range(13):
        if i % 2 == 0:
            draw.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe], fill=RED)
    draw.rectangle([x, y, x + w * 0.42, y + h * 7 / 13], fill=NAVY)
    for r in range(5):
        for c in range(6):
            sx = x + w * 0.04 + c * w * 0.068
            sy = y + h * 0.05 + r * h * 0.115
            draw.ellipse([sx, sy, sx + 2.5, sy + 2.5], fill=(255, 255, 255))


def flag_chn(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(222, 41, 16), outline=(150, 150, 150))
    pts = star_points(x + w * 0.18, y + h * 0.28, h * 0.16, h * 0.065)
    draw.polygon(pts, fill=(255, 222, 0))
    for sx, sy in [(0.42, 0.14), (0.50, 0.28), (0.50, 0.48), (0.42, 0.62)]:
        pts = star_points(x + w * sx, y + h * sy, h * 0.055, h * 0.022)
        draw.polygon(pts, fill=(255, 222, 0))


def flag_rus(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=(150, 150, 150))
    draw.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    draw.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 0))


# --- masthead --------------------------------------------------------------
def draw_masthead(draw):
    draw.rectangle([0, 0, W, 112], fill=INK)
    f_name = font(F_SERIF, 36)
    draw.text((28, 22), "THE WORLD TODAY", font=f_name, fill=(255, 255, 255))
    f_sub = font(F_SANS, 19)
    draw.text((30, 70), "The day's world news, in one page", font=f_sub, fill=(200, 192, 176))
    f_date = font(F_SANS_B, 26)
    d = "FRIDAY 20 NOVEMBER 2026"
    dw = f_date.getlength(d)
    draw.text((W - 28 - dw, 24), d, font=f_date, fill=GOLD_SOFT)
    f_tag = font(F_SANS_B, 16)
    t = "SUMMED UP · VERIFIED"
    tw = f_tag.getlength(t)
    draw.text((W - 28 - tw, 64), t, font=f_tag, fill=(200, 192, 176))
    draw.rectangle([0, 112, W, 118], fill=RED)


# --- hero: Shenzhen summit (left) ------------------------------------------
def draw_summit(draw, x, y, w, h):
    rounded_card(draw, [x, y, x + w, y + h], fill=PAPER2, outline=LINE, radius=12)
    kicker(draw, x + 22, y + 16, "Shenzhen · China — the lead story", RED, 16)
    # three flags in a row
    fw, fh = 84, 52
    fx = x + 22
    fy = y + 44
    flag_usa(draw, fx, fy, fw, fh)
    flag_chn(draw, fx + fw + 12, fy, fw, fh)
    flag_rus(draw, fx + 2 * (fw + 12), fy, fw, fh)
    f_vs = font(F_SANS_B, 15)
    draw.text((fx + fw + 2, fy + fh + 4), "USA", font=f_vs, fill=INK_SOFT)
    draw.text((fx + 2 * fw + 14, fy + fh + 4), "CHINA", font=f_vs, fill=INK_SOFT)
    draw.text((fx + 3 * fw + 26, fy + fh + 4), "RUSSIA", font=f_vs, fill=INK_SOFT)
    # headline
    f_h = font(F_SANS_B, 30)
    yy = para(draw, x + 22, y + 126, "Three powers sign a 'peace declaration'", f_h, INK, w - 44, 37)
    f_d = font(F_SANS, 18)
    yy = para(
        draw, x + 22, yy + 6,
        "Trump, Xi and Putin meet in Shenzhen — the first three-way "
        "summit. Four points: UN reform, fuel supply, court immunity and "
        "nuclear-risk talks. No mention of Ukraine.",
        f_d, INK_SOFT, w - 44, 23,
    )
    # bottom strip: the four points, one wrapped line
    yy += 8
    rule(draw, x + 22, yy, x + w - 22, 1, LINE)
    yy += 8
    f_p = font(F_SANS_B, 16)
    draw.text((x + 22, yy), "THE FOUR POINTS", font=f_p, fill=RED)
    f_q = font(F_SANS, 14)
    para(draw, x + 22, yy + 22,
         "UN reform · Fuel supply · Court immunity · Nuclear-risk talks",
         f_q, INK, w - 44, 20)


# --- hero: Ukraine overnight attack (right) --------------------------------
def draw_ukraine(draw, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=NIGHT)
    # sky banner across the top: missile trails over a city silhouette
    banner_h = 118
    for i, (sx, sy, ex, ey) in enumerate([
        (30, 100, 250, 22), (120, 108, 340, 28), (210, 112, 430, 44),
    ]):
        col = (255, 176, 66) if i % 2 == 0 else (255, 110, 70)
        mx, my = (sx + ex) / 2, min(sy, ey) - 34
        steps = 24
        pts = []
        for s in range(steps + 1):
            t = s / steps
            px = (1 - t) * (1 - t) * sx + 2 * (1 - t) * t * mx + t * t * ex
            py = (1 - t) * (1 - t) * sy + 2 * (1 - t) * t * my + t * t * ey
            pts.append((x + px, y + py))
        draw.line(pts, fill=col, width=3)
        draw.ellipse([x + ex - 5, y + ey - 5, x + ex + 5, y + ey + 5], fill=(255, 240, 200))
    # city silhouette along the banner's bottom edge
    for bx, bw, bh in [(16, 46, 30), (76, 34, 42), (126, 52, 26), (330, 40, 36), (386, 30, 28)]:
        draw.rectangle([x + bx, y + banner_h - bh, x + bx + bw, y + banner_h], fill=(24, 34, 60))
        for wy in range(5, bh - 5, 11):
            draw.rectangle([x + bx + 8, y + banner_h - bh + wy, x + bx + 13, y + banner_h - bh + wy + 4],
                           fill=(255, 200, 90))
    # kicker on a solid pill so the missile trails pass behind it
    draw.rounded_rectangle([x + 14, y + 10, x + 303, y + 38], radius=8, fill=NAVY)
    kicker(draw, x + 22, y + 16, "Kyiv · Ukraine — overnight", (255, 176, 66), 16)
    # headline + deck on clean navy below the banner
    ty = y + banner_h + 14
    f_h = font(F_SANS_B, 30)
    yy = para(draw, x + 22, ty, "Russia's biggest strike in months hits Kyiv", f_h,
              (255, 255, 255), w - 44, 37)
    f_d = font(F_SANS, 18)
    yy = para(
        draw, x + 22, yy + 6,
        "110+ missiles and about 400 drones overnight. 8 killed, 28 hurt. "
        "Three bridges over the Dnipro damaged. Poland scrambles jets.",
        f_d, (216, 222, 236), w - 44, 24,
    )
    # casualty chips
    yy += 12
    chips = [("110+", "MISSILES"), ("~400", "DRONES"), ("3", "BRIDGES HIT")]
    cx = x + 22
    f_n = font(F_SANS_B, 26)
    f_c = font(F_SANS_B, 13)
    for num, lab in chips:
        cw = 118
        draw.rounded_rectangle([cx, yy, cx + cw, yy + 54], radius=8,
                               outline=(255, 176, 66), width=2)
        draw.text((cx + 12, yy + 4), num, font=f_n, fill=(255, 255, 255))
        draw.text((cx + 12, yy + 32), lab, font=f_c, fill=(255, 176, 66))
        cx += cw + 12


# --- grid tiles ------------------------------------------------------------
def icon_scales(draw, x, y, s, color=GOLD):
    draw.line([(x + s / 2, y + 2), (x + s / 2, y + s - 8)], fill=color, width=3)
    draw.line([(x + 4, y + 8), (x + s - 4, y + 8)], fill=color, width=3)
    for cx in (x + 6, x + s - 6):
        draw.line([(cx, y + 8), (cx, y + 16)], fill=color, width=2)
        draw.polygon([(cx - 8, y + 16), (cx + 8, y + 16), (cx, y + 26)], outline=color, width=2)
    draw.line([(x + s / 2 - 8, y + s - 4), (x + s / 2 + 8, y + s - 4)], fill=color, width=3)
    draw.ellipse([x + s / 2 - 3, y, x + s / 2 + 3, y + 6], fill=color)


def icon_chart_up(draw, x, y, s, color=(16, 130, 80)):
    draw.line([(x + 2, y + s - 4), (x + s - 2, y + s - 4)], fill=INK_SOFT, width=2)
    pts = [(x + 3, y + s - 10), (x + s * 0.35, y + s - 18), (x + s * 0.55, y + s - 12),
           (x + s - 6, y + 4)]
    draw.line(pts, fill=color, width=3)
    ex, ey = pts[-1]
    draw.polygon([(ex - 8, ey + 2), (ex + 2, ey - 4), (ex + 2, ey + 8)], fill=color)


def icon_chart_down(draw, x, y, s, color=RED):
    draw.line([(x + 2, y + s - 4), (x + s - 2, y + s - 4)], fill=INK_SOFT, width=2)
    pts = [(x + 3, y + 6), (x + s * 0.35, y + 14), (x + s * 0.55, y + 8),
           (x + s - 6, y + s - 10)]
    draw.line(pts, fill=color, width=3)
    ex, ey = pts[-1]
    draw.polygon([(ex - 8, ey - 2), (ex + 2, ey - 8), (ex + 2, ey + 4)], fill=color)


def icon_tower(draw, x, y, s, color=NAVY):
    draw.rectangle([x + s * 0.3, y + 2, x + s * 0.7, y + s - 2], fill=color)
    for wy in range(6, int(s) - 4, 7):
        draw.line([(x + s * 0.34, y + wy), (x + s * 0.66, y + wy)], fill=(255, 255, 255), width=1)
    crack = [(x + s * 0.7, y + 8), (x + s * 0.58, y + 13), (x + s * 0.72, y + 18),
             (x + s * 0.6, y + 23), (x + s * 0.7, y + 28)]
    draw.line(crack, fill=RED, width=2)


def icon_vi(draw, x, y, s, color=GOLD):
    draw.rounded_rectangle([x, y, x + s, y + s], radius=6, fill=NAVY)
    f = font(F_SERIF, int(s * 0.52))
    t = "VI"
    tw = f.getlength(t)
    draw.text((x + (s - tw) / 2, y + s * 0.2), t, font=f, fill=color)


def icon_megaphone(draw, x, y, s, color=RED):
    draw.polygon([(x + 2, y + s * 0.35), (x + s * 0.55, y + s * 0.15),
                  (x + s * 0.55, y + s * 0.6), (x + 2, y + s * 0.55)], fill=color)
    draw.rectangle([x + s * 0.55, y + s * 0.2, x + s * 0.68, y + s * 0.55], fill=color)
    draw.line([(x + s * 0.72, y + s * 0.3), (x + s - 2, y + s * 0.15)], fill=color, width=2)
    draw.line([(x + s * 0.72, y + s * 0.38), (x + s - 2, y + s * 0.38)], fill=color, width=2)
    draw.line([(x + s * 0.72, y + s * 0.46), (x + s - 2, y + s * 0.6)], fill=color, width=2)
    draw.rectangle([x + s * 0.3, y + s * 0.55, x + s * 0.45, y + s * 0.85], fill=color)


def tile(draw, x, y, w, h, kicker_text, kicker_color, headline, deck, icon):
    rounded_card(draw, [x, y, x + w, y + h], fill=PAPER2, outline=LINE, radius=10)
    draw.rectangle([x, y + 10, x + 5, y + h - 10], fill=kicker_color)
    pad = 16
    kicker(draw, x + pad, y + 12, kicker_text, kicker_color, 14)
    icon(draw, x + w - 48, y + 10, 34)
    f_h = font(F_SANS_B, 21)
    hw = w - pad * 2 - 42
    lines = wrap(headline, f_h, hw)
    yy = text_block(draw, x + pad, y + 36, lines, f_h, INK, 26)
    f_d = font(F_SANS, 15)
    dw = w - pad * 2
    dlines = wrap(deck, f_d, dw)
    room = y + h - 12 - (yy + 4)
    max_lines = max(1, room // 20)
    text_block(draw, x + pad, yy + 4, dlines[:max_lines], f_d, INK_SOFT, 20)


# --- ticker + footer --------------------------------------------------------
def draw_ticker(draw, y, h):
    draw.rectangle([0, y, W, y + h], fill=NAVY_DARK)
    f_a = font(F_SANS_B, 16)
    draw.text((28, y + 11), "ALSO TODAY", font=f_a, fill=GOLD_SOFT)
    f_t = font(F_SANS, 17)
    items = ("U.S. and Venezuela sign a deal to restore military ties   ·   "
             "Italy joins the Europe-wide general strike   ·   "
             "Poland checks two possible airspace violations")
    lines = wrap(items, f_t, W - 28 - 170)
    yy = y + 8
    for line in lines[:2]:
        draw.text((190, yy), line, font=f_t, fill=(226, 230, 238))
        yy += 22


def draw_footer(draw, y):
    f = font(F_SANS, 14)
    t = "Sources: Reuters, AP, CNN, BBC, The Times — figures as reported on Friday 20 November 2026"
    tw = f.getlength(t)
    draw.text(((W - tw) / 2, y), t, font=f, fill=GREY)


# --- assemble ---------------------------------------------------------------
def build():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    draw_summit(draw, 24, 134, 478, 360)
    draw_ukraine(draw, 522, 134, 478, 360)
    # section label
    f_sec = font(F_SANS_B, 17)
    draw.text((28, 508), "THE DAY, IN BRIEF", font=f_sec, fill=INK)
    rule(draw, 240, 518, W - 28, 1, LINE)
    tiles = [
        ("The Hague · Justice", GOLD, "World court: Myanmar guilty of genocide",
         "First time a state is held responsible · 9–6 vote · Reparations ordered",
         icon_scales),
        ("Wall Street · Tech", (16, 130, 80), "Anthropic's $2 trillion debut",
         "Priced $83, opened $111.50, closed $97.17 (+17%) · Biggest IPO ever",
         icon_chart_up),
        ("Markets · Sell-off", RED, "AI sell-off spreads worldwide",
         "S&P 500 −2.0% · Nasdaq −2.3% · Nikkei −4.8% · SoftBank −14%",
         icon_chart_down),
        ("Riyadh · Middle East", NAVY, "Missile hits Riyadh's tallest tower",
         "Houthi strike damages the 80-storey PIF Tower · No injuries",
         icon_tower),
        ("Culture · Gaming", GOLD, "GTA 6: $2.36bn in a day",
         "About 24.6m copies on launch day — biggest entertainment launch*",
         icon_vi),
        ("Europe · Protest", RED, "Europe's youth walk out",
         "25+ countries strike over living costs · “Fight for our future”",
         icon_megaphone),
    ]
    gx, gy = [24, 352, 680], [530, 712]
    tw, th = 320, 170
    for i, (kick, col, head, deck, icon) in enumerate(tiles):
        tile(draw, gx[i % 3], gy[i // 3], tw, th, kick, col, head, deck, icon)
    draw_ticker(draw, 896, 64)
    draw_footer(draw, 972)
    return img


def main():
    img = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG")
    print(f"wrote {OUT}: {img.size[0]}x{img.size[1]} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
