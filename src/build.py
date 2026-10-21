import os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from menus import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
PHONE = "(608) 480-4001"; TEL = "tel:6084804001"
EMAIL = "WSTQuestions@gmail.com"; PE_EMAIL = "WSTPrivateEvents@gmail.com"
ADDRESS = "324 South Water Street, Stoughton, WI"
MAPS = "https://www.google.com/maps/search/?api=1&query=Water+Street+Tavern+324+S+Water+St+Stoughton+WI"
RESY = "https://resy.com/cities/stoughton-wi-wi/venues/water-street-tavern"
FB = "https://www.facebook.com/100089725462678/"; IG = "https://www.instagram.com/TheWaterStreetTavern"
PE_MAILTO = ("mailto:WSTPrivateEvents@gmail.com?subject=Water%20Street%20Tavern%20Private%20Event&body=Please%20provide%20the%20following%20information.%0A%0AName%3A%0APhone%20number%3A%0ARequested%20date%3A%0AAnticipated%20number%20of%20guests%3A%0AType%20of%20event%3A%0A%0AWe'll%20get%20back%20to%20you%20within%2048%20hours.%0A%0AThanks%20for%20thinking%20of%20us%2C%20and%20we%20look%20forward%20to%20hosting%20you!")

KITCHEN = [("Dinner","Wednesday – Saturday","4:00 – 9:00 pm"),("Brunch","Saturday & Sunday","9:00 am – 2:00 pm")]
BAR = [("Wednesday – Friday","4:00 – 9:30 pm*"),("Saturday","9:00 am – 9:30 pm*"),("Sunday","9:00 am – 2:00 pm*")]
BAR_NOTE = "*Earliest time the bar will close, based on customer activity. If you're here, we're here!"

MENU_LINKS = [("dinner.html","Dinner"),("drinks.html","Drinks"),("brunch.html","Brunch"),("date-night.html","Date Night (Wednesday)"),("nightly-specials.html","Nightly Specials")]

FB_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8.2h2.8l.4-3.2h-3.2V8.5c0-.9.3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V22h3.4z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.9 8.2c-.1-1.6-.4-3-1.6-4.2S17.7 2.4 16.1 2.4C14.4 2.3 9.6 2.3 7.9 2.4 6.3 2.5 4.9 2.8 3.7 4S2.1 6.6 2 8.2c-.1 1.7-.1 6.5 0 8.2.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.7.1 6.5.1 8.2 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.2-1.7.2-6.5.1-8.2zm-2.2 10.1a3.3 3.3 0 0 1-1.9 1.9c-1.3.5-4.4.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 0 1-1.9-1.9c-.5-1.3-.4-4.4-.4-5.8s-.1-4.5.4-5.8a3.3 3.3 0 0 1 1.9-1.9c1.3-.5 4.4-.4 5.8-.4s4.5-.1 5.8.4a3.3 3.3 0 0 1 1.9 1.9c.5 1.3.4 4.4.4 5.8s.1 4.5-.4 5.8z"/></svg>'

def head(title, desc):
    t = "The Water Street Tavern | Stoughton, WI" if title is None else f"{title} | The Water Street Tavern, Stoughton WI"
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(t)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(t)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="img/dining-room.jpg">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(active):
    def a(href, label):
        cur = ' aria-current="page"' if href == active else ''
        return f'<a href="{href}"{cur}>{label}</a>'
    menu_active = active in [h for h,_ in MENU_LINKS]
    dd = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{l}</a>' for h,l in MENU_LINKS)
    return f'''<div class="announce"><span class="long">We're happy to announce we are now hosting private events!</span><span class="short">Now hosting private events</span><a href="private-events.html">Plan your event</a></div>
<header class="site-header">
 <div class="hdr">
  <a class="brand" href="index.html" aria-label="The Water Street Tavern home"><img src="img/logo-dark.png" alt="Food &amp; Drinks · Water Street Tavern · Stoughton, WI" width="700" height="338"></a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
  <nav class="nav" id="nav" aria-label="Main">
   <button class="nav-close" aria-label="Close menu">&times;</button>
   {a("index.html","Home")}
   <div class="dd"><button aria-expanded="false"{' style="color:var(--brass)"' if menu_active else ''}>Menus</button><div class="dd-menu">{dd}</div></div>
   {a("private-events.html","Private Events")}
   {a("art-o-mat.html","Art-o-mat")}
   {a("gift-certificates.html","Gift Certificates")}
   {a("about.html","About")}
   {a("reservations.html","Reservations")}
   <a class="btn" href="{RESY}" target="_blank" rel="noopener">Book a Table</a>
  </nav>
 </div>
</header>
<div class="scrim"></div>
<main id="main">
'''

