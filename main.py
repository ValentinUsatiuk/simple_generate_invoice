import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class PDF:
    def __init__(self, id_product):
        self.product_id = id_product
        self.count_receipt = 1
        self.name = df.loc[df["id"] == self.product_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.product_id, "price"].squeeze()

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.count_receipt}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")

        self.count_receipt += 1

print(df)
product_id = input("Enter the id of the receipt: ")
pdf = PDF(product_id)
pdf.generate()