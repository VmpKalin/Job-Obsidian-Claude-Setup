#!/usr/bin/env python3
"""Build a cover-letter.docx from a plain-text/markdown body.

Standard library only -- nothing to install. A .docx file is just a ZIP archive
of XML parts, so we assemble the minimal set of parts by hand and zip them up.

The body text is wrapped in a simple letterhead (applicant name + contact line).

Usage:
    python3 build_letter.py --body cover-letter.md --out cover-letter.docx
    python3 build_letter.py --body cover-letter.md --out cover-letter.docx \
            --name "Alex Sample" --contact "alex.sample@example.com | +00 000 000 000"

After building, convert to PDF with LibreOffice headless (optional):
    <soffice> --headless --convert-to pdf --outdir <dir> <dir>/cover-letter.docx
  where <soffice> is:
    Windows: "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
    macOS:   /Applications/LibreOffice.app/Contents/MacOS/soffice
    Linux:   libreoffice   (or soffice)
If LibreOffice is not installed, just keep the .docx.
"""

import argparse
import zipfile
from xml.sax.saxutils import escape

# --- Default (fake, public-safe) letterhead -------------------------------
DEFAULT_NAME = "Alex Sample"
DEFAULT_CONTACT = "alex.sample@example.com | +00 000 000 000 | Sample City"

# --- Fixed ZIP parts that every .docx needs -------------------------------
CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""


def _run(text, bold=False, size=None):
    """A single run of text (one <w:r>). size is in half-points."""
    props = []
    if bold:
        props.append("<w:b/>")
    if size:
        props.append('<w:sz w:val="%d"/>' % size)
        props.append('<w:szCs w:val="%d"/>' % size)
    rpr = "<w:rPr>%s</w:rPr>" % "".join(props) if props else ""
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, escape(text))


def _para(runs, spacing_after=120):
    """A paragraph (<w:p>) from a list of run XML strings."""
    ppr = '<w:pPr><w:spacing w:after="%d"/></w:pPr>' % spacing_after
    return "<w:p>%s%s</w:p>" % (ppr, "".join(runs))


def build_document_xml(body_text, name, contact):
    """Wrap the body in a letterhead and return word/document.xml."""
    paragraphs = []

    # Letterhead: name (big, bold) + contact line, then a blank line.
    paragraphs.append(_para([_run(name, bold=True, size=32)]))
    paragraphs.append(_para([_run(contact, size=18)], spacing_after=240))

    # Body: one <w:p> per line so blank lines are preserved.
    for line in body_text.splitlines():
        if line.strip() == "":
            paragraphs.append(_para([]))  # empty paragraph = blank line
        else:
            paragraphs.append(_para([_run(line, size=22)]))

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>" + "".join(paragraphs) + "</w:body></w:document>"
    )


def build_docx(body_text, out_path, name, contact):
    document_xml = build_document_xml(body_text, name, contact)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document_xml)


def main():
    ap = argparse.ArgumentParser(description="Build cover-letter.docx (stdlib only).")
    ap.add_argument("--body", required=True, help="path to the cover-letter body (txt/md)")
    ap.add_argument("--out", required=True, help="output .docx path")
    ap.add_argument("--name", default=DEFAULT_NAME, help="applicant name for the letterhead")
    ap.add_argument("--contact", default=DEFAULT_CONTACT, help="contact line for the letterhead")
    args = ap.parse_args()

    with open(args.body, "r", encoding="utf-8") as f:
        body_text = f.read()

    build_docx(body_text, args.out, args.name, args.contact)
    print("Wrote %s" % args.out)


if __name__ == "__main__":
    main()
