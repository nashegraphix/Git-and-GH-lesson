import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def generate_payslip(employee_id, name, position, salary):
    payslip_file = f"payslip_{employee_id}.pdf"
    c = canvas.Canvas(payslip_file, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica", 12)
    c.drawString(2 * cm, height - 2 * cm, f"Employee ID: {employee_id}")
    c.drawString(2 * cm, height - 3 * cm, f"Name: {name}")
    c.drawString(2 * cm, height - 4 * cm, f"Position: {position}")
    c.drawString(2 * cm, height - 5 * cm, f"Salary: ${salary}")

    c.showPage()
    c.save()
    print(f"Payslip generated for {name} (Employee ID: {employee_id})")






jhvbkjjnnhiiuhnuhionoh








def main():
    excel_file = "employees.xlsx"
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        generate_payslip(row['Employee ID'], row['Name'], row['Position'], row['Salary'])

if __name__ == "__main__":
    main()
