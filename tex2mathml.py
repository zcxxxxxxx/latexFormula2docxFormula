import latex2mathml.converter


def tex2mathml(input):
    return latex2mathml.converter.convert(input)


def convert_file(input_file, output_file):
    with open(input_file, "r") as f:
        tex_lines = f.readlines()

    mathml_lines = []
    for line in tex_lines:
        if line != "\n":
            mathml_code = tex2mathml(line.strip())
            if mathml_code:
                mathml_lines.append(mathml_code + "\n")

    with open(output_file, "w") as f:
        f.writelines(mathml_lines)


if __name__ == "__main__":
    input_file = "tex.txt"
    output_file = "mathml.txt"
    convert_file(input_file, output_file)
