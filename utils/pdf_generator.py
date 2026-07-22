from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(itinerary):

    pdf_file = "TripMate_Itinerary.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    for line in itinerary.split("\n"):

        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)

    return pdf_file
