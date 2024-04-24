from fpdf import FPDF


def main():
    username = input("Name: ").strip().title()
    pdf = FPDF()
    
    pdf.add_page()
    pdf.set_font('helvetica', 'B', size=23)
    pdf.cell(text="CS50 Shirtificate", center=True)
    pdf.image('./shirtificate.png', 30, 30, 150)

    pdf.set_font('helvetica', 'B', size=12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-60, 150, f'{username} took CS50', new_x="LMARGIN", align='C')

    pdf.output("shirtificate.pdf")

    print(pdf.cur_orientation)


if __name__ == '__main__':
    main()