def footer():
    k = "".join(f'<li>{E(l)} · {E(d)}<br><span style="color:var(--ivory)">{E(t)}</span></li>' for l,d,t in KITCHEN)
    return f'''</main>
<footer class="site-footer">
 <div class="wrap">
  <div class="fgrid">
   <div>
    <img class="flogo" src="img/logo-light.png" alt="Water Street Tavern" width="700" height="338">
    <p>A retro supper club on the Yahara River in historic downtown Stoughton.</p>
    <div class="social"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a></div>
   </div>
   <div><h4>Visit</h4><ul><li><a href="{MAPS}" target="_blank" rel="noopener">324 South Water Street<br>Stoughton, WI</a></li><li style="margin-top:10px"><a href="{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
   <div><h4>Kitchen Hours</h4><ul>{k}</ul><p class="small" style="margin-top:12px">Walk-ins always welcome.</p></div>
   <div><h4>Explore</h4><ul><li><a href="dinner.html">Dinner</a></li><li><a href="drinks.html">Drinks</a></li><li><a href="brunch.html">Brunch</a></li><li><a href="nightly-specials.html">Nightly Specials</a></li><li><a href="private-events.html">Private Events</a></li><li><a href="reservations.html">Reservations</a></li><li><a href="art-o-mat.html">Art-o-mat</a></li><li><a href="gift-certificates.html">Gift Certificates</a></li><li><a href="about.html">About</a></li></ul></div>
  </div>
  <div class="fbottom"><span>&copy; 2026 The Water Street Tavern · Stoughton, Wisconsin</span><span>Private events: <a href="mailto:{PE_EMAIL}">{PE_EMAIL}</a></span></div>
 </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
'''

def band(img, inner, cls="", pos="center"):
    return f'''<section class="band {cls}">
 <div class="band__bg" style="background-image:url('img/{img}.jpg');background-position:{pos}" data-sm="img/{img}-sm.jpg" role="img" aria-hidden="true"></div>
 <div class="band__veil"></div>
 <div class="band__content">{inner}</div>
</section>
'''

def tags(ts): return "".join(f'<span class="diet" title="{"Gluten free or can be modified" if t=="GF" else "Vegetarian or can be modified"}">{t}</span>' for t in ts)

def item(name, price, desc, ts, opt):
    pr = f'<span class="dots"></span><span class="price">{E(price)}</span>' if price else ''
    d = f'<p class="desc">{E(desc)}</p>' if desc else ''
    o = f'<p class="opt">{E(opt)}</p>' if opt else ''
    return f'<div class="item"><div class="row"><span class="name">{E(name)}{tags(ts)}</span>{pr}</div>{d}{o}</div>'

def groups(data):
    out = []
    for title, note, items in data:
        n = f'<p class="gnote">{E(note)}</p>' if note else ''
        out.append(f'<div class="mgroup"><div class="ghead"><h2>{E(title)}</h2></div>{n}{"".join(item(*i) for i in items)}</div>')
    return "".join(out)

def menu_nav(active):
    return '<nav class="menu-nav" aria-label="Menus">' + "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{l}</a>' for h,l in MENU_LINKS) + '</nav>'

LEGAL = '''<div class="legal"><p>* Be advised that consuming raw or undercooked meat, eggs or poultry may increase the risk of foodborne illness.</p>
<p><strong>GF</strong> indicates a gluten free dish, or a dish that can be modified to gluten free upon request. <strong>V</strong> indicates a vegetarian dish, or a dish that can be modified to vegetarian upon request. Please check with your server.</p></div>'''

def takeout(): return f'<p class="center muted" style="margin-top:34px">Call <a href="{TEL}">{PHONE}</a> to place a take-out order.</p>'

def hours_cards(extra=True):
    kr = "".join(f'<div class="hrow"><span>{E(l)}<br><span class="small">{E(d)}</span></span><span>{E(t)}</span></div>' for l,d,t in KITCHEN)
    br = "".join(f'<div class="hrow"><span>{E(d)}</span><span>{E(t)}</span></div>' for d,t in BAR)
    third = f'''<div class="card reveal"><h3>Dine In &amp; Take Out</h3>
      <div class="hrow"><span>Walk-ins</span><span>Always welcome</span></div>
      <div class="hrow"><span>Reservations</span><span><a href="{RESY}" target="_blank" rel="noopener">Book on Resy</a></span></div>
      <div class="hrow"><span>Take out</span><span><a href="{TEL}">{PHONE}</a></span></div>
      <p class="hnote muted">Walk-ins always welcomed and encouraged! Take-out orders can be placed with a phone call.</p></div>'''
    return f'''<div class="hours">
     <div class="card reveal"><h3>Kitchen Hours</h3>{kr}</div>
     <div class="card reveal"><h3>Bar Hours</h3>{br}<p class="hnote muted">{E(BAR_NOTE)}</p></div>
     {third}
    </div>'''

def page(fn, title, desc, active, body):
    with open(os.path.join(ROOT, fn), "w") as f:
        f.write(head(title, desc) + header(active) + body + footer())

# ---------------- HOME ----------------
week = [
 ("Wednesday","Date Night","A special couples menu, with an optional bottle of wine to share.","date-night.html","See the menu"),
 ("Thursday","The Kitchen Is Experimenting","Check out our Facebook Thursday afternoon to see what's up!",FB,"Follow on Facebook"),
 ("Friday","Friday Fish Fry","Bluegill, perch and walleye.","nightly-specials.html","Fish fry details"),
 ("Saturday","Prime Rib","14 oz of prime rib with mashed potatoes, brussel sprouts and a house salad.","nightly-specials.html","Saturday special"),
]
week_html = "".join(f'<div class="day reveal"><span class="dname">{d}</span><h3>{t}</h3><p>{p}</p><a class="more" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}>{m} &rarr;</a></div>' for d,t,p,h,m in week)

