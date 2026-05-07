/**
 * Generate USCG Industry Day flyer as PowerPoint (.pptx)
 * 8.5x11 portrait (letter size) — single slide
 * Matches the existing PNG flyer layout
 */
const pptxgen = require("pptxgenjs");
const path = require("path");

const OUTPUT = path.join(__dirname, "uscg-industry-day-flyer.pptx");
const LOGO = path.join(__dirname, "../../assets/SanFranciscoPost-Logo-Transparent.png");

// Brand colors (no # prefix for pptxgenjs)
const SAME_BLUE = "003478";
const CG_ORANGE = "CF4E38";
const WHITE = "FFFFFF";
const LIGHT_GRAY = "DCE1EB";
const DARK_NAVY = "002A5A";

// Slide dimensions
const W = 8.5;
const H = 11;

let pres = new pptxgen();
pres.defineLayout({ name: "LETTER_PORTRAIT", width: W, height: H });
pres.layout = "LETTER_PORTRAIT";
pres.author = "SAME San Francisco Post";
pres.title = "USCG Industry Day & Open House - March 12, 2026";

let slide = pres.addSlide();
slide.background = { color: SAME_BLUE };

// === TOP CG ORANGE RACING STRIPE ===
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: W, h: 0.14,
  fill: { color: CG_ORANGE },
});
// Thin white line under stripe
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0.14, w: W, h: 0.03,
  fill: { color: WHITE },
});

// === HEADER ZONE ===
let y = 0.35;

// "INDUSTRY DAY"
slide.addText("INDUSTRY DAY", {
  x: 0.6, y: y, w: 7.3, h: 0.7,
  fontSize: 48, fontFace: "Arial Black", color: WHITE,
  bold: true, margin: 0,
});
y += 0.65;

// "& OPEN HOUSE"
slide.addText("& OPEN HOUSE", {
  x: 0.6, y: y, w: 7.3, h: 0.5,
  fontSize: 34, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, margin: 0,
});
y += 0.55;

// Thin orange rule
slide.addShape(pres.shapes.LINE, {
  x: 0.6, y: y, w: 7.3, h: 0,
  line: { color: CG_ORANGE, width: 2 },
});
y += 0.15;

// "U.S. Coast Guard | Civil Engineering Unit Oakland"
slide.addText("U.S. Coast Guard  |  Civil Engineering Unit Oakland", {
  x: 0.6, y: y, w: 7.3, h: 0.35,
  fontSize: 14, fontFace: "Calibri", color: LIGHT_GRAY,
  margin: 0,
});
y += 0.3;

// "Co-hosted by SAME San Francisco Post"
slide.addText("Co-hosted by SAME San Francisco Post", {
  x: 0.6, y: y, w: 7.3, h: 0.3,
  fontSize: 11, fontFace: "Calibri", color: LIGHT_GRAY,
  margin: 0,
});
y += 0.4;

// === DATE/TIME/LOCATION BAND (CG Orange) ===
const bandTop = y;
const bandH = 0.95;
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: bandTop, w: W, h: bandH,
  fill: { color: CG_ORANGE },
});

// Date info (left side)
slide.addText("THURSDAY", {
  x: 0.6, y: bandTop + 0.08, w: 5, h: 0.25,
  fontSize: 14, fontFace: "Arial Black", color: WHITE,
  bold: true, margin: 0,
});
slide.addText("MARCH 12, 2026", {
  x: 0.6, y: bandTop + 0.3, w: 5, h: 0.35,
  fontSize: 28, fontFace: "Arial Black", color: WHITE,
  bold: true, margin: 0,
});
slide.addText("2:00 PM - 5:00 PM", {
  x: 0.6, y: bandTop + 0.63, w: 5, h: 0.25,
  fontSize: 12, fontFace: "Consolas", color: WHITE,
  margin: 0,
});

