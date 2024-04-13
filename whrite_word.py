from docx import Document
from lxml import etree
import latex2mathml.converter


def latex_to_word(latex_input):
    mathml = latex2mathml.converter.convert(latex_input)
    tree = etree.fromstring(mathml)
    xslt = etree.parse("MML2OMML.XSL")
    transform = etree.XSLT(xslt)
    new_dom = transform(tree)
    return new_dom.getroot()


def all(input_file, output_file):
    document = Document()
    with open(input_file, "r") as f:
        tex_lines = f.readlines()
    for line in tex_lines:
        if line != "\n":
            p = document.add_paragraph()
            word_math = latex_to_word(line)
            p._element.append(word_math)

    document.save(output_file)


if __name__ == "__main__":
    input_file = "tex.txt"
    output_file = "demo1.docx"
    all(input_file, output_file)