home = band("dining-room", f'''<span class="eyebrow">Food &amp; Drinks · Historic Downtown Stoughton</span>
<h1>Welcome to<br>The Water Street Tavern</h1><hr class="rule">
<p>Top-notch dining with a retro supper club vibe. Enjoy a memorable dinner with friends and family, or just a cocktail at the patio fireplace on the river.</p>
<div class="btns" style="justify-content:center;margin-top:30px"><a class="btn light" href="{RESY}" target="_blank" rel="noopener">Book a Table</a><a class="btn outline-light" href="dinner.html">View Menus</a></div>''', "tall")
home += f'''
<div class="wrap"><div class="info">
 <div><span class="k">Find Us</span><a href="{MAPS}" target="_blank" rel="noopener">324 South Water Street</a></div>
 <div><span class="k">Call</span><a href="{TEL}">{PHONE}</a></div>
 <div><span class="k">Dinner</span><span class="v">Wed – Sat · from 4:00 pm</span></div>
</div></div>

<section class="section" id="news">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">At the Tavern</span><h2>News &amp; Updates</h2><hr class="rule"></div>
  <article class="news-feature reveal">
   <div class="nf-img" style="background-image:url('img/patio-night-sm.jpg')" role="img" aria-label="The riverfront patio at night"></div>
   <div class="nf-body"><span class="tag">This Season</span>
    <h3 style="font-size:2rem">Fall is in the air, but the patio is still here for you!</h3>
    <p>We're getting a chill in the air, so we've enclosed the covered patio. It now provides a cozy, heated, four-season dining area that retains its great views of the river, with the same full service as the main dining room.</p>
    <p>The outdoor fire pits are still here for you, and a great space for the hearty to hang out and enjoy a cocktail or a hot beverage!</p>
   </div>
  </article>
  <article class="news-feature reveal" style="grid-template-columns:1fr">
   <div class="nf-body center" style="padding:44px 40px"><span class="tag">Now Booking</span>
    <h3 style="font-size:2rem">We're now hosting private events</h3>
    <p style="max-width:620px;margin:0 auto 22px">Holiday parties, special birthdays and other private celebrations, hosted in our riverfront space.</p>
    <a class="btn ghost" href="private-events.html">Learn More</a></div>
  </article>
  <div class="section-head reveal" style="margin:84px auto 36px"><span class="eyebrow">Check Out Our Dinner Specials</span><h2 style="font-size:2.3rem">This Week at the Tavern</h2></div>
  <div class="week">{week_html}</div>
 </div>
</section>
'''
home += band("table-candle", f'''<div class="glass reveal"><span class="eyebrow">Now Hosting Private Events</span>
<h2>Celebrate With Us</h2><hr class="rule">
<p>Looking for a place to hold your holiday party, special birthday, or other private event? Water Street Tavern would love to celebrate with you.</p>
<div class="btns" style="justify-content:center;margin-top:26px"><a class="btn light" href="private-events.html">Plan Your Event</a><a class="btn outline-light" href="mailto:{PE_EMAIL}">Email Us</a></div></div>''', "tall", "68% center")
home += f'''
<section class="section ivory">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Private Events</span><h2>How to Book Your Event</h2><hr class="rule"><p>Tell us a few details and our team will get back to you within 48 hours.</p></div>
  <div class="pe-grid">
   <div class="pe-card reveal"><span class="num">I.</span><h3>Choose Your Occasion</h3><p>A holiday party, a special birthday, or any other private event you'd like to celebrate.</p></div>
   <div class="pe-card reveal"><span class="num">II.</span><h3>Send Your Request</h3><p>Email <a href="mailto:{PE_EMAIL}">{PE_EMAIL}</a> with your name, phone number, requested date, anticipated number of guests and type of event.</p></div>
   <div class="pe-card reveal"><span class="num">III.</span><h3>We'll Be in Touch</h3><p>We'll get back to you within 48 hours. Thanks for thinking of us, and we look forward to hosting you!</p></div>
  </div>
  <p class="center" style="margin-top:46px"><a class="btn" href="{PE_MAILTO}">Schedule Your Event</a></p>
 </div>
</section>

<section class="section dark" id="hours">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Plan Your Visit</span><h2>Hours</h2><hr class="rule"></div>
  {hours_cards()}
 </div>
</section>
'''
home += band("bar", '''<div class="glass"><span class="eyebrow">From the Bar</span><h2>The House Old Fashioned</h2><hr class="rule"><p>Four Roses bourbon, Luxardo cherries &amp; bitters, always muddled, Wisconsin-style.</p><div class="btns" style="justify-content:center;margin-top:26px"><a class="btn outline-light" href="drinks.html">Drinks Menu</a></div></div>''')
home += f'''
<section class="section">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Our Menus</span><h2>Burgers, Comfort Food &amp; Elevated Entrées</h2><hr class="rule"></div>
  <div class="tiles">
   <a class="tile reveal" href="dinner.html"><span class="eyebrow">Wed – Sat</span><h3>Dinner</h3><p>Starters, steaks, entrées &amp; handhelds</p></a>
   <a class="tile reveal" href="drinks.html"><span class="eyebrow">Fall / Winter</span><h3>Drinks</h3><p>Cocktails, wine, beer &amp; mocktails</p></a>
   <a class="tile reveal" href="brunch.html"><span class="eyebrow">Sat &amp; Sun</span><h3>Brunch</h3><p>Benedicts, classics &amp; brunch cocktails</p></a>
   <a class="tile reveal" href="date-night.html"><span class="eyebrow">Wednesday</span><h3>Date Night</h3><p>Four courses for two</p></a>
  </div>
 </div>
</section>
'''
home += band("patio-night", f'''<div class="glass"><span class="eyebrow">On the Yahara River</span><h2>Come As You Are</h2><hr class="rule"><p>Whether you're joining us for a casual meal, a special celebration, or simply to unwind by the water.</p><div class="btns" style="justify-content:center;margin-top:26px"><a class="btn light" href="{RESY}" target="_blank" rel="noopener">Book a Table</a><a class="btn outline-light" href="about.html">Our Story</a></div></div>''', "tall")
home += f'''
<section class="section ivory">
 <div class="wrap split">
  <div class="reveal"><div class="ph" style="background-image:url('img/art-o-mat-sm.jpg')" role="img" aria-label="The Art-o-mat machine"></div></div>
  <div class="reveal">
   <span class="eyebrow">Only at the Tavern</span><h2>The Art-o-mat</h2><hr class="rule left">
   <p>A retired cigarette vending machine converted to vend art. Water Street Tavern is one of the few in the state of Wisconsin. Get your token for $5 and start your mini art collection!</p>
   <p><a class="btn ghost" href="art-o-mat.html">About the Art-o-mat</a></p>
   <div style="margin-top:56px;padding-top:40px;border-top:1px solid var(--line)"><span class="eyebrow">Give the Tavern</span><h3 style="font-size:2rem">Gift Certificates</h3><p>Available in any amount you wish. Just stop in to pick up a gift that is sure to be appreciated.</p><a href="gift-certificates.html">Learn more &rarr;</a></div>
  </div>
 </div>
</section>
'''
page("index.html", None, "Top-notch dining with a retro supper club vibe on the river in historic downtown Stoughton, WI. Dinner Wed–Sat, weekend brunch, cocktails by the patio fireplace, and now hosting private events.", "index.html", home)

