# docx-cyrillic-latin
Transliterator for Cyrillic &lt;-> Latin (Serbian) for .docx files.

## How to use?
There is a streamlit app available at 
https://lightwastak3n-docx-cyrillic-latin-streamlit-app-fv2jfq.streamlitapp.com/
or
https://tinyurl.com/docxlatincyrillic

If you want to run it locally
- You need python docx package `pip install python-docx`
- Import `converter.py` and use `convert_docx()` function.
- To convert file called example.docx from Latin to Cyrillic run `convert_docx("example.docx", "lc")`.
- To convert from Cyrillic to Latin just type anything else (for example `convert_docx("example.docx", "cl")`