// FREE badge (right side — white box with orange text)
const freeX = 6.3;
const freeY = bandTop + 0.18;
slide.addShape(pres.shapes.RECTANGLE, {
  x: freeX, y: freeY, w: 1.6, h: 0.6,
  fill: { color: WHITE },
});
slide.addText("FREE", {
  x: freeX, y: freeY, w: 1.6, h: 0.6,
  fontSize: 32, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, align: "center", valign: "middle", margin: 0,
});

y = bandTop + bandH;

// === MAIN CONTENT ZONE (darker navy) ===
const contentTop = y;
const contentH = 5.45;
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: contentTop, w: W, h: contentH,
  fill: { color: DARK_NAVY },
});

let cy = contentTop + 0.2;

// AGENDA header
slide.addText("AGENDA", {
  x: 0.6, y: cy, w: 7.3, h: 0.3,
  fontSize: 15, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, margin: 0,
});
cy += 0.35;

// Agenda items — rich text array
const agendaItems = [
  { time: "2:00 PM", desc: "Opening Remarks (CEUO CO / SAME SF)" },
  { time: "2:15 PM", desc: "CEUO Briefing" },
  { time: "", desc: "Branch chiefs, structure, contracting process", sub: true },
  { time: "2:30 PM", desc: "Panel Discussion" },
  { time: "", desc: "Opportunities, challenges & Q&A", sub: true },
  { time: "3:15 PM", desc: "Networking + Breakout Sessions" },
  { time: "", desc: "Conf Room H: Industry showcase & networking", sub: true },
  { time: "", desc: "Rooms A-E: Field-specific breakouts & 1-on-1s", sub: true },
  { time: "4:45 PM", desc: "Closing Remarks" },
  { time: "5:00 PM", desc: "Event Complete / No-host Social" },
];

for (const item of agendaItems) {
  if (item.time) {
    // Time + description on same row
    slide.addText(item.time, {
      x: 0.6, y: cy, w: 1.1, h: 0.25,
      fontSize: 11, fontFace: "Consolas", color: WHITE,
      bold: true, margin: 0, valign: "top",
    });
    slide.addText(item.desc, {
      x: 1.75, y: cy, w: 6.15, h: 0.25,
      fontSize: 11, fontFace: "Calibri", color: WHITE,
      margin: 0, valign: "top",
    });
    cy += 0.26;
  } else {
    // Sub-description (indented, lighter)
    slide.addText(item.desc, {
      x: 1.75, y: cy, w: 6.15, h: 0.22,
      fontSize: 10, fontFace: "Calibri", color: LIGHT_GRAY,
      margin: 0, valign: "top",
    });
    cy += 0.22;
  }
}

cy += 0.12;

// Thin divider line
slide.addShape(pres.shapes.LINE, {
  x: 0.6, y: cy, w: 7.3, h: 0,
  line: { color: LIGHT_GRAY, width: 0.5 },
});
cy += 0.18;

// WHO SHOULD ATTEND header
slide.addText("WHO SHOULD ATTEND", {
  x: 0.6, y: cy, w: 7.3, h: 0.3,
  fontSize: 15, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, margin: 0,
});
cy += 0.35;

// Attendee list with bullets
const attendees = [
  "General Contractors & Specialty Subcontractors",
  "A/E Firms & Engineering Consultants",
  "Small Businesses Exploring Federal Contracting",
  "Construction & Facilities Professionals",
];

for (const item of attendees) {
  // Orange bullet dot
  slide.addShape(pres.shapes.OVAL, {
    x: 0.65, y: cy + 0.07, w: 0.08, h: 0.08,
    fill: { color: CG_ORANGE },
  });
  slide.addText(item, {
    x: 0.85, y: cy, w: 6.7, h: 0.24,
    fontSize: 11, fontFace: "Calibri", color: WHITE,
    margin: 0, valign: "top",
  });
  cy += 0.26;
}

cy += 0.1;