# ---------------- PRIVATE EVENTS ----------------
pe = band("table-candle", f'''<span class="eyebrow">Now Hosting Private Events</span><h1>Water Street Tavern<br>Private Events</h1><hr class="rule">
<p>Looking for a place to hold your holiday party, special birthday, or other private event? Water Street Tavern would love to celebrate with you!</p>
<div class="btns" style="justify-content:center;margin-top:30px"><a class="btn light" href="{PE_MAILTO}">Schedule Your Event</a><a class="btn outline-light" href="{TEL}">Call {PHONE}</a></div>''', "tall", "68% center")
pe += f'''
<section class="section">
 <div class="narrow center">
  <span class="eyebrow reveal">Occasions</span><h2 class="reveal">Gather by the River</h2><hr class="rule">
  <p class="lede reveal">Our riverfront supper club in historic downtown Stoughton is a warm, relaxed setting for the moments worth celebrating, served with the same care we bring to every table.</p>
  <div class="occasions reveal"><span>Holiday Parties</span><span>Special Birthdays</span><span>Other Private Events</span></div>
 </div>
</section>

<section class="section ivory" style="padding-top:90px">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">The Setting</span><h2>Our Spaces</h2><hr class="rule"><p>The best fit for your gathering depends on your date and guest count. Tell us about your event and we'll help you plan it.</p></div>
  <div class="spaces">
   <div class="space reveal"><div class="sp-img" style="background-image:url('img/dining-room-sm.jpg')" role="img" aria-label="The dining room"></div>
    <div class="sp-body"><span class="eyebrow">Inside</span><h3 style="font-size:2rem">The Dining Room</h3><p>Our beautiful, riverfront space with a retro supper club feel, where we serve a mix of exceptional burgers, classic comfort food and elevated entrées.</p></div></div>
   <div class="space reveal"><div class="sp-img" style="background-image:url('img/patio-night-sm.jpg')" role="img" aria-label="The riverfront patio at night"></div>
    <div class="sp-body"><span class="eyebrow">Four-Season</span><h3 style="font-size:2rem">The Covered Patio</h3><p>Enclosed for the cooler months, the covered patio is a cozy, heated, four-season dining area that keeps its great views of the river, with the same full service as the main dining room. The outdoor fire pits are a great spot for a cocktail or a hot beverage.</p></div></div>
   <div class="space reveal"><div class="sp-img" style="background-image:url('img/bar-sm.jpg')" role="img" aria-label="The bar"></div>
    <div class="sp-body"><span class="eyebrow">Food &amp; Drink</span><h3 style="font-size:2rem">From Our Kitchen &amp; Bar</h3><p>Supper club classics, steaks, Friday fish fry, Wisconsin-style old fashioneds and a thoughtful wine list. Ask us about food and drink options for your event.</p><p><a href="dinner.html">Dinner</a> &nbsp;·&nbsp; <a href="drinks.html">Drinks</a> &nbsp;·&nbsp; <a href="brunch.html">Brunch</a></p></div></div>
  </div>
 </div>
</section>

<section class="section">
 <div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">How It Works</span><h2>Booking Your Event</h2><hr class="rule"></div>
  <div class="pe-grid">
   <div class="pe-card reveal"><span class="num">I.</span><h3>Reach Out</h3><p>Email <a href="mailto:{PE_EMAIL}">{PE_EMAIL}</a> or use the request form below.</p></div>
   <div class="pe-card reveal"><span class="num">II.</span><h3>Share the Details</h3><p>Your name, phone number, requested date, anticipated number of guests and type of event.</p></div>
   <div class="pe-card reveal"><span class="num">III.</span><h3>Hear Back in 48 Hours</h3><p>We'll get back to you within 48 hours. Thanks for thinking of us; we look forward to hosting you!</p></div>
  </div>
 </div>
</section>

<section class="section ivory" id="inquire">
 <div class="wrap">
  <div class="inquiry reveal">
   <div>
    <span class="eyebrow">Event Inquiry</span><h2>Schedule Your Event</h2><hr class="rule left">
    <p>Fill in the details below and we'll open a pre-written email to our private events team. Prefer to write your own? Email <a href="mailto:{PE_EMAIL}">{PE_EMAIL}</a>.</p>
    <ul class="checklist"><li>Name</li><li>Phone number</li><li>Requested date</li><li>Anticipated number of guests</li><li>Type of event</li></ul>
    <p class="small muted">Questions? Call <a href="{TEL}">{PHONE}</a> during business hours.</p>
   </div>
   <form class="pe-form" id="peForm" novalidate>
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Phone number<input name="phone" type="tel" autocomplete="tel"></label>
    <div class="two"><label>Requested date<input name="date" type="date"></label><label>Number of guests<input name="guests" type="number" min="1" inputmode="numeric"></label></div>
    <label>Type of event<select name="type"><option value="">Select…</option><option>Holiday party</option><option>Birthday</option><option>Other private event</option></select></label>
    <label>Anything else we should know?<textarea name="notes" rows="3"></textarea></label>
    <button class="btn" type="submit" style="width:100%">Compose Inquiry Email</button>
    <p class="small muted" style="margin-top:10px">This opens your email app. Nothing is sent until you press send.</p>
   </form>
  </div>
 </div>
</section>
'''
pe += band("patio-night", f'''<div class="glass"><span class="eyebrow">Just a Bigger Table?</span><h2>Large Party Reservations</h2><hr class="rule"><p>For reservations larger than groups of 9, please call the restaurant during business hours at {PHONE}, or email {EMAIL}.</p><div class="btns" style="justify-content:center;margin-top:26px"><a class="btn light" href="{TEL}">Call Us</a><a class="btn outline-light" href="reservations.html">Reservations</a></div></div>''')
pe += '''<script>
document.getElementById('peForm').addEventListener('submit',function(e){e.preventDefault();var f=e.target;var v=function(n){return (f[n].value||'').trim()};
var body="Please provide the following information.\\n\\nName: "+v('name')+"\\nPhone number: "+v('phone')+"\\nRequested date: "+v('date')+"\\nAnticipated number of guests: "+v('guests')+"\\nType of event: "+v('type')+(v('notes')?"\\n\\nNotes: "+v('notes'):"")+"\\n\\nWe'll get back to you within 48 hours.\\n\\nThanks for thinking of us, and we look forward to hosting you!";
location.href="mailto:WSTPrivateEvents@gmail.com?subject="+encodeURIComponent("Water Street Tavern Private Event")+"&body="+encodeURIComponent(body);});
</script>'''
page("private-events.html", "Private Events", "Host your holiday party, special birthday or private event at Water Street Tavern, a riverfront supper club in downtown Stoughton, WI. Email WSTPrivateEvents@gmail.com.", "private-events.html", pe)

