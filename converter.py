from docx import Document


c_lower = "абвгдђежзијклмнопрстћуфхцчш"
c_upper = c_lower.upper()

l_lower = "abvgdđežzijklmnoprstćufhcčš"
l_upper = l_lower.upper()

cl_digraphs = {
    "љ": "lj", "њ": "nj", "џ": "dž",
    "Љ": "Lj", "Њ": "Nj", "Џ": "Dž"
}

cl_lower = {x:y for x, y in zip(c_lower, l_lower)}
cl_upper = {x:y for x, y in zip(c_upper, l_upper)}
cl_dict = {**cl_lower, **cl_upper, **cl_digraphs}

# lc_dict_digraphs = {"LJ": "Љ", "NJ": "Њ", "DŽ": "Џ"}
lc_dict = {y:x for x, y in cl_dict.items()}
lc_dict = {**lc_dict, "LJ": "Љ", "NJ": "Њ", "DŽ": "Џ"}

# List to check digraphs for latin
lc_digraphs = ["LJ", "Lj", "lj", "NJ", "Nj", "nj", "DŽ", "Dž", "dž"]

def latin_to_cyrillic(text):
    # Replace digraphs
    for digraph in lc_digraphs:
        if digraph in text:
            text = text.replace(digraph, lc_dict[digraph])
    # Replace everything else
    for letter in text:
        if letter in lc_dict:
            text = text.replace(letter, lc_dict[letter])
    return text


def cyrillic_to_latin(text):
    new_text = ""
    for letter in text:
        if letter in cl_dict:
            new_text += cl_dict[letter]
        else:
            new_text += letter
    return new_text


def convert_docx(file, conversion):
    convertor = latin_to_cyrillic if conversion == "lc" else cyrillic_to_latin
    document = Document(file)
    for paragraph in document.paragraphs:
        if paragraph.runs:
            for item in paragraph.runs:
                if item.text != "":
                    item.text = convertor(item.text)
    document.save("converted.docx")