// Key messaging
slide.addText("Direct access to Coast Guard civil engineering leadership.", {
  x: 0.6, y: cy, w: 7.3, h: 0.25,
  fontSize: 12, fontFace: "Calibri", color: WHITE,
  bold: true, margin: 0,
});
cy += 0.27;
slide.addText("Real conversations. Real opportunities.", {
  x: 0.6, y: cy, w: 7.3, h: 0.25,
  fontSize: 11, fontFace: "Calibri", color: LIGHT_GRAY,
  margin: 0,
});

// === QUESTIONS / CONTACT BAND ===
const contactTop = contentTop + contentH;
const contactH = 0.85;
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: contactTop, w: W, h: contactH,
  fill: { color: SAME_BLUE },
});
// Thin CG orange line at top of contact band
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: contactTop, w: W, h: 0.025,
  fill: { color: CG_ORANGE },
});

slide.addText("QUESTIONS?", {
  x: 0.6, y: contactTop + 0.1, w: 7.3, h: 0.25,
  fontSize: 14, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, margin: 0,
});
slide.addText("LT Duncan Clark, Construction Manager, CEU Oakland", {
  x: 0.6, y: contactTop + 0.35, w: 7.3, h: 0.22,
  fontSize: 11, fontFace: "Calibri", color: WHITE,
  margin: 0,
});
slide.addText("Duncan.G.Clark@uscg.mil", {
  x: 0.6, y: contactTop + 0.56, w: 7.3, h: 0.22,
  fontSize: 11, fontFace: "Calibri", color: LIGHT_GRAY,
  bold: true, margin: 0,
});

// === BOTTOM SECTION — anchored from bottom up ===

// Bottom CG orange racing stripe
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: H - 0.14, w: W, h: 0.14,
  fill: { color: CG_ORANGE },
});
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: H - 0.17, w: W, h: 0.03,
  fill: { color: WHITE },
});

// Disclaimer (just above bottom stripe)
const disclaimerY = H - 0.37;
slide.addText(
  "This event does not constitute official U.S. Coast Guard endorsement of SAME or any participating organization.",
  {
    x: 0.4, y: disclaimerY, w: 7.7, h: 0.2,
    fontSize: 7, fontFace: "Calibri", color: LIGHT_GRAY,
    align: "center", margin: 0,
  }
);

// Thin separator above disclaimer
const sepY = disclaimerY - 0.1;
slide.addShape(pres.shapes.LINE, {
  x: 0.6, y: sepY, w: 7.3, h: 0,
  line: { color: CG_ORANGE, width: 0.5 },
});

// Logo (above separator)
const logoH2 = 0.5;
const logoW2 = 1.5;
const logoX = (W - logoW2) / 2;
const logoY = sepY - logoH2 - 0.08;

slide.addImage({
  path: LOGO,
  x: logoX, y: logoY, w: logoW2, h: logoH2,
  sizing: { type: "contain", w: logoW2, h: logoH2 },
});

// REGISTER CTA (centered between contact band and logo)
const contactBottom = contactTop + contactH;
const ctaW = 4.5;
const ctaH2 = 0.5;
const ctaX = (W - ctaW) / 2;
const ctaCenterY = (contactBottom + logoY) / 2;
const ctaTop = ctaCenterY - ctaH2 / 2;

slide.addShape(pres.shapes.RECTANGLE, {
  x: ctaX, y: ctaTop, w: ctaW, h: ctaH2,
  fill: { color: SAME_BLUE },
  line: { color: CG_ORANGE, width: 2 },
});
slide.addText("REGISTER: [INSERT LINK HERE]", {
  x: ctaX, y: ctaTop, w: ctaW, h: ctaH2,
  fontSize: 14, fontFace: "Arial Black", color: CG_ORANGE,
  bold: true, align: "center", valign: "middle", margin: 0,
});

// Save
pres.writeFile({ fileName: OUTPUT }).then(() => {
  console.log("PPTX saved to:", OUTPUT);
  console.log("Size: 8.5x11 (Letter Portrait)");
});