# ---------------- MENU PAGES ----------------
def menu_page(fn, title, eyebrow, sub, img, pdf, content, desc, pos="center"):
    b = band(img, f'<span class="eyebrow">{eyebrow}</span><h1>{title}</h1><hr class="rule"><p>{sub}</p>', "short", pos)
    b += f'''<section class="section tight"><div class="wrap">{menu_nav(fn)}
<p class="center" style="margin:22px 0 64px"><a class="pdf-link" href="menus/{pdf}" target="_blank" rel="noopener">Download printable menu (PDF) &darr;</a></p>
{content}{takeout()}</div></section>'''
    page(fn, title, desc, fn, b)

specials = "".join(f'<div class="day"><span class="dname">{E(d)}</span><h3>{E(t)}</h3><p>{E(p)}</p></div>' for d,t,p in DINNER_SPECIALS)
menu_page("dinner.html","Dinner","Wednesday – Saturday · 4:00 – 9:00 pm","Exceptional burgers, classic comfort food and elevated entrées.","dining-room","dinner.pdf",
  f'<div class="menu">{groups(DINNER)}</div><div class="section-head" style="margin:30px auto 30px"><span class="eyebrow">Specials</span><h2 style="font-size:2.2rem">Through the Week</h2></div><div class="week">{specials}</div>{LEGAL}',
  "Dinner menu at Water Street Tavern, Stoughton WI: starters, soups and salads, steaks, entrées, burgers and handhelds.")

beer = f'''<div class="mgroup" style="column-span:all"><div class="ghead"><h2>Beer · Cider · Seltzer</h2></div>
<div class="split" style="gap:50px;align-items:start"><div><h3>On Tap</h3><ul class="plist">{"".join(f"<li>{E(x)}</li>" for x in BEER_TAP)}</ul></div>
<div><h3>Cans</h3><ul class="plist">{"".join(f"<li>{E(x)}</li>" for x in BEER_CANS)}</ul></div></div>
<h3 style="margin-top:36px">Soda, etc.</h3><ul class="plist" style="columns:3">{"".join(f"<li>{E(x)}</li>" for x in SODA)}</ul>
<p class="center" style="margin-top:36px;font-family:var(--serif);font-size:1.3rem;font-style:italic">“Art-o-mat tokens are only $5!”</p></div>'''
menu_page("drinks.html","Drinks","Fall / Winter 2026","Specialty cocktails, wine, beer and thoughtful mocktails.","bar","drinks.pdf",
  f'<div class="menu">{groups(DRINKS)}</div>{beer}',
  "Drinks menu at Water Street Tavern: Wisconsin-style old fashioneds, specialty and dessert cocktails, wine by the glass and bottle, beer and mocktails.")
menu_page("brunch.html","Brunch","Saturday &amp; Sunday · 9:00 am – 2:00 pm","Elevated yet approachable weekend brunch by the river.","patio-night","brunch.pdf",
  f'<div class="menu">{groups(BRUNCH)}</div><p class="center"><a href="drinks.html">See brunch cocktails on our drinks menu &rarr;</a></p>{LEGAL}',
  "Weekend brunch at Water Street Tavern, Stoughton WI, Saturday and Sunday 9 am to 2 pm: benedicts, classics, burgers and more.")

courses = "".join(f'<div class="course"><span class="num">{E(n)}</span><h3>{ {"Course One":"House Salad","Course Two":"A Starter to Share","Course Three":"Two Entrées","Course Four":"Dessert to Share"}[n] }</h3><p class="muted" style="max-width:520px;margin:0 auto">{E(d)}</p>{"<ul>"+"".join(f"<li>{E(i)}</li>" for i in items)+"</ul>" if items else ""}</div>' for n,d,items in DATE_COURSES)
def wl(lst): return "".join(item(n+(" ✶" if g else ""), p, "", [], None) for n,g,p in lst)
date = f'''<div class="split" style="align-items:start;gap:70px">
<div class="center"><span class="eyebrow">A Special Couples Menu</span><h2>Date Night for Two</h2><div class="price-badge">$75</div>{courses}
<div class="course" style="border-top:1px solid var(--line);padding-top:34px"><span class="num">Wine</span><h3>Add a Select Bottle</h3><p class="muted">Add a select bottle of red or white for $30.</p></div></div>
<div><div class="mgroup"><div class="ghead"><h2>Red</h2></div>{wl(DATE_RED)}</div><div class="mgroup"><div class="ghead"><h2>White</h2></div>{wl(DATE_WHITE)}</div>
<div class="mgroup"><div class="ghead"><h2>Sangria</h2></div><p>Try a pitcher of our weekly special.</p></div>
<p class="small muted">✶ Wines marked with a star are available by the glass. Select bottles available for $30.</p></div></div>'''
menu_page("date-night.html","Date Night","Every Wednesday","A special couples menu, with an optional bottle of wine to share.","table-candle","date-night.pdf",date,
  "Wednesday Date Night at Water Street Tavern: a four-course couples menu for $75, with an optional bottle of wine.")

ns_days = [
 ("Wednesday","Date Night!","A special couples menu, with an optional bottle of wine to share!","$75 for two","date-night.html","View the Date Night menu"),
 ("Thursday","The Kitchen Is Experimenting","Check out Facebook Thursday afternoon to see what's up!",None,FB,"Follow us on Facebook"),
 ("Friday","Fish Fry","Perch · Bluegill · Walleye","Walleye $27 · Bluegill $27 · Perch $28",None,None),
 ("Saturday","Prime Rib","14 oz of prime rib served with mashed potatoes and brussel sprouts and a house salad.","$39",None,None),
 ("Saturday &amp; Sunday","Brunch","Served 9:00 am – 2:00 pm.",None,"brunch.html","View the Brunch menu"),
]
ns = ""
for d,t,p,price,h,l in ns_days:
    pr = f'<span class="price" style="font-family:var(--serif);font-size:1.3rem;color:var(--green)">{price}</span>' if price else ''
    lk = f'<p style="margin:10px 0 0"><a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}>{l} &rarr;</a></p>' if h else ''
    ns += f'<div class="space reveal" style="min-height:0;grid-template-columns:220px 1fr"><div class="sp-body" style="background:var(--green);color:var(--ivory);padding:40px 30px;justify-content:center"><span class="eyebrow" style="margin:0;color:var(--brass-soft)">{d}</span></div><div class="sp-body" style="padding:40px 46px"><h3 style="font-size:2rem;margin-bottom:.2em">{t}</h3><p style="margin:0 0 6px">{p}</p>{pr}{lk}</div></div>'
b = band("dining-room", '<span class="eyebrow">Something Special Every Night</span><h1>Nightly Specials</h1><hr class="rule"><p>Date night, a kitchen experiment, a Wisconsin fish fry and Saturday prime rib.</p>', "short")
b += f'<section class="section"><div class="wrap">{menu_nav("nightly-specials.html")}<div style="margin-top:56px" class="ns">{ns}</div>{takeout()}</div></section>'
b += '<style>@media(max-width:700px){.ns .space{grid-template-columns:1fr!important}.ns .space .sp-body:first-child{padding:18px 28px!important}}</style>'
page("nightly-specials.html","Nightly Specials","Nightly specials at Water Street Tavern: Wednesday date night, Thursday kitchen experiments, Friday fish fry and Saturday prime rib.","nightly-specials.html",b)

# ---------------- ART-O-MAT ----------------
b = band("art-o-mat-detail", '<span class="eyebrow">Art for a Token</span><h1>The Art-o-mat</h1><hr class="rule"><p>One of the few in the state of Wisconsin.</p>', "")
b += '''<section class="section"><div class="wrap split" style="align-items:start">
<div class="reveal" style="position:sticky;top:120px"><div class="ph" style="background-image:url('img/art-o-mat-sm.jpg')" role="img" aria-label="The Art-o-mat machine at Water Street Tavern"></div></div>
<div class="reveal"><span class="eyebrow">About the Art-o-mat</span><h2>A Vending Machine for Art</h2><hr class="rule left">
<p class="lede">Art-o-mat&reg; machines are retired cigarette vending machines that have been converted to vend art. There are over <a href="https://www.artomat.org/locations/" target="_blank" rel="noopener">200 active machines</a> in various locations throughout the country. Water Street Tavern is one of the few in the state of Wisconsin!</p>
<p>The inspiration for Art-o-mat&reg; came to artist Clark Whittington while observing a friend who had a Pavlovian reaction to the crinkle of cellophane. When the friend heard someone opening a snack from a vending machine, he had the uncontrollable urge to buy a snack as well.</p>
<p>In June 1997, Clark was set to have a solo art show at a local cafe, Penny University in Winston-Salem, N.C. He used a recently-banned cigarette machine to create the first Art-o-mat&reg; and it was exhibited along with 12 of his paintings. The machine sold Polaroid black &amp; white photographs mounted on blocks for $1.00 each.</p>
<p>The show was scheduled to be dismantled in July 1997. However, owner Cynthia Giles loved the machine and asked that it stay permanently. At that point, it was clear that involvement from other artists would be needed if the project was going to continue. Cynthia introduced Clark to a handful of other local artists and the group Artists in Cellophane (AIC) was formed.</p>
<p>The machine remains unaltered and now resides in Delurk Gallery in Winston-Salem, NC.</p>
<p>AIC is the sponsoring organization of Art-o-mat&reg;. The mission of AIC is to encourage art consumption by combining the worlds of art and commerce in an innovative form. AIC believes that art should be progressive, yet personal and approachable. What better way to do this, than with a heavy, cold, steel machine?</p>
<div style="background:var(--ivory);border:1px solid var(--line);padding:34px;margin-top:34px;text-align:center"><h3 style="font-size:1.9rem">Start Your Mini Art Collection</h3><p>Come in and get your token for $5!</p><a class="btn ghost" href="https://www.artomat.org" target="_blank" rel="noopener">Visit the Art-o-mat Website</a></div>
</div></div></section>'''
page("art-o-mat.html","Art-o-mat","Water Street Tavern is home to one of the few Art-o-mat machines in Wisconsin: retired cigarette machines that vend art. Tokens are $5.","art-o-mat.html",b)

# ---------------- GIFT CERTIFICATES ----------------
b = band("bar", '<span class="eyebrow">Give the Tavern</span><h1>Gift Certificates</h1><hr class="rule"><p>Now available, in any amount you wish.</p>', "")
b += f'''<section class="section"><div class="narrow center">
<span class="eyebrow reveal">Gift Certificates Now Available</span><h2 class="reveal">A Gift That's Sure to Be Appreciated</h2><hr class="rule">
<p class="lede reveal">Gift certificates are available in any amount you wish. Just stop in at Water Street Tavern to pick up a gift that is sure to be appreciated!</p>
<div class="reveal" style="border:1px solid var(--line);background:var(--ivory);padding:30px 34px;margin:40px auto 0;max-width:600px"><p style="margin:0"><strong>Good to know:</strong> in case there was any doubt, our gift certificates from before our big remodel will still be honored.</p></div>
<div class="btns reveal" style="justify-content:center;margin-top:40px"><a class="btn" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a><a class="btn ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>'''
page("gift-certificates.html","Gift Certificates","Water Street Tavern gift certificates are available in any amount. Stop in at 324 South Water Street, Stoughton.","gift-certificates.html",b)

# ---------------- RESERVATIONS ----------------
b = band("table-candle", f'<span class="eyebrow">Walk-ins Always Welcome</span><h1>Reservations</h1><hr class="rule"><p>Reserve your table online, or simply stop in.</p><div class="btns" style="justify-content:center;margin-top:28px"><a class="btn light" href="{RESY}" target="_blank" rel="noopener">Book a Reservation</a></div>', "", "68% center")
b += f'''<section class="section"><div class="wrap">
<div class="section-head reveal"><span class="eyebrow">Plan Your Visit</span><h2>Hours</h2><hr class="rule"></div>
{hours_cards()}
</div></section>
<section class="section ivory"><div class="wrap split" style="align-items:start;gap:60px">
<div class="reveal"><span class="eyebrow">Larger Groups</span><h2>Parties of 10 or More</h2><hr class="rule left">
<p>For reservations larger than groups of 9, please call the restaurant during business hours at <a href="{TEL}">{PHONE}</a>, or email <a href="mailto:{EMAIL}?subject=Reservations">{EMAIL}</a>.</p>
<p>Planning a celebration? See <a href="private-events.html">Private Events</a>.</p></div>
<div class="reveal"><span class="eyebrow">By Email</span><h2>Email Requests</h2><hr class="rule left">
<p>For reservation requests via email, please contact us a minimum of 48 hours prior to your desired time, and be sure to include:</p>
<ul class="checklist"><li>Requested date and time</li><li>Number of guests</li><li>Contact phone number</li></ul>
<a class="btn ghost" href="mailto:{EMAIL}?subject=Reservations">Email a Request</a></div>
</div></section>'''
page("reservations.html","Reservations","Book a table at Water Street Tavern in Stoughton, WI on Resy. Walk-ins always welcome. Larger parties please call (608) 480-4001.","reservations.html",b)

# ---------------- ABOUT ----------------
b = band("patio-night", '<span class="eyebrow">On the River in Historic Downtown Stoughton</span><h1>About Water Street Tavern</h1><hr class="rule">', "tall")
b += f'''<section class="section"><div class="narrow">
<div class="center reveal"><span class="eyebrow">Mission Statement</span><h2>An Experience Worth Returning To</h2><hr class="rule"></div>
<p class="lede reveal">Water Street Tavern (WST) is operated by a talented team with an extensive and unique skillset that will allow us to fulfill our goal to be one of the best dining establishments in the area. Our principles are to provide a safe, clean, relaxed environment for everyone; and to be a quality serving establishment for the community.</p>
<p class="reveal">We serve a mix of exceptional burgers, classic comfort food, and elevated entrees in our beautiful, riverfront space. We approach customer service with appreciation and believe it is a privilege to serve our guests.</p>
<p class="reveal">Our commitment goes beyond great food. We strive to be a safe place where everyone, staff included, feel welcome and respected. We celebrate open-mindedness, diversity, and inclusiveness.</p>
<blockquote class="reveal" style="margin:56px 0;padding:36px 0;border-top:1px solid var(--brass-soft);border-bottom:1px solid var(--brass-soft);text-align:center;font-family:var(--serif);font-size:clamp(1.5rem,3vw,2.1rem);line-height:1.35;font-style:italic;color:var(--green)">“The WST family welcomes you. Whether you're joining us for a casual meal, a special celebration, or simply to unwind by the water; come as you are.”</blockquote>
<p class="reveal center">Our goal is simple: to give you an experience worth returning to, again and again.</p>
</div></section>'''
b += band("dining-room", f'<span class="eyebrow">Join Us</span><h2>Dinner Wednesday – Saturday</h2><hr class="rule"><p>Brunch Saturday &amp; Sunday. Walk-ins always welcome.</p><div class="btns" style="justify-content:center;margin-top:26px"><a class="btn light" href="{RESY}" target="_blank" rel="noopener">Book a Table</a><a class="btn outline-light" href="private-events.html">Private Events</a></div>', "")
page("about.html","About","About Water Street Tavern: exceptional burgers, classic comfort food and elevated entrées in a riverfront space in Stoughton, WI. Come as you are.","about.html",b)

# 404 + redirects for old URLs
for old,new in [("home","index.html"),("reservations-1","reservations.html"),("date-night-wednesday","date-night.html")]:
    os.makedirs(os.path.join(ROOT, old), exist_ok=True)
    open(os.path.join(ROOT, old, "index.html"),"w").write(f'<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=../{new}"><link rel="canonical" href="../{new}"><a href="../{new}">Continue</a>')
print("built")
